import os
import sys
import traceback

from PyQt5 import QtCore

from satide.GUI.MainWindow import MainWindow

dir_name = os.path.dirname(__file__)


def excepthook(type_, value, traceback_):
    traceback.print_exception(type_, value, traceback_)
    QtCore.qFatal('')


sys.excepthook = excepthook


window = MainWindow(dir_name)
window.app.exec_()
