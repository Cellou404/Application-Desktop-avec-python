# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajouter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    title = "ajouter"
    inconName = "images/add-user.png"

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 378)
        Dialog.setMinimumSize(QtCore.QSize(705, 378))
        Dialog.setMaximumSize(QtCore.QSize(705, 378))
        Dialog.setStyleSheet("background-color: rgb(216, 255, 247);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 721, 71))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.inconName))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 96, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 0, 111, 71))
        self.frame_2.setStyleSheet("image: url(Images/add-user.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 130, 298, 128))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(88, 23))
        self.label_2.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_prenom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_prenom.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_prenom.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_prenom.setFont(font)
        self.lineEdit_prenom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_prenom.setPlaceholderText("")
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.horizontalLayout.addWidget(self.lineEdit_prenom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(88, 23))
        self.label_3.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_nom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_nom.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_nom.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nom.setFont(font)
        self.lineEdit_nom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nom.setPlaceholderText("")
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.horizontalLayout_2.addWidget(self.lineEdit_nom)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(88, 23))
        self.label_4.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_age = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_age.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_age.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_age.setPlaceholderText("")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.horizontalLayout_3.addWidget(self.lineEdit_age)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(88, 23))
        self.label_5.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_tel.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_tel.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_tel.setFont(font)
        self.lineEdit_tel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tel.setPlaceholderText("")
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.horizontalLayout_4.addWidget(self.lineEdit_tel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(0, 330, 711, 51))
        self.frame_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(560, 20, 103, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(370, 132, 298, 130))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(88, 23))
        self.label_6.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_date = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_date.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_date.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_date.setPlaceholderText("")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout_5.addWidget(self.lineEdit_date)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(88, 23))
        self.label_7.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_somme_A = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_somme_A.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_somme_A.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_somme_A.setFont(font)
        self.lineEdit_somme_A.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_somme_A.setPlaceholderText("")
        self.lineEdit_somme_A.setObjectName("lineEdit_somme_A")
        self.horizontalLayout_6.addWidget(self.lineEdit_somme_A)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(88, 23))
        self.label_8.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_somme_B = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_somme_B.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_somme_B.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_somme_B.setFont(font)
        self.lineEdit_somme_B.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_somme_B.setPlaceholderText("")
        self.lineEdit_somme_B.setObjectName("lineEdit_somme_B")
        self.horizontalLayout_7.addWidget(self.lineEdit_somme_B)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_effacer = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_effacer.setFont(font)
        self.pushButton_effacer.setToolTip("")
        self.pushButton_effacer.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"selection-background-color: rgb(170, 255, 255);\n"
"selection-color: rgb(170, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_effacer.setObjectName("pushButton_effacer")
        self.horizontalLayout_9.addWidget(self.pushButton_effacer)
        self.pushButton_enregistrer = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_enregistrer.setFont(font)
        self.pushButton_enregistrer.setToolTip("")
        self.pushButton_enregistrer.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"selection-color: rgb(170, 255, 255);\n"
"selection-color: rgb(0, 170, 0);\n"
"color: rgb(0, 255, 0);")
        self.pushButton_enregistrer.setObjectName("pushButton_enregistrer")
        self.horizontalLayout_9.addWidget(self.pushButton_enregistrer)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_effacer.clicked.connect(self.lineEdit_somme_B.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_somme_A.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_date.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_tel.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_age.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_nom.clear)
        self.pushButton_effacer.clicked.connect(self.lineEdit_prenom.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "AJOUTER"))
        self.label_2.setText(_translate("Dialog", "Prénom"))
        self.label_3.setText(_translate("Dialog", "Nom"))
        self.label_4.setText(_translate("Dialog", "Âge"))
        self.label_5.setText(_translate("Dialog", "Téléphone"))
        self.label_10.setText(_translate("Dialog", "by CCTech | 2019"))
        self.label_6.setText(_translate("Dialog", "Date_arr"))
        self.label_7.setText(_translate("Dialog", "Somme_A"))
        self.label_8.setText(_translate("Dialog", "Somme_B"))
        self.pushButton_effacer.setText(_translate("Dialog", "EFFACER"))
        self.pushButton_enregistrer.setText(_translate("Dialog", "ENREGISTRER"))