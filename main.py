import sys
from PyQt5.QtWidgets import *
from gui import MainWindow

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())