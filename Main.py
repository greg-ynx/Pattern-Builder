# This script is the main function of this application.
import sys

from PyQt5 import QtWidgets
from src.app.ui.MainWindow.UiMainWindow import UiMainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = UiMainWindow(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
