import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
import random

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
scoreCom = 0
scorePlay = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Paper Game')
        self.setGeometry(350, 150, 550, 500)
        self.UI()

    def UI(self):
        ##################Scores##########################
        self.scoreComputerText = QLabel("Computer Score: ", self)
        self.scoreComputerText.move(50, 20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel("Your Score: ", self)
        self.scorePlayerText.move(350, 20)
        self.scorePlayerText.setFont(textFont)

        ###################Images##########################
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("../images/rock.png"))
        self.imageComputer.move(50, 100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("../images/rock.png"))
        self.imagePlayer.move(350, 100)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap("../images/game.png"))
        self.imageGame.move(250, 200)
        ###############Buttons#######################
        btnStart = QPushButton("Start", self)
        btnStart.setFont(buttonFont)
        btnStart.move(160, 280)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.setFont(buttonFont)
        btnStop.move(300, 280)
        btnStop.clicked.connect(self.stop)

        ################Timer########################
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        self.timer.start()

    def stop(self):
        global scoreCom
        global scorePlay
        self.timer.stop()
        x = scoreCom
        y = scorePlay

        if self.valueComputer == 1:
            if self.valuePlayer == 2:
                scorePlay += 1
            elif self.valuePlayer == 3:
                scoreCom += 1
        elif self.valueComputer == 2:
            if self.valuePlayer == 3:
                scorePlay += 1
            elif self.valuePlayer == 1:
                scoreCom += 1
        else:
            if self.valuePlayer == 1:
                scorePlay += 1
            elif self.valuePlayer == 2:
                scoreCom += 1

        if scoreCom > x:
            self.mbox = QMessageBox.information(self, "Information", "Computer win!!!")
        elif scorePlay > y:
            self.mbox = QMessageBox.information(self, "Information", "You win!!!")
        else:
            self.mbox = QMessageBox.information(self, "Information", "Draw game!!!")

        self.scoreComputerText.resize(250, 20)
        self.scoreComputerText.setText("Computer Score: " + str(scoreCom))
        self.scorePlayerText.resize(150, 20)
        self.scorePlayerText.setText("Your Score: " + str(scorePlay))

    def playGame(self):
        self.valueComputer = random.randint(1, 3)
        self.valuePlayer = random.randint(1, 3)

        if self.valueComputer == 1:
            self.imageComputer.setPixmap(QPixmap("../images/rock.png"))
        elif self.valueComputer == 2:
            self.imageComputer.setPixmap(QPixmap("../images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("../images/scissors.png"))

        if self.valuePlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("../images/rock.png"))
        elif self.valuePlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("../images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("../images/scissors.png"))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
