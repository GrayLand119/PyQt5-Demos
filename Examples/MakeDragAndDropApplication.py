from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()
        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.setGeometry(300, 350, 500, 300)
        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)

        l1 = QListWidgetItem(QIcon('copy.png'), "C++")
        l2 = QListWidgetItem(QIcon('Paste.png'), "C# ")
        l3 = QListWidgetItem(QIcon('print.png'), "Java")
        l4 = QListWidgetItem(QIcon('save.png'), "Python")

        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        self.myListWidget1.insertItem(3, l3)
        self.myListWidget1.insertItem(4, l4)

        QListWidgetItem(QIcon('football.png'), "HTLM", self.
                        myListWidget2)
        QListWidgetItem(QIcon('tenis.png'), "CSS", self.
                        myListWidget2)
        QListWidgetItem(QIcon('cricket.png'), "Javascript", self.
                        myListWidget2)

        self.setWindowTitle('Drag and Drop Example');
        self.setLayout(self.myLayout)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
