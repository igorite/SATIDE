from PyQt5.QtCore import *
from PyQt5.QtGui import *
from satide.GUI.BlockContainer import BlockContainer
from satide.GUI.StyleSheet import stylesheet
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        self.app = None
        self.toolbar = None

        # Create Window
        self.create_window()

        QWidget.__init__(self)
        self.resize(800, 800)
        self.center()

        # Load icon
        self.setWindowIcon(QIcon("img/logo_small.png"))

        # Create block container
        self.mdi = BlockContainer(self)
        scrollbar = QScrollBar()
        scrollbar.setFixedWidth(50)
        scrollbar.setFixedHeight(50)
        scrollbar.show()
        scrollbar.setMinimum(70)
        self.mdi.addScrollBarWidget(scrollbar, Qt.AlignTop)
        self.setCentralWidget(self.mdi)
        self.show()

        self.setStyleSheet(stylesheet)

        # Create Toolbar
        self.create_toolbar()

        # Execute app
        self.app.exec_()

    def create_window(self):
        self.app = QApplication([])
        # self.app.setStyle('fusion')
        self.app.setApplicationName("SATIDE")

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create_toolbar(self):
        toolbar_box = QToolBar(self)
        toolbar_box.setIconSize(QSize(40, 40))
        self.toolbar = self.addToolBar(Qt.LeftToolBarArea, toolbar_box)


        exit_act = QAction(QIcon("img/add_block.png"), "Add a new block", self)
        exit_act.setShortcut("Ctrl+B")
        exit_act.triggered.connect(self.mdi.create_block)
        toolbar_box.addAction(exit_act)

        zoom_in_act = QAction(QIcon("img/zoom_in.png"), "Zoom in", self)
        zoom_in_act.setShortcut("Ctrl++")
        zoom_in_act.triggered.connect(self.mdi.zoom_in)
        toolbar_box.addAction(zoom_in_act)

        zoom_out_act = QAction(QIcon("img/zoom_out.png"), "Zoom out", self)
        zoom_out_act.setShortcut("Ctrl+-")
        zoom_out_act.triggered.connect(self.mdi.zoom_out)
        toolbar_box.addAction(zoom_out_act)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
