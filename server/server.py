import socket

from config import DEFAULT_ADDRESS, ENCODING
from calculator import Calculator, CalculatorException
from db_scripts import add_info, load_info, create_db, DBException


def recv_until_end(connection: socket) -> str:
    result = ''
    while True:
        part = connection.recv(1024).decode(ENCODING)
        if not part:
            break
        result += part
        if result[-1] == '#':
            result = result[:-1]
            break
    return result


def execute_prompt(prompt: str, calculator: Calculator = Calculator()) -> str:
    try:
        if not prompt:
            return load_info()

        result = calculator.calculate(prompt)
        add_info(prompt, result)
        return str(result)

    except CalculatorException as e:
        return '#' + str(e)

    except DBException:
        return '#Database error occurred.'


def serve(bind=DEFAULT_ADDRESS):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(bind)

    create_db()

    while True:
        server.listen()
        connection, _ = server.accept()

        prompt = recv_until_end(connection)
        result = execute_prompt(prompt)

        connection.sendall(result.encode(ENCODING))
        connection.close()


if __name__ == "__main__":
    serve()
