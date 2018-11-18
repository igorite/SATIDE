from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *


class BlockCreatorView(QFrame):

    def __init__(self, parent):
        self.parent = parent
        QFrame.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def load(self):
        pass


    def add_function(self, function_object):
        self.layout.addWidget(function_object, 0, 0)
