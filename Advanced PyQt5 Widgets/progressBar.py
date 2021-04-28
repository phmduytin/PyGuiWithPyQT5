import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProgressBar Widget")
        self.setGeometry(350, 150, 500, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox=QHBoxLayout()
        self.progressBar = QProgressBar()
        btnStart = QPushButton("Start")
        btnStart.clicked.connect(self.timerStart)
        btnStop = QPushButton("Stop")
        btnStop.clicked.connect(self.timerStop)
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.runProgressBar)


        vbox.addWidget(self.progressBar)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def runProgressBar(self):
        global count
        count +=1
        self.progressBar.setValue(count)
        if count == 100:
            self.timer.stop()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        global count
        count = 0
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
