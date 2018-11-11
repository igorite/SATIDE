from PyQt5.QtCore import *
from PyQt5.QtGui import *
from satide.Blocks.BlockContainer import BlockContainer
from satide.Steps.Steps import Steps
from satide.GUI.StyleSheet import stylesheet
from PyQt5.QtWidgets import *
import os



class MainWindow(QMainWindow):

    def __init__(self, dir_name = None):
        self.app = None
        self.toolbar = None
        self.blocks_button = None
        self.steps_button = None
        if dir_name is not None:
            self.dir_name = dir_name
        else:
            self.dir_name = os.path.dirname(__file__)

        # Create Window
        self.create_window()
        QWidget.__init__(self)
        self.resize(800, 800)
        self.center()

        # Load icon
        self.setWindowIcon(QIcon(os.path.join(self.dir_name, "img/logo_small.png")))
        # Create block container
        self.mdi = BlockContainer(self)
        self.mdi_frame = QFrame()
        self.mdi_frame.setObjectName("mdi_frame")
        self.mdi_frame_layout = QGridLayout()
        self.mdi_frame.setLayout(self.mdi_frame_layout)
        self.mdi_frame_layout.addWidget(self.mdi, 0, 1)

        # Create bar
        self.bar = QFrame()
        self.bar.setObjectName("bar")
        self.bar_layout = QGridLayout()
        self.create_bar()

        # Create central frame
        self.central_frame = QFrame()
        self.central_frame.setObjectName("central_frame")
        self.central_frame_layout = QGridLayout()
        self.central_frame.setLayout(self.central_frame_layout)
        self.central_frame_layout.addWidget(self.bar)
        self.central_frame_layout.addWidget(self.mdi_frame)
        self.setCentralWidget(self.central_frame)

        # Create Steps Frame
        self.steps = Steps()
        self.steps_layout = QGridLayout()

        # Set StyleSheet
        self.setStyleSheet(stylesheet)

        # Create Toolbar
        self.create_toolbar()

        # Execute app
        self.show()


    def create_bar(self):
        self.bar.setLayout(self.bar_layout)

        # Create test case creator
        self.blocks_button = QPushButton("oops")
        self.bar_layout.addWidget(self.blocks_button, 0, 0)


        # create Block creator
        self.steps_button = QPushButton("Steps")
        self.bar_layout.addWidget(self.steps_button, 0, 1)


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
        toolbar_box.setOrientation(Qt.Vertical)
        toolbar_box.setIconSize(QSize(40, 40))
        self.mdi_frame_layout.addWidget(toolbar_box, 0, 0)


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
