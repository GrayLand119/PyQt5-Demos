import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

"""
pip3 install PyQtWebEngine
"""

app = QApplication(sys.argv)

web = QWebEngineView()

web.load(QUrl("https://www.github.com/grayland119"))

web.show()

sys.exit(app.exec_())
