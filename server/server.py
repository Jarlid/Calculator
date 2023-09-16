import socket

from config import DEFAULT_ADDRESS, MAX_LEN, ENCODING
from calculator import Calculator


def serve(bind=DEFAULT_ADDRESS):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(bind)

    calculator = Calculator()

    while True:
        server.listen()
        connection, _ = server.accept()

        prompt = connection.recv(MAX_LEN).decode(ENCODING)
        result = calculator.calculate(prompt)

        connection.send(str(result).encode(ENCODING))
        connection.close()


if __name__ == "__main__":
    serve()
