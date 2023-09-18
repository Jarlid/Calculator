import socket

from config import DEFAULT_ADDRESS, ENCODING
from calculator import Calculator, CalculatorException


class DummyException(Exception):  # TODO: удалить после добавления БД.
    pass


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
            # TODO: достать историю из БД.
            # load_info()
            return "#"

        result = calculator.calculate(prompt)
        # TODO: отправить в БД.
        # add_info(prompt, result)
        return str(result)

    except CalculatorException as e:
        return '#' + str(e)

    except DummyException:  # TODO: заменить DummyException на Exception от БД.
        return '#Database error occurred.'


def serve(bind=DEFAULT_ADDRESS):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(bind)

    while True:
        server.listen()
        connection, _ = server.accept()

        prompt = recv_until_end(connection)
        result = execute_prompt(prompt)

        connection.sendall(result.encode(ENCODING))
        connection.close()


if __name__ == "__main__":
    serve()
