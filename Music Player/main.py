import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 480, 700)

        self.setWindowTitle("Music Player")

        # self.setFixedWidth(500)
        # self.setFixedHeight(500)

        self.UI()

    def UI(self):
        self.widgets()
        self.layouts()

    def layouts(self):
        ##################Creating Layouts#########################
        self.mainLayout = QVBoxLayout()
        self.topMainLayout = QVBoxLayout()
        self.topGroupBox = QGroupBox("Music Player")
        self.topGroupBox.setStyleSheet("background-color:#fcc324")
        self.topLayout = QHBoxLayout()
        self.middleLayout = QHBoxLayout()
        self.bottomLayout = QVBoxLayout()

        ###################Adding Widgets##########################
        ################Top layout widgets#########################
        self.topLayout.addWidget(self.progessBar)

        ################Middle Layout Widgets######################
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.previousButton)

        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        self.topGroupBox.setLayout(self.topMainLayout)
        self.mainLayout.addWidget(self.topGroupBox)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)


    def widgets(self):
        #####################Progress bar###########################
        self.progessBar = QProgressBar()
        #######################Buttons##############################
        self.addButton =QToolButton()
        self.addButton.setIcon(QIcon("icons/add.png"))
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a song")

        self.shuffleButton = QToolButton()
        self.shuffleButton.setIcon(QIcon("icons/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48, 48))
        self.shuffleButton.setToolTip("Shuffle the list")

        self.previousButton = QToolButton()
        self.previousButton.setIcon(QIcon("icons/previous.png"))
        self.previousButton.setIconSize(QSize(48, 48))
        self.previousButton.setToolTip("Previous Song")




def main():
    App = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(App.exec())


if __name__ == '__main__':
    main()
