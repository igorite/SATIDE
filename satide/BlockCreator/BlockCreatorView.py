from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *


class BlockCreatorView(QFrame):

    def __init__(self, parent):
        self.parent = parent
        self.rows = 0
        QFrame.__init__(self)
        self.layout = QGridLayout()
        self.layout.setRowStretch(0, 10)
        self.layout.setColumnStretch(0, 2)
        self.layout.setColumnStretch(2, 10)
        self.layout.setColumnStretch(3, 10)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)

    def load(self):
        pass

    def add_function(self, function_object):
        self.parent.blocks.append([self.parent.block_id, function_object])
        self.add_row()
        self.layout.addWidget(function_object, self.rows-1, 2)
        self.parent.block_id += 1
        print(self.parent.blocks)


    def add_row(self):
        self.rows += 1
        number = QLabel(str(self.rows))
        number.setObjectName("row_number")
        self.layout.addWidget(number, self.rows-1, 1)


