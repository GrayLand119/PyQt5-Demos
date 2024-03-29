from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QWizard, QVBoxLayout, QPushButton, QWizardPage
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Wizard"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        button = QPushButton("Launch")
        button.clicked.connect(self.btn_clicked)

        vbox.addWidget(button)

        self.setLayout(vbox)

        self.wizard = QWizard()
        self.wizard.setWindowTitle("Launcher Page")
        page1 = QWizardPage()
        page1.setTitle("p11111")

        page2 = QWizardPage()
        page2.setTitle("page 2")
        self.wizard.addPage(page1)
        self.wizard.addPage(page2)

        self.show()

    def btn_clicked(self):
        self.wizard.open()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
