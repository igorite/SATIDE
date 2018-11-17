from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *
from satide.Blocks.Block import BaseBlock, BaseVariable
from satide.BlockCreator.BlockCreatorContainer import BlockCreatorContainer
from satide.BlockCreator.BlockCreatorToolbar import BlockCreatorToolbar


class BlockCreatorFrame(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.toolbar = QToolBar()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Add Block Creator Toolbar
        self.toolbar = BlockCreatorToolbar()
        self.layout.addWidget(self.toolbar, 0, 0)


        # Add Block Creator Container
        self.creator_container = BlockCreatorContainer()
        self.layout.addWidget(self.creator_container, 0, 1)



