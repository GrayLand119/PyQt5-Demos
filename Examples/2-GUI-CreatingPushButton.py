from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect, QSize
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.title = 'My window'
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon_char_g.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.UIComponents()

        self.show()

    def UIComponents(self):
        button = QPushButton('Click Me', self)
        button.setIcon(QtGui.QIcon("icon_char_g.png"))
        button.setIconSize(QSize(32, 32))
        button.setToolTip("<h2>This is Click Me Button</h2>")
        button.setGeometry(10, 10, 150, 40)
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print("Did click me !!")



App = QApplication(sys.argv)
window = MyWindow()
sys.exit(App.exec())
