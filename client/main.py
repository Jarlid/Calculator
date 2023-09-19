from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

import socket
import sys
import os

from utils import recv_until_closed


PATH_TO_UI = os.path.join('UI', 'UI.ui')
ACCEPTABLE_SYMBOLS = '0123456789.()+-*/e'

PORT = 6666
IP = '127.0.0.1'
DEFAULT_SERVER_ADDRESS = (IP, PORT)

ENCODING = 'ascii'


class MainWindow(QMainWindow):
    def __init__(self, server_address=DEFAULT_SERVER_ADDRESS):
        super().__init__()
        self.server_address = server_address
        uic.loadUi(PATH_TO_UI, self)
        self._bind_buttons()
        self.lineEdit.textChanged.connect(self.validate_input)
        self.historyBrowser.setText(self.get_history())
    
    def _bind_buttons(self):
        def write_symbol_on_lineEdit(symbol):
            return lambda _: self.lineEdit.setText(f'{self.lineEdit.text()}{symbol}')
        
        for button, symbol in ((self.button_1, '1'),
                               (self.button_2, '2'),
                               (self.button_3, '3'),
                               (self.button_4, '4'),
                               (self.button_5, '5'),
                               (self.button_6, '6'),
                               (self.button_7, '7'),
                               (self.button_8, '8'),
                               (self.button_9, '9'),
                               (self.button_0, '0'),
                               (self.button_point, '.'),
                               (self.button_sum, '+'),
                               (self.button_diff, '-'),
                               (self.button_mul, '*'),
                               (self.button_div, '/'),
                               (self.button_openbracket, '('),
                               (self.button_closebracket, ')')
                               ):
            button.clicked.connect(write_symbol_on_lineEdit(symbol))
        self.button_C.clicked.connect(lambda _: self.lineEdit.setText(''))
        self.button_enter.clicked.connect(self.calculate)
    
    def get_history(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall('#'.encode(ENCODING))
            data = recv_until_closed(sock).decode(ENCODING)
        return data
    
    def validate_input(self, input_expression):
        if all(symbol in ACCEPTABLE_SYMBOLS for symbol in input_expression):
            return
        text = ''.join(symbol for symbol in input_expression if symbol in ACCEPTABLE_SYMBOLS)
        self.lineEdit.setText(text)
    
    def calculate(self):
        expression = self.lineEdit.text()
        if not expression:
            return
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall((expression + '#').encode(ENCODING))
            result = recv_until_closed(sock).decode(ENCODING)
        if result.startswith('#'):
            error_msg = QMessageBox()
            error_msg.setWindowTitle('Error!')
            error_msg.setText(result[1:].strip())
            error_msg.exec_()
            return
        self.lineEdit.setText(result)
        self.historyBrowser.setText(f'{self.historyBrowser.toPlainText()}\n{expression}={result}')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
