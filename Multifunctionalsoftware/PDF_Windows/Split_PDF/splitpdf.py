# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitpdf.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SplitPDF_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font-family:\'微软雅黑 Light\';\n"
"font-size:18px;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:#03030C;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_split_pdf = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_split_pdf.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_split_pdf.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-radius:5px;")
        self.lineEdit_split_pdf.setPlaceholderText("")
        self.lineEdit_split_pdf.setObjectName("lineEdit_split_pdf")
        self.horizontalLayout_4.addWidget(self.lineEdit_split_pdf)
        self.pushButton_split_pdf = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_split_pdf.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_split_pdf.setStyleSheet("background:#00e3f8;\n"
"border:none;\n"
"border-radius:5px;")
        self.pushButton_split_pdf.setObjectName("pushButton_split_pdf")
        self.horizontalLayout_4.addWidget(self.pushButton_split_pdf)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_2.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_save_split_pdf = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_save_split_pdf.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_save_split_pdf.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-radius:5px;")
        self.lineEdit_save_split_pdf.setObjectName("lineEdit_save_split_pdf")
        self.horizontalLayout_3.addWidget(self.lineEdit_save_split_pdf)
        self.pushButton_save_split_pdf = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_save_split_pdf.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_save_split_pdf.setStyleSheet("background:#00e3f8;\n"
"border:none;\n"
"border-radius:5px;")
        self.pushButton_save_split_pdf.setObjectName("pushButton_save_split_pdf")
        self.horizontalLayout_3.addWidget(self.pushButton_save_split_pdf)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_3.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_split_page_range = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_split_page_range.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_split_page_range.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-radius:5px;")
        self.lineEdit_split_page_range.setObjectName("lineEdit_split_page_range")
        self.horizontalLayout_2.addWidget(self.lineEdit_split_page_range)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start_pdf_split = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_start_pdf_split.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_start_pdf_split.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_start_pdf_split.setStyleSheet("background:#F17470;\n"
"border:none;\n"
"border-radius:5px;")
        self.pushButton_start_pdf_split.setObjectName("pushButton_start_pdf_split")
        self.horizontalLayout.addWidget(self.pushButton_start_pdf_split)
        self.pushButton_quit = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_quit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_quit.setStyleSheet("background:#F17470;\n"
"border:none;\n"
"border-radius:5px;")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "选择待拆分的PDF文件"))
        self.pushButton_split_pdf.setText(_translate("MainWindow", "选择PDF文件"))
        self.label_2.setText(_translate("MainWindow", "选择保存的文件夹位置"))
        self.pushButton_save_split_pdf.setText(_translate("MainWindow", "选择文件夹"))
        self.label_3.setText(_translate("MainWindow", "拆分页范围"))
        self.lineEdit_split_page_range.setPlaceholderText(_translate("MainWindow", "输入形如1-5,4-10,8-13......"))
        self.pushButton_start_pdf_split.setText(_translate("MainWindow", "拆分PDF"))
        self.pushButton_quit.setText(_translate("MainWindow", "关闭"))
