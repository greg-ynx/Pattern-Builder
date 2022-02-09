# -*- coding: utf-8 -*-

# This program was meant to return a matrix from your chosen custom pattern

from PyQt5 import QtCore, QtGui, QtWidgets
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        
##############################################################################
#PAGE 1
       
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        
        # message "Set your matrix size"
        self.sizeMessageLabel = QtWidgets.QLabel(self.page_1)
        self.sizeMessageLabel.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sizeMessageLabel.setFont(font)
        self.sizeMessageLabel.setObjectName("sizeMessageLabel")
        
        # spin box for the x size of the matrix
        self.spinBox_x = QtWidgets.QSpinBox(self.page_1)
        self.spinBox_x.setGeometry(QtCore.QRect(90, 180, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_x.setFont(font)
        self.spinBox_x.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_x.setMaximum(40)
        self.spinBox_x.setProperty("value", 0)
        self.spinBox_x.setObjectName("spinBox_x")
        
        # label for x spin box
        self.widthLabel = QtWidgets.QLabel(self.page_1)
        self.widthLabel.setGeometry(QtCore.QRect(100, 240, 91, 31))
        self.widthLabel.setObjectName("widthLabel")  
        
        # spin box for the y size of the matrix
        self.spinBox_y = QtWidgets.QSpinBox(self.page_1)
        self.spinBox_y.setGeometry(QtCore.QRect(250, 180, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_y.setFont(font)
        self.spinBox_y.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_y.setMaximum(40)
        self.spinBox_y.setProperty("value", 0)
        self.spinBox_y.setObjectName("spinBox_y")
        
        # label for y spin box
        self.heightLabel = QtWidgets.QLabel(self.page_1)
        self.heightLabel.setGeometry(QtCore.QRect(270, 240, 91, 31))
        self.heightLabel.setObjectName("heightLabel")
        
        # line on the first page
        self.lineSizePage = QtWidgets.QFrame(self.page_1)
        self.lineSizePage.setGeometry(QtCore.QRect(10, 540, 441, 20))
        self.lineSizePage.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSizePage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSizePage.setObjectName("lineSizePage")
        
        # horizontal layout for the ok button
        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(self.page_1)
        self.horizontalLayoutWidget_1.setGeometry(QtCore.QRect(350, 560, 101, 51))
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        
        self.hLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_1)
        self.hLayout_1.setContentsMargins(0, 0, 0, 0)
        self.hLayout_1.setObjectName("hLayout_1")
        
        # creating the ok button
        self.okButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_1)
        self.okButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton_1.setDefault(True)
        self.okButton_1.setObjectName("okButton_1")

        
        self.hLayout_1.addWidget(self.okButton_1)
        
        # label in between the spin box 
        self.xLabel = QtWidgets.QLabel(self.page_1)
        self.xLabel.setGeometry(QtCore.QRect(210, 180, 31, 51))
        self.xLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.xLabel.setFont(font)
        self.xLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.xLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xLabel.setObjectName("xLabel")
        
        self.stackedWidget.addWidget(self.page_1)
        
##############################################################################

#PAGE 2
        
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        
        # travel to second page
        self.okButton_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        
        
        # message "Set your matrix pattern :"
        self.patternMessageLabel = QtWidgets.QLabel(self.page_2)
        self.patternMessageLabel.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.patternMessageLabel.setFont(font)
        self.patternMessageLabel.setObjectName("patternMessageLabel")

            
    
        # grid layout for the matrix button
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-40, 0, 550, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(75, 75, 75, 75)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        
        # ok button for matrix function
        self.okButton_1.clicked.connect(self.matrix)
        
        
        # horizontal layout for back and ok buttons
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(240, 560, 211, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        
        self.hLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hLayout_2.setObjectName("hLayout_2")
        
        # creating and setting back button
        self.backButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.backButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton_2.setAutoDefault(False)
        self.backButton_2.setDefault(False)
        self.backButton_2.setFlat(False)
        self.backButton_2.setObjectName("backButton_2")
        self.hLayout_2.addWidget(self.backButton_2)
        self.backButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.backButton_2.clicked.connect(self.deleteGrid)
        
        # creating and setting final ok button
        self.okButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.okButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton_2.setDefault(True)
        self.okButton_2.setObjectName("okButton_2")
        self.okButton_2.clicked.connect(self.finalMatrix)
        self.hLayout_2.addWidget(self.okButton_2)
        
        
        # line on the second page
        self.linePatternPage = QtWidgets.QFrame(self.page_2)
        self.linePatternPage.setGeometry(QtCore.QRect(10, 540, 441, 20))
        self.linePatternPage.setFrameShape(QtWidgets.QFrame.HLine)
        self.linePatternPage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linePatternPage.setObjectName("linePatternPage")
        
        self.stackedWidget.addWidget(self.page_2)
    
##############################################################################         
    
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def matrix(self):
        """
        Generate a matrix

        """
        print("Matrix loading...")
        x = self.spinBox_x.value()
        y = self.spinBox_y.value()
        for i in range(int(x)):
            for j in range(int(y)):
                self.button = QtWidgets.QPushButton(self.gridLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
                self.button.setSizePolicy(sizePolicy)
                self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.button.setObjectName("button")
                self.button.setText("0")
                self.button.setStyleSheet("background-color : red")
                self.button.clicked.connect(self.clicked)
                self.button.setObjectName("button{}{}".format(i, j))
                self.gridLayout.addWidget(self.button, i, j)
                
                
    def deleteGrid(self):
        """
        Delete the matrix grid

        """
        x = self.spinBox_x.value()
        y = self.spinBox_y.value()
        for i in range(int(x)):
            for j in range(int(y)):
                removeButton = MainWindow.findChild(QtWidgets.QPushButton, "button{}{}".format(i, j))
                removeButton.deleteLater()


    def clicked(QMainWindow):
        """
        Change button color and ID when pressed

        Returns
        -------
        bool
            True when button is red and turned to blue.
            False when button is blue and turned to red.

        """
        button = MainWindow.sender()
        namebp = button.objectName()
        print("{} pressed".format(namebp))
        if button.text()=="0":
            button.setText("1")
            button.setStyleSheet("background-color : blue")
            return True
        else :
            button.setText("0")
            button.setStyleSheet("background-color : red")
            return False
        
        
    def finalMatrix(self):
        """
        Matrix returned to python console

        Returns
        -------
        matrix : list of list (array)

        """
        matrix = []
        line = []
        x = self.spinBox_x.value()
        y = self.spinBox_y.value()
        for i in range(x):
            matrix.append([])
            line = []
            for j in range(int(y)):
                button = MainWindow.findChild(QtWidgets.QPushButton, "button{}{}".format(i, j))
                line.append(int(button.text()))
            matrix[i] = line
        print(matrix)
        return matrix
        
    
    # method naming the elements
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pattern Builder"))
        self.sizeMessageLabel.setText(_translate("MainWindow", "Set your matrix size :"))
        self.widthLabel.setText(_translate("MainWindow", "Size x (horizontal)"))
        self.heightLabel.setText(_translate("MainWindow", "Size y (vertical)"))
        self.okButton_1.setText(_translate("MainWindow", "Ok"))
        self.xLabel.setText(_translate("MainWindow", "X"))
        self.patternMessageLabel.setText(_translate("MainWindow", "Set your matrix pattern :"))
        self.backButton_2.setText(_translate("MainWindow", "Back"))
        self.okButton_2.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
