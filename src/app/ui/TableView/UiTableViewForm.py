# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_widget_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# Some modifications made to this generated class by lyl-Lynx.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from src.app.exceptions.CustomException import IdNotFound, ProtectedRowError, TableMaxItemError


class UiTableViewForm(object):

    def __init__(self, table_view_form):

        table_view_form.setObjectName("table_view_form")
        table_view_form.setWindowModality(QtCore.Qt.WindowModal)
        table_view_form.resize(600, 800)
        table_view_form.setMinimumSize(QtCore.QSize(512, 512))
        table_view_form.setBaseSize(QtCore.QSize(600, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../assets/img/pattern_builder_icon.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        table_view_form.setWindowIcon(icon)
        self.table_view_form = table_view_form

        self.selected_row: int = 0
        self.selected_item: dict = {}

        self.verticalLayout = QtWidgets.QVBoxLayout(table_view_form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.actions_widget = QtWidgets.QWidget(table_view_form)
        self.actions_widget.setObjectName("actions_widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.actions_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.actions_label = QtWidgets.QLabel(self.actions_widget)
        self.actions_label.setObjectName("actions_label")
        self.horizontalLayout.addWidget(self.actions_label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.actions_reset_button = QtWidgets.QPushButton(self.actions_widget)
        self.actions_reset_button.setObjectName("actions_reset_button")
        self.actions_reset_button.clicked.connect(self.reset)
        self.horizontalLayout.addWidget(self.actions_reset_button)

        self.actions_add_button = QtWidgets.QPushButton(self.actions_widget)
        self.actions_add_button.setObjectName("actions_add_button")
        self.actions_add_button.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.actions_add_button)

        self.actions_delete_button = QtWidgets.QPushButton(self.actions_widget)
        self.actions_delete_button.setObjectName("actions_delete_button")
        self.actions_delete_button.clicked.connect(self.delete)
        self.horizontalLayout.addWidget(self.actions_delete_button)

        self.verticalLayout.addWidget(self.actions_widget)

        self.table_widget_scroll_area = QtWidgets.QScrollArea(table_view_form)
        self.table_widget_scroll_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.table_widget_scroll_area.setWidgetResizable(True)
        self.table_widget_scroll_area.setObjectName("table_widget_scroll_area")

        self.table_widget_scroll_area_contents = QtWidgets.QWidget()
        self.table_widget_scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 578, 684))
        self.table_widget_scroll_area_contents.setObjectName("table_widget_scroll_area_contents")

        self.gridLayout = QtWidgets.QGridLayout(self.table_widget_scroll_area_contents)
        self.gridLayout.setObjectName("gridLayout")

        self.table_widget = QtWidgets.QTableWidget(self.table_widget_scroll_area_contents)
        self.table_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(2)

        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.table_widget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setItem(1, 2, item)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.verticalHeader().setStretchLastSection(False)
        self.table_widget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table_widget.clicked.connect(self.select_item)
        self.gridLayout.addWidget(self.table_widget, 0, 0, 1, 1)

        self.table_widget_scroll_area.setWidget(self.table_widget_scroll_area_contents)
        self.verticalLayout.addWidget(self.table_widget_scroll_area)

        self.close_widget = QtWidgets.QWidget(table_view_form)
        self.close_widget.setObjectName("close_widget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.close_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.close_button = QtWidgets.QPushButton(self.close_widget)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)

        self.verticalLayout.addWidget(self.close_widget)

        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.retranslateUi(table_view_form)
        QtCore.QMetaObject.connectSlotsByName(table_view_form)
        print(self.get_all())
        print(self.getById(0))

    def get_row_count(self):
        return self.table_widget.rowCount()

    def get_all(self):
        rep = list()
        for row in range(self.table_widget.rowCount()):
            rep.append({
                'id': int(self.table_widget.item(row, 0).text()),
                'Hex': self.table_widget.item(row, 1).text(),
                'RGB': self.table_widget.item(row, 2).text()
            })
        return rep

    def getById(self, row_id: int):
        items = self.get_all()
        try:
            for _ in items:
                if row_id == items[row_id]['id']:
                    return items[row_id]
            raise IdNotFound
        except IdNotFound:
            print("No color found linked to this id -> " + str(row_id))

    def select_item(self):
        self.selected_row = self.table_widget.currentRow()
        self.selected_item = self.getById(self.selected_row)
        print(self.selected_row)
        print(self.selected_item)

    def reset(self):
        self.table_widget.setRowCount(2)

    def add(self):
        count = self.get_row_count()
        try:
            if count < 64:
                color = QtWidgets.QColorDialog.getColor()
                print(color.name())
                print(color.name().upper())
                print((color.red(), color.green(), color.blue()))
                self.table_widget.insertRow(count)
                n_count = self.table_widget.rowCount()-1
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(n_count))
                self.table_widget.setItem(n_count, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(color.name().upper()))
                self.table_widget.setItem(n_count, 1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str((color.red(), color.green(), color.blue())))
                self.table_widget.setItem(n_count, 2, item)
                print(self.getById(n_count))
            else:
                raise TableMaxItemError
        except TableMaxItemError:
            print("Max items amount (64 colors) already reach in table!")

    def delete(self):
        try:
            if self.selected_row != 1 and self.selected_row != 0:
                self.table_widget.removeRow(self.selected_row)
                items = self.get_all()
                for i in range(len(items)):
                    if items[i]['id'] != i:
                        item = QtWidgets.QTableWidgetItem()
                        item.setText(str(i))
                        self.table_widget.setItem(i, 0, item)
            else:
                raise ProtectedRowError
            print("Row deleted with success!")
        except ProtectedRowError:
            print("Row {} is protected, you can only delete custom added rows.".format(self.selected_row))

    def retranslateUi(self, table_view_form):

        _translate = QtCore.QCoreApplication.translate
        table_view_form.setWindowTitle(_translate("table_view_form", "Pattern builder - Table view"))
        self.actions_label.setText(_translate("table_view_form", "Actions:"))
        self.actions_reset_button.setText(_translate("table_view_form", "Reset"))
        self.actions_add_button.setText(_translate("table_view_form", "Add"))
        self.actions_delete_button.setText(_translate("table_view_form", "Delete"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("table_view_form", "Id"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("table_view_form", "Hexa code"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("table_view_form", "RGB code"))
        __sortingEnabled = self.table_widget.isSortingEnabled()
        self.table_widget.setSortingEnabled(False)
        item = self.table_widget.item(0, 0)
        item.setText(_translate("table_view_form", "0"))
        item = self.table_widget.item(0, 1)
        item.setText(_translate("table_view_form", "#FF0000"))
        item = self.table_widget.item(0, 2)
        item.setText(_translate("table_view_form", "(255,0,0)"))
        item = self.table_widget.item(1, 0)
        item.setText(_translate("table_view_form", "1"))
        item = self.table_widget.item(1, 1)
        item.setText(_translate("table_view_form", "#0000FF"))
        item = self.table_widget.item(1, 2)
        item.setText(_translate("table_view_form", "(0,0,255)"))
        self.table_widget.setSortingEnabled(__sortingEnabled)
        self.close_button.setText(_translate("table_view_form", "Close"))


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
ui = UiTableViewForm(widget)
widget.show()
sys.exit(app.exec_())
