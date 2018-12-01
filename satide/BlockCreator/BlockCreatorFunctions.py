from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *
from satide.BlockCreator.Functions.LoopFunctions.LoopFunctions import ForBlock
from satide.BlockCreator.BlockCreatorView import BlockCreatorView


class BlockCreatorFunctions(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.setMaximumWidth(200)
        self.setMaximumWidth(200)
        self.layout = QGridLayout()
        self.setLayout(self.layout)


    def load(self):
        self.view = self.parent.view
        # Add Functions buttons
        self.for_button = QPushButton("For button")

        self.for_button.clicked.connect(partial(self.add_func, "for_block"))
        self.layout.addWidget(self.for_button)

    def add_func(self, object):

        if object == "for_block":
            for_block = ForBlock(self.parent.block_id)
            self.view.add_function(for_block)

