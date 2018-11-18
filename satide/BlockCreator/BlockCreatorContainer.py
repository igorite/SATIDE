from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *
from satide.BlockCreator.BlockCreatorFunctions import BlockCreatorFunctions
from satide.BlockCreator.BlockCreatorView import BlockCreatorView


class BlockCreatorContainer(QFrame):

    def __init__(self, parent):

        # Initial Configuration
        QFrame.__init__(self)
        self.parent = parent

        self.setObjectName("block_creator")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Add Functions block
        self.functions = BlockCreatorFunctions(self)
        self.layout.addWidget(self.functions, 0, 0)

        # Add View
        self.view = BlockCreatorView(self)
        self.layout.addWidget(self.view, 0, 1)

        self.functions.load()
        self.view.load()
