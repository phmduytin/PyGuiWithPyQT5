import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialogs")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileButton = QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)
        fontButton=QPushButton("Change Font")
        fontButton.clicked.connect(self.changeFont)
        colorButton=QPushButton("Change Color")
        colorButton.clicked.connect(self.changeColor)

        vbox.addWidget(self.editor)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addWidget(fontButton)
        hbox.addWidget(colorButton)
        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

    def openFile(self):
        url = QFileDialog.getOpenFileName(self, "Open a file", "", "All File(*);;*txt")
        fileUrl = url[0]
        # self.s = ""
        with open(fileUrl, 'r') as f:
            s = f.read()
        self.editor.setText(s)

    def changeFont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
