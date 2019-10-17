from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
import PyQt5 as Qt
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        # super(MyWindow, self).__init__()
        super().__init__()

        self.title = 'My window'
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 500
        self.iconName = "icon_char_g.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon_char_g.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.UIComponents()
        # vLayout = QVBoxLayout()
        # vLayout.addWidget(self.groupBox)
        #
        # self.setLayout(vLayout)


        self.show()

    def UIComponents(self):
        self.groupBox = QGroupBox("Group title here", self)
        vLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()

        button1 = QPushButton('Click Me 1', self)
        button1.setIcon(QtGui.QIcon("icon_char_g.png"))
        button1.setIconSize(QSize(32, 32))
        button1.setToolTip("<h2>This is Click Me Button</h2>")
        button1.setMinimumHeight(40)
        button1.clicked.connect(self.ClickMe)
        hboxLayout.addWidget(button1)

        button2 = QPushButton('Click Me 2', self)
        button2.setIcon(QtGui.QIcon("icon_char_g.png"))
        button2.setIconSize(QSize(32, 32))
        button2.setToolTip("<h2>This is Click Me Button</h2>")
        button2.setMinimumHeight(40)
        button2.clicked.connect(self.ClickMe)
        hboxLayout.addWidget(button2)

        vLayout.addChildLayout(hboxLayout)
        self.setLayout(vLayout)
        # self.groupBox.setLayout(hboxLayout)



    # def createLayout(self):



    def ClickMe(self):
        print("Did click me !!")




App = QApplication(sys.argv)
window = MyWindow()
sys.exit(App.exec())
