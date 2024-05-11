from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import sys

class treeSettingUI(QMainWindow):
    def __init__(self):
        super(treeSettingUI, self).__init__()
        uic.loadUi('../doc/UIdocs/UI/treeSettingUI.ui', self)
        self.show()

class welcomeUI(QMainWindow):
    def __init__(self):
        super(welcomeUI, self).__init__()

        # carico la UI da un file .ui
        uic.loadUi('../doc/UIdocs/UI/mainUI.ui', self)
        
        # definisco i widget
        self.newTreeButton = self.findChild(QPushButton, 'newTreeButton')
        self.randomTreeButton = self.findChild(QPushButton, 'randomTreeButton')
        # collego i widget ai metodi
        self.newTreeButton.clicked.connect(self.gotoTreeSetting)

        # mostro la finestra
        self.show()

    def gotoTreeSetting(self):
            self.treeSetting = treeSettingUI()
            self.treeSetting.show()

def main():
    app = QApplication([])
    window = welcomeUI()
    app.exec_()


if __name__ == "__main__":
    main()
