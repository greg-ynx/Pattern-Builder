import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class PatternGrid:

    def __init__(self, column: int, row: int):
        self.column_count = column
        self.row_count = row
