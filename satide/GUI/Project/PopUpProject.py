from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from satide.GUI.PopUpWindow import PopUpWindow
import os


class PopUpProject(PopUpWindow):

    def __init__(self):
        PopUpWindow.__init__(self)

        self.setMinimumWidth(500)
        self.main_frame.setMinimumHeight(150)
        self.layout = QGridLayout()
        self.layout.setColumnStretch(2, 2)
        self.layout.setColumnStretch(1, 20)
        self.setLayout(self.layout)
        self.setTitle("Create Project")

        self.name_label = QLabel("Project name:")
        self.name = QLineEdit()
        self.layout.addWidget(self.name_label, 0, 0)
        self.layout.addWidget(self.name, 0, 1)


        self.path_label = QLabel("Path:")
        self.layout.addWidget(self.path_label, 1, 0)

        self.path = QLineEdit()
        self.layout.addWidget(self.path, 1, 1)

        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.search_path)
        self.layout.addWidget(self.browse_button, 1, 2)


        self.ok_button = QPushButton("Create")
        self.ok_button.clicked.connect(self.create_project)
        self.layout.addWidget(self.ok_button, 2, 2)

        self.file_explorer = QFileDialog()
        self.file_explorer.setFileMode(QFileDialog.Directory)


    def search_path(self):
        path = self.file_explorer.getExistingDirectory()
        self.path.setText(str(path))



    def create_project(self):

        path = self.path.text()
        if path == "":
            pass

        name = self.name.text()
        if name == "":
            pass

        directory = path + "/" + name

        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(directory+"/Functions")
            os.makedirs(directory+"/Test")

        data = [
            ["project_name", name],
            ["path", path]

        ]

        with open(directory + "/main.py", "w") as file:
            for element in data:
                file.write(element[0]+" = " + element[1]+"\n")
        self.close()
