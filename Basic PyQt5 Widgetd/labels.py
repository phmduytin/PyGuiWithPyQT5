import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using labels')
        self.setGeometry(100, 100, 350, 350)
        self.UI()

    def UI(self):
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello World", self)
        text1.move(100,50)
        text2.move(100,100)


        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
