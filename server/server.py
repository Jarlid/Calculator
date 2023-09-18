import socket

from config import DEFAULT_ADDRESS, MAX_LEN, ENCODING
from calculator import Calculator, CalculatorException


class DummyException(Exception):  # TODO: удалить после добавления БД.
    pass


def execute_prompt(prompt: str, calculator: Calculator = Calculator()) -> str:
    try:
        if prompt == '#':
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

        prompt = connection.recv(MAX_LEN).decode(ENCODING)
        result = execute_prompt(prompt)

        connection.send(result.encode(ENCODING))
        connection.close()


if __name__ == "__main__":
    serve()
