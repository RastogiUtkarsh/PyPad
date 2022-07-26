import sys
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
class PyPad(QMainWindow):
    def __init__(self):
        super(PyPad, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(20)
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.setWindowTitle('PyPad :)')
        self.make_toolbar()
        self.make_menu()

    def spellchek(self,text):
        fml = QTextCharFormat()
        fml.setBackground(QColor('yellow'))
    def make_toolbar(self):
        toolbar = QToolBar()
        undoact = QAction('Undo',self)
        undoact.triggered.connect(self.editor.undo)
        toolbar.addAction(undoact)

        redoact = QAction('Redo', self)
        redoact.triggered.connect(self.editor.redo)
        toolbar.addAction(redoact)

        toolbar.addSeparator()
        toolbar.addSeparator()

        copyact = QAction('Copy',self)
        copyact.triggered.connect(self.editor.copy)
        toolbar.addAction(copyact)

        pasteact = QAction('Paste', self)
        pasteact.triggered.connect(self.editor.paste)
        toolbar.addAction(pasteact)

        self.font_box = QSpinBox()
        self.font_box.setValue(20)
        self.font_box.valueChanged.connect(self.setfontsize)
        toolbar.addWidget(self.font_box)

        self.make_menu()
        self.addToolBar(toolbar)
    def make_menu(self):
        menu = QMenuBar()

        filemenu = QMenu('File',self)
        menu.addMenu(filemenu)

        savepdfact = QAction('Save as PDF',self)
        savepdfact.triggered.connect(self.savepdf)

        filemenu.addAction(savepdfact)

        menu.addSeparator()

        about = QMenu('About',self)
        menu.addMenu(about)

        self.setMenuBar(menu)

    def savepdf(self):
        path , _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(path)
        self.editor.document().print_(printer)
    def setfontsize(self):
        value = self.font_box.value()
        self.editor.setFontPointSize(value)


app = QApplication(sys.argv)
window = PyPad()
window.show()
sys.exit(app.exec_())
