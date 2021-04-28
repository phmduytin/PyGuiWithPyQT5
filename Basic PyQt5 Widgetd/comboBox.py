import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Comboboxes')
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton("Save",self)
        button.move(150,130)

        self.combo.addItem("Tien")
        self.combo.addItem("Hiep")
        self.combo.addItems(["123", "3432"])
        list1 = ["Batman", "Superman", "Spiderman"]

        self.combo.addItems(list1)

        button.clicked.connect(self.showCombo)


        self.show()

    def showCombo(self):
        value = self.combo.currentText()
        idx = self.combo.currentIndex()

        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
