from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.Core.Data import *


class BlockCreatorToolbar(QToolBar):

    def __init__(self):

        # Initial configuration
        QToolBar.__init__(self)
        self.setObjectName("block_creator_toolbar")
        self.setOrientation(Qt.Vertical)
        self.setIconSize(QSize(40, 40))

        #
        self.exit_act = QAction(QIcon("img/add_block.png"), "Add a new block", self)
        self.exit_act.setShortcut("Ctrl+B")
        self.addAction(self.exit_act)

