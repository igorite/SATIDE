from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *


class BlockCreatorFunctions(QFrame):

    def __init__(self):
        QFrame.__init__(self)
        self.setMaximumWidth(200)
        self.setMaximumWidth(200)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
