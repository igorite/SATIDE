from satide.GUI.MainWindow import MainWindow
import os

dir_name = os.path.dirname(__file__)

window = MainWindow(dir_name)
window.app.exec_()
