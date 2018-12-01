import os
from PyQt5.QtGui import *


def load_icon(img):
    path = os.path.dirname(__file__)
    image = QIcon(os.path.join(path, img +".png"))
    print(str(path))
    return image
