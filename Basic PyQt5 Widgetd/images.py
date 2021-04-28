import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using labels')
        self.setGeometry(100, 100, 500, 500)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('../images/logo.png'))
        self.image.move(50,50)

        removeButton = QPushButton("Remove", self)
        removeButton.move(50,15)
        removeButton.clicked.connect(self.removeFunc)

        showButton = QPushButton("Show", self)
        showButton.move(150,15)
        showButton.clicked.connect(self.showFunc)





        self.show()
    def removeFunc(self):
        self.image.close()

    def showFunc(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
