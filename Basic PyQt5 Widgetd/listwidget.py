import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using List Widget')
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget=QListWidget(self)
        self.listWidget.move(100,80)

        list1 = ["Batman", "Superman", "Spiderman"]
        ########
        self.listWidget.addItems(list1)
        self.listWidget.addItem("Heman")

        # for number in range(5,11):
        #     self.listWidget.addItem(str(number))

        ######################################################
        btnAdd = QPushButton("Add", self)
        btnAdd.move(380,85)
        btnAdd.setFont(font)
        btnAdd.resize(100,35)
        btnAdd.clicked.connect(self.addFunc)
        btnDel = QPushButton("Delete", self)
        btnDel.move(380,135)
        btnDel.setFont(font)
        btnDel.resize(100, 35)
        btnDel.clicked.connect(self.delFunc)
        btnGet = QPushButton("Get", self)
        btnGet.move(380,185)
        btnGet.setFont(font)
        btnGet.resize(100, 35)
        btnGet.clicked.connect(self.getFunc)
        btnDelteAll = QPushButton("Delete All", self)
        btnDelteAll.move(380, 235)
        btnDelteAll.setFont(font)
        btnDelteAll.resize(100, 35)
        btnDelteAll.clicked.connect(self.deleteAllFunc)


        self.show()

    def addFunc(self):
        val = self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")

    def delFunc(self):
        idx = self.listWidget.currentRow()
        self.listWidget.takeItem(idx)

    def getFunc(self):
        idx = self.listWidget.currentItem().text()
        QMessageBox.information(self, "getFunc", idx)

    def deleteAllFunc(self):
        self.listWidget.clear()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
