from unittest import TestCase
from PyQt5.QtTest import QTest
from satide.GUI.MainWindow import MainWindow


class TestMainWindow(TestCase):

    def setUp(self):
        self.window = MainWindow()


    def test_dimensions(self):
        assert self.window.width() == 800
        assert self.window.height() == 800



