from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

import sys
import os


PATH_TO_UI = os.path.join('UI', 'UI.ui')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(PATH_TO_UI, self)
        self._bind_buttons()
    
    def _bind_buttons(self):
        self.button_1.clicked.connect(self.on_button_click)
    
    def on_button_click(self, e):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
