from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, pyqtSlot, pyqtSignal
from PyQt5 import QtCore


class Window(QMainWindow):
    mySignal = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        title = "PyQt5 Signal And Slots"
        left = 500
        top = 200
        width = 500
        height = 250
        iconName = "icon.png"
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.CreateButton()

        # self.mySignal = pyqtSignal()

        self.mySignal.connect(self.my_slot)
        self.mySignal.emit(2, 2)

        self.show()

    def CreateButton(self):
        button = QPushButton("Close Application", self)
        button.setGeometry(QRect(100, 100, 211, 48))
        button.setIcon(QtGui.QIcon("exit.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.clicked.connect(self.ButtonAction)

    @pyqtSlot()
    def ButtonAction(self):
        sys.exit()

    @pyqtSlot(int, int)
    def my_slot(self, a=0, b=0):
        print("my_slot function called.", a, b)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
