import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabel Widget")
        self.setGeometry(350,150,600,500)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        self.table=QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()

        self.table.setItem(0,0,QTableWidgetItem("First Item"))
        self.table.setItem(0,1,QTableWidgetItem("First Item"))
        self.table.setItem(4,2,QTableWidgetItem("Final Item"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.doubleClick)
        #self.table.currentItem().connect(self.getValue())

        btn =QPushButton("Get")
        btn.clicked.connect(self.getValue)

        vbox.addWidget(self.table)
        vbox.addWidget(btn)

        self.setLayout(vbox)

        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())
    def doubleClick(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
