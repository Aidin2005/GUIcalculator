from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 401)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.top_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_frame.setObjectName("top_frame")
        self.answer_box = QtWidgets.QLineEdit(parent=self.top_frame)
        self.answer_box.setGeometry(QtCore.QRect(0, 20, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_box.setFont(font)
        self.answer_box.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.answer_box.setText("")
        self.answer_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.answer_box.setObjectName("answer_box")
        self.gridLayout_2.addWidget(self.top_frame, 0, 0, 1, 1)
        self.bottom_frame = QtWidgets.QFrame(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bottom_frame.setFont(font)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.bottom_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_6 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(14, 123, 26);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 4, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 4, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.bottom_frame)
        self.btn_clear.setStyleSheet("background-color: rgb(255, 11, 150);\n"
"color: rgb(255, 255, 255);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 2, 1, 2)
        self.btn_8 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_all_clear = QtWidgets.QPushButton(parent=self.bottom_frame)
        self.btn_all_clear.setStyleSheet("background-color: rgb(195, 9, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_all_clear.setObjectName("btn_all_clear")
        self.gridLayout.addWidget(self.btn_all_clear, 0, 0, 1, 2)
        self.btn_minus = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_mul.setFont(font)
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.bottom_frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #conection
        self.btn_1.clicked.connect(lambda : self.pressed(1))
        self.btn_2.clicked.connect(lambda: self.pressed(2))
        self.btn_3.clicked.connect(lambda: self.pressed(3))
        self.btn_4.clicked.connect(lambda: self.pressed(4))
        self.btn_5.clicked.connect(lambda: self.pressed(5))
        self.btn_6.clicked.connect(lambda: self.pressed(6))
        self.btn_7.clicked.connect(lambda: self.pressed(7))
        self.btn_8.clicked.connect(lambda: self.pressed(8))
        self.btn_9.clicked.connect(lambda: self.pressed(9))
        self.btn_0.clicked.connect(lambda: self.pressed(0))
        self.btn_plus.clicked.connect(lambda: self.pressed('+'))
        self.btn_minus.clicked.connect(lambda: self.pressed('-'))
        self.btn_mul.clicked.connect(lambda: self.pressed('*'))
        self.pushButton_3.clicked.connect(lambda: self.pressed('/'))
        self.btn_dot.clicked.connect(lambda: self.pressed('.'))

        self.btn_equal.clicked.connect(self.equal)

        self.btn_all_clear.clicked.connect(self.all_clear)

        self.btn_clear.clicked.connect(self.clear)


    def  pressed(self,number):
        self.answer_box.insert(str(number))


    def equal(self):
        content = self.answer_box.text().strip()
        answer = eval(content)
        self.answer_box.setText(str(answer))

    def all_clear(self):
        self.answer_box.clear()

    def clear(self):
        content = self.answer_box.text().strip()
        self.answer_box.setText(content[:-1])



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_clear.setText(_translate("MainWindow", "Del"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_all_clear.setText(_translate("MainWindow", "AC"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_5.setText(_translate("MainWindow", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
