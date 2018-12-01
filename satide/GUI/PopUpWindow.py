from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.GUI.StyleSheet import stylesheet
from satide.img import ImgLoader
import os




class PopUpWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setStyleSheet(stylesheet)
        self.setObjectName("pop_up")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(ImgLoader.load_icon("logo_small"))
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.title_bar = QFrame()
        self.title_bar.setMinimumHeight(30)
        self.title_bar.setObjectName("pop_up_title_bar")
        self.title_bar_layout = QGridLayout()
        self.title_bar_layout.setColumnStretch(1, 10)
        self.title_bar_layout.setColumnStretch(2, 5)
        self.title_bar_layout.setColumnStretch(3, 10)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setLayout(self.title_bar_layout)
        self.title = QLabel("title")
        self.title.setObjectName("pop_up_title")
        self.title_bar_layout.addWidget(self.title, 0, 2)

        self.close_button = QPushButton()
        self.close_button.setIconSize(QSize(25, 25))
        self.close_button.setObjectName("close")
        self.close_button.setIcon(ImgLoader.load_icon("close"))
        self.close_button.clicked.connect(self.close)
        self.title_bar_layout.addWidget(self.close_button, 0, 4)

        self.layout.addWidget(self.title_bar, 0, 0)

        self.main_frame = QFrame()
        self.layout.addWidget(self.main_frame, 1, 0)

        super().setLayout(self.layout)

    def setLayout(self, QLayout, overrride=True):
        self.main_frame.setLayout(QLayout)



    def setTitle(self, title):
        self.title.setText(title)
        self.setWindowTitle(title)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)