from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFontDialog, QColorDialog, QFileDialog, \
    QMessageBox
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.Qt import QFileInfo


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QToolbar"
        self.top = 200
        self.left = 500
        self.width = 680
        self.height = 480
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createEditor()
        self.CreateMenu()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')
        printAction = QAction(QIcon("icon.png"), "Print", self)
        printAction.triggered.connect(self.printDialog)
        fileMenu.addAction(printAction)
        printPreviewAction = QAction(QIcon("icon.png"), "Print Preview", self)
        printPreviewAction.triggered.connect(self.printpreviewDialog)
        fileMenu.addAction(printPreviewAction)
        exportpdfAction = QAction(QIcon("icon.png"), "Export PDF", self)
        exportpdfAction.triggered.connect(self.printPDF)
        fileMenu.addAction(exportpdfAction)
        exiteAction = QAction(QIcon("icon.png"), 'Exit', self)
        exiteAction.setShortcut("Ctrl+E")
        exiteAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exiteAction)
        copyAction = QAction(QIcon("icon.png"), 'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)
        saveAction = QAction(QIcon("icon.png"), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        editMenu.addAction(saveAction)
        pasteAction = QAction(QIcon("icon.png"), 'Paste', self)
        pasteAction.setShortcut("Ctrl+P")
        editMenu.addAction(pasteAction)
        fontAction = QAction(QIcon("font.png"), "Font", self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)
        colorAction = QAction(QIcon("icon.png"), "Color", self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)
        helpAction = QAction(QIcon('icon.png'), "About Application", self)
        helpAction.triggered.connect(self.AboutmessageBox)
        helpMenu.addAction(helpAction)
        choiceAction = QAction(QIcon('icon.png'), "Choice MessageBox", self)

        choiceAction.triggered.connect(self.choiceMessageBox)
        helpMenu.addAction(choiceAction)
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(exiteAction)
        self.toolbar.addAction(fontAction)
        self.toolbar.addAction(colorAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(printPreviewAction)
        self.toolbar.addAction(exportpdfAction)
        self.toolbar.addAction(helpAction)

    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def printPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "": fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def AboutmessageBox(self):
        QMessageBox.about(self, "About Application", "This is a simple texteditor application")

    def choiceMessageBox(self):
        message = QMessageBox.question(self, "Choice Message", "Do You Like PyQt5 ?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if message == QMessageBox.Yes:
            print("Yes I Like PyQt5")
        else:
            print("No I Dot Like PyQt5")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
