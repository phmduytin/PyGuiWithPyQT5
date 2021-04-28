import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using labels')
        self.setGeometry(100, 100, 350, 350)
        self.UI()

    def UI(self):

        self.nameText = QLabel("Username:", self)
        self.nameText.move(60,50)
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Enter usename...")
        self.nameTextBox.move(120, 50)

        self.passText = QLabel("Password:", self)
        self.passText.move(60, 80)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Enter password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120, 80)


        self.text = QLabel("Save", self)
        self.text.move(150,210)
        btnEnter = QPushButton("Enter", self)
        btnEnter.move(180,110)
        btnEnter.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("Your name is: " + name + " and Your password: " + password)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
