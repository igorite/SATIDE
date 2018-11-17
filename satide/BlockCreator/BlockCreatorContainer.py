from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *
from satide.Blocks.Block import BaseBlock, BaseVariable


class BlockCreatorContainer(QFrame):

    def __init__(self):

        QFrame.__init__(self)
        self.setObjectName("block_creator")
