import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout()
        # btn1=QPushButton("Button1")
        # btn2=QPushButton("Button2")
        # btn3=QPushButton("Button3")
        # btn4=QPushButton("Button4")
        # btn5=QPushButton("Button5")
        # self.gridLayout.addWidget(btn1,1,0)
        # self.gridLayout.addWidget(btn2,1,1)
        # self.gridLayout.addWidget(btn3,1,2)
        # self.gridLayout.addWidget(btn4,2,0)
        # self.gridLayout.addWidget(btn5,2,1)
        x = 7
        y = 10
        for i in range(0, 3):
            for j in range(x, y):
                btn = QPushButton(str(j))
                self.gridLayout.addWidget(btn, i, j-x)
                btn.clicked.connect(self.clickMe)

            x -= 3
            y -= 3

        self.setLayout(self.gridLayout)
        self.show()

    def clickMe(self):
        buttonID = self.sender().text()
        print(buttonID)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
