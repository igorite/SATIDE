from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
from satide.Blocks.Block import Block

from PyQt5.QtWidgets import *


class BlockContainer(QMdiArea):

    def __init__(self, parent):
        self.parent = parent
        self.blocks = []
        self.link_status = False
        self.link_status_id = None
        self.links = []
        self.links_id = 0
        self.id = 0
        self.cursor = QCursor()
        self.paint = 0
        self.distance = 70
        QMdiArea.__init__(self)
        self.resize(100, 100)

    def zoom_in(self):
        if self.distance < 100:
            self.distance += 10
        for block in self.blocks:
            block[1].block_resize()


    def zoom_out(self):
        if self.distance > 50:
            self.distance -= 10
        for block in self.blocks:
            block[1].block_resize()

    def paintEvent(self, event):
        QMdiArea.paintEvent(self, event)

        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(self.viewport())

        painter.fillRect(self.rect(), QColor(20, 36, 75))

        dash_pen = QPen(QColor(200, 200, 200), 1)
        dash_pen.setStyle(Qt.DashLine)
        dash_pen.setJoinStyle(Qt.RoundJoin)


        painter.setPen(dash_pen)

        i = 0
        while i * self.distance < self.height():
            painter.drawLine(20, 20 + i * self.distance, 20 + self.width(), 20 + i * self.distance)
            i += 1
        j = 0
        while j * self.distance < self.width():
            painter.drawLine(20 + j * self.distance, 20, 20 + j * self.distance, 20 + self.height())
            j += 1


        painter.setPen(QPen(QColor(5, 189, 57, 255), 6))
        for link in self.links:
            start = None
            end = None
            for block in self.blocks:
                if link[0] == block[0]:
                    start = block[1]
            for block in self.blocks:
                if link[1] == block[0]:
                    end = block[1]
            if start is not None and end is not None:

                start_point = QPoint(start.pos())
                end_point = QPoint(end.pos())
                start_x = np.round(start_point.x()+(start.width()/2), 0)
                end_x = np.round(end_point.x()+(end.width()/2), 0)

                line = (start_x, start_point.y()+start.height()-38, end_x, end_point.y()+18)

                painter.drawLine(line[0], line[1]+20, line[2], line[3])
            elif start is not None:
                self.cursor = QCursor()
                start_point = QPoint(start.pos())
                start_x = np.round(start_point.x() + (start.width() / 2), 0)
                cursor = self.cursor.pos()
                line = (start_x, start_point.y() + start.height()-38, cursor.x(), cursor.y())

                painter.drawLine(line[0], line[1] + 20, line[2], line[3])

        painter.end()
        self.resize(self.width(), self.height()+1)
        self.resize(self.width(), self.height()-1)

    def mouseMoveEvent(self, event):
        self.repaint()
        self.update()

    def create_link(self, block_id):

        if self.link_status is False:
            for link in self.links:
                if link[0] == block_id:
                    self.link_status = True
                    self.link_status_id = block_id
                    link[1] = None
                    return
            self.links.append([block_id, None])
            self.link_status = True
            self.link_status_id = block_id
            return
        if self.link_status is True:
            for link in self.links:
                if link[0] == self.link_status_id:
                    link[1] = block_id
            self.link_status_id = None
            self.link_status = False

    def create_link_down(self, block_id):
        if self.link_status is False:
            for link in self.links:
                if link[0] == block_id:
                    self.link_status = True
                    self.link_status_id = block_id
                    link[1] = None
                    return
            self.links.append([block_id, None])
            self.link_status = True
            self.link_status_id = block_id


    def create_link_up(self, block_id):

        if self.link_status is True:

            if self.link_status_id == block_id:
                return

            for link in self.links:
                if link[0] == self.link_status_id:
                    link[1] = block_id
            self.link_status_id = None
            self.link_status = False



    def mousePressEvent(self, event):
        if self.link_status is True:
            for link in self.links:
                if link[0] == self.link_status_id:
                    self.links.remove(link)
            self.link_status = False
            self.link_status_id = None

    def quit(self):
        self.quit()

    def create_block(self):
        b = Block(self, self.id)
        self.addSubWindow(b)
        b.block_resize()
        b.show()
        self.blocks.append([self.id, b])
        self.id += 1
