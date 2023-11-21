# Form implementation generated from reading ui file 'UIKnapsack.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

autoGenerate = False
quantity = 0
class Ui_UIKnapsack(object):
    def setSelection(self):
        if(self.rdAuto.isChecked() == True or self.rdCustomize.isChecked() == True):
            if(self.rdAuto.isChecked() == True):
                autoGenerate = True
                self.grNumberItems.setVisible(True)
                self.grSelection.setVisible(False)
        else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg_box.setText("You must Choose Auto Generate or Customize!")
                msg_box.setWindowTitle("Notice")
                msg_box.exec()
    def setQuantity(self):
        quantity = self.spinQuantity.value()
        if(quantity > 0):
            self.grNumberItems.setVisible(False)
            self.grCreateItemsAuto.setVisible(True)
        else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg_box.setText("Your Quantity must be greater than 0")
                msg_box.setWindowTitle("Notice")
                msg_box.exec()
    def backToStep1(self):
         self.grNumberItems.setVisible(False)
         self.grSelection.setVisible(True)
    def backToStep2(self):
        self.grNumberItems.setVisible(True)
        self.grCreateItemsAuto.setVisible(False)
    def setupUi(self, UIKnapsack):
        UIKnapsack.setObjectName("UIKnapsack")
        UIKnapsack.resize(849, 610)
        UIKnapsack.setStyleSheet("background: white")
        self.centralwidget = QtWidgets.QWidget(parent=UIKnapsack)
        self.centralwidget.setObjectName("centralwidget")
        self.grSelection = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grSelection.setGeometry(QtCore.QRect(160, 100, 531, 271))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grSelection.setFont(font)
        self.grSelection.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.grSelection.setAutoFillBackground(False)
        self.grSelection.setStyleSheet("QGroupBox#grSelection {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    background: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.grSelection.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.grSelection.setFlat(False)
        self.grSelection.setObjectName("grSelection")
        self.rdAuto = QtWidgets.QRadioButton(parent=self.grSelection)
        self.rdAuto.setGeometry(QtCore.QRect(140, 60, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rdAuto.setFont(font)
        self.rdAuto.setStatusTip("")
        self.rdAuto.setObjectName("rdAuto")
        self.rdCustomize = QtWidgets.QRadioButton(parent=self.grSelection)
        self.rdCustomize.setEnabled(True)
        self.rdCustomize.setGeometry(QtCore.QRect(140, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rdCustomize.setFont(font)
        self.rdCustomize.setMouseTracking(True)
        self.rdCustomize.setIconSize(QtCore.QSize(17, 17))
        self.rdCustomize.setObjectName("rdCustomize")
        self.btnNextStep2 = QtWidgets.QPushButton(parent=self.grSelection)
        self.btnNextStep2.setGeometry(QtCore.QRect(190, 180, 131, 51))
        self.btnNextStep2.clicked.connect(self.setSelection)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnNextStep2.setFont(font)
        self.btnNextStep2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnNextStep2.setStyleSheet("QPushButton#btnNextStep2 {\n"
"border: 1px solid #FF6B81;\n"
"border-radius: 10px;\n"
"background: #FF6B81;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNextStep2:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: white;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnNextStep2:pressed {\n"
"    background: #FF6B81;\n"
"    color: white; \n"
"}")
        self.btnNextStep2.setDefault(False)
        self.btnNextStep2.setFlat(False)
        self.btnNextStep2.setObjectName("btnNextStep2")
        self.grCreateItemsAuto = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grCreateItemsAuto.setGeometry(QtCore.QRect(120, 30, 621, 491))
        self.grCreateItemsAuto.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grCreateItemsAuto.setFont(font)
        self.grCreateItemsAuto.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.grCreateItemsAuto.setAutoFillBackground(False)
        self.grCreateItemsAuto.setStyleSheet("")
        self.grCreateItemsAuto.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.grCreateItemsAuto.setFlat(False)
        self.grCreateItemsAuto.setObjectName("grCreateItemsAuto")
        self.btnNextStep4 = QtWidgets.QPushButton(parent=self.grCreateItemsAuto)
        self.btnNextStep4.setGeometry(QtCore.QRect(330, 410, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnNextStep4.setFont(font)
        self.btnNextStep4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnNextStep4.setStyleSheet("QPushButton#btnNextStep4 {\n"
"border: 1px solid #FF6B81;\n"
"border-radius: 10px;\n"
"background: #FF6B81;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNextStep4:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: white;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnNextStep4:pressed {\n"
"    background: #FF6B81;\n"
"    color: white; \n"
"}")
        self.btnNextStep4.setDefault(False)
        self.btnNextStep4.setFlat(False)
        self.btnNextStep4.setObjectName("btnNextStep4")
        self.btnBackStep2 = QtWidgets.QPushButton(parent=self.grCreateItemsAuto)
        self.btnBackStep2.setGeometry(QtCore.QRect(170, 410, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBackStep2.setFont(font)
        self.btnBackStep2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBackStep2.setStyleSheet("QPushButton#btnBackStep2 {\n"
"border: 1px solid #D9D9D9;\n"
"border-radius: 10px;\n"
"background: #D9D9D9;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnBackStep2:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: black;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnBackStep2:pressed {\n"
"    background: #FF6B81;\n"
"    color: black; \n"
"}")
        self.btnBackStep2.setDefault(False)
        self.btnBackStep2.setFlat(False)
        self.btnBackStep2.setObjectName("btnBackStep2")
        self.btnBackStep2.clicked.connect(self.backToStep2)
        self.listItem = QtWidgets.QListView(parent=self.grCreateItemsAuto)
        self.listItem.setGeometry(QtCore.QRect(60, 50, 511, 331))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listItem.setFont(font)
        self.listItem.setObjectName("listItem")
        self.grNumberItems = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grNumberItems.setGeometry(QtCore.QRect(150, 80, 551, 301))
        self.grNumberItems.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grNumberItems.setFont(font)
        self.grNumberItems.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.grNumberItems.setAutoFillBackground(False)
        self.grNumberItems.setStyleSheet("QGroupBox#grNumberItems {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    background: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.grNumberItems.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.grNumberItems.setFlat(False)
        self.grNumberItems.setObjectName("grNumberItems")
        self.btnNextStep3 = QtWidgets.QPushButton(parent=self.grNumberItems)
        self.btnNextStep3.setGeometry(QtCore.QRect(280, 190, 131, 51))
        self.btnNextStep3.clicked.connect(self.setQuantity)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnNextStep3.setFont(font)
        self.btnNextStep3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnNextStep3.setStyleSheet("QPushButton#btnNextStep3 {\n"
"border: 1px solid #FF6B81;\n"
"border-radius: 10px;\n"
"background: #FF6B81;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnNextStep3:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: white;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnNextStep3:pressed {\n"
"    background: #FF6B81;\n"
"    color: white; \n"
"}")
        self.btnNextStep3.setDefault(False)
        self.btnNextStep3.setFlat(False)
        self.btnNextStep3.setObjectName("btnNextStep3")
        self.btnBackStep1 = QtWidgets.QPushButton(parent=self.grNumberItems)
        self.btnBackStep1.setGeometry(QtCore.QRect(120, 190, 131, 51))
        self.btnBackStep1.clicked.connect(self.backToStep1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBackStep1.setFont(font)
        self.btnBackStep1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBackStep1.setStyleSheet("QPushButton#btnBackStep1 {\n"
"border: 1px solid #D9D9D9;\n"
"border-radius: 10px;\n"
"background: #D9D9D9;\n"
"color: black;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnBackStep1:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: black;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnBackStep1:pressed {\n"
"    background: #FF6B81;\n"
"    color: black; \n"
"}")
        self.btnBackStep1.setDefault(False)
        self.btnBackStep1.setFlat(False)
        self.btnBackStep1.setObjectName("btnBackStep1")
        self.spinQuantity = QtWidgets.QSpinBox(parent=self.grNumberItems)
        self.spinQuantity.setGeometry(QtCore.QRect(190, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.spinQuantity.setFont(font)
        self.spinQuantity.setObjectName("spinQuantity")
        self.grNumberItems.raise_()
        self.grSelection.raise_()
        self.grCreateItemsAuto.raise_()
        UIKnapsack.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=UIKnapsack)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 26))
        self.menubar.setObjectName("menubar")
        UIKnapsack.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=UIKnapsack)
        self.statusbar.setObjectName("statusbar")
        UIKnapsack.setStatusBar(self.statusbar)

        self.retranslateUi(UIKnapsack)
        QtCore.QMetaObject.connectSlotsByName(UIKnapsack)

    def retranslateUi(self, UIKnapsack):
        _translate = QtCore.QCoreApplication.translate
        UIKnapsack.setWindowTitle(_translate("UIKnapsack", "Knapsack using Genetic Algorithm"))
        self.grSelection.setTitle(_translate("UIKnapsack", "Step 1: Choose your expression"))
        self.rdAuto.setText(_translate("UIKnapsack", "Auto Generate Items"))
        self.rdCustomize.setText(_translate("UIKnapsack", "Customize Items"))
        self.btnNextStep2.setText(_translate("UIKnapsack", "Next"))
        self.grCreateItemsAuto.setTitle(_translate("UIKnapsack", "Step 3: Create Items"))
        self.btnNextStep4.setText(_translate("UIKnapsack", "Next"))
        self.btnBackStep2.setText(_translate("UIKnapsack", "Back"))
        self.grNumberItems.setTitle(_translate("UIKnapsack", "Step 2: Enter the item quantity"))
        self.btnNextStep3.setText(_translate("UIKnapsack", "Next"))
        self.btnBackStep1.setText(_translate("UIKnapsack", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIKnapsack = QtWidgets.QMainWindow()
    ui = Ui_UIKnapsack()
    ui.setupUi(UIKnapsack)
    UIKnapsack.show()
    sys.exit(app.exec())