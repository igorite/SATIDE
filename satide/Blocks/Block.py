from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BlockFrame(QFrame):

    def __init__(self, parent, block_container, block_title=None):
        """

        :type parent: Block
        :type block_container: BlockContainer
        """
        self.parent = parent
        self.id = parent.id
        self.block_container = block_container
        self.distance = self.block_container.distance

        if block_title is None:
            self.block_title = str(self.id)
        else:
            self.block_title = block_title

        self.title_frame = None
        self.button = None
        self.connect_button = None
        self.options_button = None
        self.connect_button_down = None
        QFrame.__init__(self)
        self.body_frame = QFrame()
        self.body_frame.setObjectName("block_body")

        self.title_layout = QGridLayout()

        self.down_connector_frame = QFrame()
        self.down_connector_layout = QGridLayout()
        self.down_connector_layout.setContentsMargins(0, 0, 0, 0)
        self.down_connector_layout.setSpacing(0)
        self.down_connector_frame.setLayout(self.down_connector_layout)
        self.layout = QGridLayout()

        self.layout.setSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSizeConstraint(0)
        self.body_layout = QGridLayout()
        self.button2 = QPushButton("hello")
        self.set_title(self.block_title)
        self.setLayout(self.layout)
        self.layout.addWidget(self.body_frame, 0, 0)
        self.layout.addWidget(self.down_connector_frame, 1, 0)
        self.body_layout.addWidget(self.button2, 1, 0)
        self.body_frame.setLayout(self.body_layout)

        self.create_connectors()

    def set_title(self, title):
        self.title_frame = QFrame(self)
        self.title_frame.setObjectName("block_title")
        self.layout.setMenuBar(self.title_frame)
        self.title_frame.setLayout(self.title_layout)
        self.button = QPushButton(title)
        self.button.setMinimumHeight(20)
        self.button.setProperty("title", "True")
        self.button.setToolTip("Hello")
        self.body_layout.addWidget(self.button)

    def create_connectors(self):
        self.connect_button = QPushButton("")
        self.connect_button.setProperty("connect", "True")
        self.connect_button.setIcon(QIcon("img/connectorUP.png"))
        self.connect_button.setIconSize(QSize(30, 30))
        self.connect_button.clicked.connect(self.create_link_up)
        self.title_layout.addWidget(self.connect_button, 0, 1)
        self.title_layout.setSizeConstraint(0)
        self.title_layout.setContentsMargins(0, 0, 0, 0)

        self.options_button = QPushButton()
        self.options_button.setProperty("img", "True")
        self.options_button.setIcon(QIcon("img/settings.png"))
        self.options_button.setMinimumSize(20, 20)
        self.body_layout.addWidget(self.options_button, 0, 1)
        self.body_layout.setColumnStretch(0, 150)

        self.connect_button_down = QPushButton("")
        self.connect_button_down.setProperty("connect", "True")
        self.connect_button_down.setIcon(QIcon("img/connectorDOWN.png"))
        self.connect_button_down.setIconSize(QSize(30, 30))
        self.connect_button_down.clicked.connect(self.create_link_down)
        self.down_connector_layout.addWidget(self.connect_button_down)


    def create_link_up(self):
        self.block_container.create_link_up(self.id)

    def create_link_down(self):
        self.block_container.create_link_down(self.id)


class Block(QMdiSubWindow):

    def __init__(self, block_container, block_id):
        """

        :type block_container: BlockContainer
        """
        self.block_container = block_container
        self.id = block_id
        QMdiSubWindow.__init__(self)
        self.oldPos = self.pos()
        self.width()

        self.link = [0, 0, 0, 0]
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('Custom')

        self.setWidget(BlockFrame(self, self.block_container))
        self.resize(self.block_container.distance * 4, self.block_container.distance * 2)
        self.block_resize()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()


    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def block_resize(self):
        self.resize(self.block_container.distance * 4, self.block_container.distance * 2)
