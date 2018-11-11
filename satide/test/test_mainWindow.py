from unittest import TestCase
from PyQt5.Qt import *
from PyQt5.QtTest import QTest
from satide.GUI.MainWindow import MainWindow


class TestMainWindow(TestCase):

    def setUp(self):
        self.window = MainWindow()

    def test_start(self):
        assert self.window.width() == 800
        assert self.window.height() == 800
        assert self.window.app.applicationName() == "SATIDE"
        assert self.window.centralWidget().objectName() == "central_frame"
        QTest.mouseClick(self.window.steps_button, Qt.LeftButton)

