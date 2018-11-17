from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *
from satide.BlockCreator.Functions.BaseFunctions import BaseVariable,BaseFunction


class ForBlock(BaseFunction):

    def __init__(self):
        BaseFunction.__init__(self)
        self.distance = 70
        self.layout = QGridLayout()
        self.setLayout(self.layout)


        self.setMaximumSize(self.distance * 4, self.distance * 2)
        self.block_title()


    def block_title(self):
        self.title = QFrame()
        self.title_layout = QGridLayout()
        self.title.setLayout(self.title_layout)


        self.title_layout.addWidget(QLabel("For"), 0, 0)
        self.title_layout.addWidget(QLabel("in"), 0, 2)


        self.iterable = BaseVariable()
        self.title_layout.addWidget(self.iterable, 0, 1)
        self.container = BaseVariable()
        self.title_layout.addWidget(self.container, 0, 3)


        self.layout.setMenuBar(self.title)
