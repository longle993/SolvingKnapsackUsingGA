# Form implementation generated from reading ui file 'UIKnapsack.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Items import Ui_Items
from result import Ui_Result
from Algorithm import Algorithm
quantity = 0
max_weight = 12 

class Ui_UIKnapsack(object):
    def __init__(self):
            self.autoGenerate = False
            self.listItems = []
            self.algorithm = None

    def setSelection(self):
        if(self.rdAuto.isChecked() == True or self.rdCustomize.isChecked() == True):
            if(self.rdAuto.isChecked() == True):
                self.autoGenerate = True
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
            self.addItems(quantity)
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
    def addItems(self, quantity):
        try:
                self.listItems.clear()
                if(self.autoGenerate == True):
                        #GenerateData
                        self.algorithm= algorithms = Algorithm(Algorithm.generateItem(quantity), Algorithm.generate_Value(quantity), Algorithm.generate_Weight(quantity), quantity)
                        
                        self.list_Items = algorithms.combine_Dictionary()
                        for item,data in self.list_Items.items():
                                # Tạo một instance của Ui_Item
                                newItem = Ui_Items()
                                # Tạo một widget để chứa giao diện từ Ui_Item
                                item_widget = QtWidgets.QWidget()
                                newItem.setupUi(item_widget)
                                # Tạo một item mới cho QListWidget và đặt widget tạo bởi Ui_Item làm nội dung của item
                                listWidgetItem = QtWidgets.QListWidgetItem()
                                listWidgetItem.setSizeHint(QtCore.QSize(534,113))  # Sử dụng sizeHint của widget
                                self.listItems.addItem(listWidgetItem)
                                self.listItems.setItemWidget(listWidgetItem, item_widget)
                                # Thiết lập giá trị cho các thành phần trong Ui_Item
                                # Ví dụ: Thiết lập giá trị cho SpinBox và TextEdit
                                item_widget.findChild(QtWidgets.QSpinBox, "spinWeight").setValue(data['weight'])  
                                item_widget.findChild(QtWidgets.QSpinBox, "spinValue").setValue(data['value'])   
                                item_widget.findChild(QtWidgets.QTextEdit, "textEdit").setPlainText(item)
                else:
                        for i in range(quantity):
                                # Tạo một instance của Ui_Item
                                newItem = Ui_Items()
                                # Tạo một widget để chứa giao diện từ Ui_Item
                                item_widget = QtWidgets.QWidget()
                                newItem.setupUi(item_widget)
                                # Tạo một item mới cho QListWidget và đặt widget tạo bởi Ui_Item làm nội dung của item
                                listWidgetItem = QtWidgets.QListWidgetItem()
                                listWidgetItem.setSizeHint(QtCore.QSize(200,70))  # Sử dụng sizeHint của widget
                                self.listItems.addItem(listWidgetItem)
                                self.listItems.setItemWidget(listWidgetItem, item_widget)
                                # Thiết lập giá trị cho các thành phần trong Ui_Item
                                # Ví dụ: Thiết lập giá trị cho SpinBox và TextEdit
                                item_widget.findChild(QtWidgets.QSpinBox, "spinWeight").setValue(1)  
                                item_widget.findChild(QtWidgets.QSpinBox, "spinValue").setValue(1)   
                                item_widget.findChild(QtWidgets.QTextEdit, "textEdit").setPlainText("Item Name")
        except Exception as e:
                print(e)  
    def solveProblem(self):
        self.groupBox.setVisible(True)
        try:  
                # Setup
                crossover_rate = 0.9
                mutation_rate = 0.1
                
                print("List Items:")
                print(self.list_Items)

                # Step 2: Tạo quần thể
                size_population = 20 
                populations = self.algorithm.create_population(size_population)
                print("\nCreate Populations:")
                print(populations)

                # Step 7: Lặp lại quá trình và chọn cá thể tốt nhất
                num_generations = 10 
                best_solution = None 

                for generation in range(num_generations):
                        fitness_score = self.algorithm.evaluate_Population(self.list_Items, populations, max_weight)
                        probabilities = self.algorithm.calculate_Probabilities(fitness_score)
                        selected_individuals = self.algorithm.roulette_wheel_selection(populations, probabilities)
                        offspring_population = self.algorithm.crossover_Population(selected_individuals, crossover_rate)
                        mutation_Populations = self.algorithm.mutate_Population(offspring_population, mutation_rate)
                        
                        # Kiểm tra nếu danh sách đột biến không rỗng trước khi chọn cá thể tốt nhất
                        if mutation_Populations:
                                best_individual = max(mutation_Populations, key=lambda x: self.algorithm.evaluate_Fitness(self.list_Items, x, max_weight))
                                
                                if best_solution is None or self.algorithm.evaluate_Fitness(self.list_Items, best_individual, max_weight) > self.algorithm.evaluate_Fitness(self.list_Items, best_solution, max_weight):
                                        best_solution = best_individual
                        else:
                                print("\nNo valid individuals after mutation.")

                        # Gán quần thể mới từ quần thể sau khi đột biến
                        populations = mutation_Populations

                # In ra cá thể tốt nhất cuối cùng
                print("\nBest Solution found:")
                self.algorithm.print_BestSolution(best_solution,self.list_Items,max_weight)
                result = self.algorithm.print_BestSolution(best_solution,self.list_Items,max_weight)
                
                item_info = result['ItemsSelected']
                for data in item_info:  # Lặp qua các giá trị trong từ điển
                        # Tạo một instance của Ui_Result
                        newResult = Ui_Result()
                        # Tạo một widget để chứa giao diện từ Ui_Result
                        result_widget = QtWidgets.QWidget()
                        newResult.setupUi(result_widget)
                        
                        # Các bước còn lại để thiết lập giá trị cho các QLabel
                        result_widget.findChild(QtWidgets.QLabel, "lblItemName").setText(data['Item'])
                        result_widget.findChild(QtWidgets.QLabel, "lblWeight").setText(str(data['Weight']))
                        result_widget.findChild(QtWidgets.QLabel, "lblValue").setText(str(data['Value']))

                        # Thêm widget vào QListWidget
                        listWidgetItem = QtWidgets.QListWidgetItem()
                        listWidgetItem.setSizeHint(QtCore.QSize(534, 113))
                        self.listResult.addItem(listWidgetItem)
                        self.listResult.setItemWidget(listWidgetItem, result_widget)
        
        except Exception as e:
                print(e)
    def completeProblem(self):
            self.groupBox.setVisible(False)                  
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
        self.btnNextStep4.clicked.connect(self.solveProblem)
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
        self.btnBackStep2.clicked.connect(self.backToStep2)
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
        self.listItems = QtWidgets.QListWidget(parent=self.grCreateItemsAuto)
        self.listItems.setGeometry(QtCore.QRect(30, 50, 561, 321))
        self.listItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.listItems.setObjectName("listItems")
        self.groupBox = QtWidgets.QGroupBox(parent=self.grCreateItemsAuto)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 621, 491))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.listResult = QtWidgets.QListWidget(parent=self.groupBox)
        self.listResult.setGeometry(QtCore.QRect(40, 40, 561, 321))
        self.listResult.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.listResult.setObjectName("listResult")
        self.btnFinish = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnFinish.setGeometry(QtCore.QRect(250, 410, 131, 51))
        self.btnFinish.clicked.connect(self.completeProblem)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnFinish.setFont(font)
        self.btnFinish.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnFinish.setStyleSheet("QPushButton#btnFinish {\n"
"border: 1px solid #FF6B81;\n"
"border-radius: 10px;\n"
"background: #FF6B81;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnFinish:hover {\n"
"    border: 1px solid #FF6B81; \n"
"    background: white;\n"
"    color: #FF6B81; \n"
"}\n"
"QPushButton#btnFinish:pressed {\n"
"    background: #FF6B81;\n"
"    color: white; \n"
"}")
        self.btnFinish.setDefault(False)
        self.btnFinish.setFlat(False)
        self.btnFinish.setObjectName("btnFinish")
        self.grNumberItems = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.grNumberItems.setGeometry(QtCore.QRect(150, 80, 551, 301))
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

        #hide groupbox
        self.grNumberItems.setVisible(False)
        self.grCreateItemsAuto.setVisible(False)
        self.groupBox.setVisible(False)
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
        self.groupBox.setTitle(_translate("UIKnapsack", "Step 4: Best Result"))
        self.btnFinish.setText(_translate("UIKnapsack", "Finish"))
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
