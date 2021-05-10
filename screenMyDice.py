# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenMyDice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenMyDice(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("banco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 55, 104);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(239, 10, 322, 60))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 800, 520))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_2.setStyleSheet("background-color: rgb(211, 243, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEditMyDiceName = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceName.setGeometry(QtCore.QRect(60, 160, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceName.setFont(font)
        self.lineEditMyDiceName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceName.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceName.setText("")
        self.lineEditMyDiceName.setMaxLength(40)
        self.lineEditMyDiceName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditMyDiceName.setDragEnabled(False)
        self.lineEditMyDiceName.setReadOnly(True)
        self.lineEditMyDiceName.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceName.setClearButtonEnabled(False)
        self.lineEditMyDiceName.setObjectName("lineEditMyDiceName")
        self.lineEditMyDiceCPF = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceCPF.setGeometry(QtCore.QRect(60, 310, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceCPF.setFont(font)
        self.lineEditMyDiceCPF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceCPF.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceCPF.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEditMyDiceCPF.setMaxLength(11)
        self.lineEditMyDiceCPF.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditMyDiceCPF.setDragEnabled(False)
        self.lineEditMyDiceCPF.setReadOnly(True)
        self.lineEditMyDiceCPF.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceCPF.setClearButtonEnabled(False)
        self.lineEditMyDiceCPF.setObjectName("lineEditMyDiceCPF")
        self.pushButtonComeBack = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonComeBack.setGeometry(QtCore.QRect(345, 436, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonComeBack.setFont(font)
        self.pushButtonComeBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonComeBack.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonComeBack.setObjectName("pushButtonComeBack")
        self.lineEditMyDiceSurname = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceSurname.setGeometry(QtCore.QRect(60, 235, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceSurname.setFont(font)
        self.lineEditMyDiceSurname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceSurname.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceSurname.setMaxLength(11)
        self.lineEditMyDiceSurname.setDragEnabled(False)
        self.lineEditMyDiceSurname.setReadOnly(True)
        self.lineEditMyDiceSurname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceSurname.setClearButtonEnabled(False)
        self.lineEditMyDiceSurname.setObjectName("lineEditMyDiceSurname")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 300, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(450, 60, 300, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditMyDiceAccountNumber = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceAccountNumber.setGeometry(QtCore.QRect(470, 160, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceAccountNumber.setFont(font)
        self.lineEditMyDiceAccountNumber.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceAccountNumber.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceAccountNumber.setText("")
        self.lineEditMyDiceAccountNumber.setMaxLength(40)
        self.lineEditMyDiceAccountNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditMyDiceAccountNumber.setDragEnabled(False)
        self.lineEditMyDiceAccountNumber.setReadOnly(True)
        self.lineEditMyDiceAccountNumber.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceAccountNumber.setClearButtonEnabled(False)
        self.lineEditMyDiceAccountNumber.setObjectName("lineEditMyDiceAccountNumber")
        self.lineEditMyDiceAccountLimit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceAccountLimit.setGeometry(QtCore.QRect(470, 385, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceAccountLimit.setFont(font)
        self.lineEditMyDiceAccountLimit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceAccountLimit.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceAccountLimit.setText("")
        self.lineEditMyDiceAccountLimit.setMaxLength(40)
        self.lineEditMyDiceAccountLimit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditMyDiceAccountLimit.setDragEnabled(False)
        self.lineEditMyDiceAccountLimit.setReadOnly(True)
        self.lineEditMyDiceAccountLimit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceAccountLimit.setClearButtonEnabled(False)
        self.lineEditMyDiceAccountLimit.setObjectName("lineEditMyDiceAccountLimit")
        self.lineEditMyDiceAccountHolder = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceAccountHolder.setGeometry(QtCore.QRect(470, 235, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceAccountHolder.setFont(font)
        self.lineEditMyDiceAccountHolder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceAccountHolder.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceAccountHolder.setText("")
        self.lineEditMyDiceAccountHolder.setMaxLength(40)
        self.lineEditMyDiceAccountHolder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditMyDiceAccountHolder.setDragEnabled(False)
        self.lineEditMyDiceAccountHolder.setReadOnly(True)
        self.lineEditMyDiceAccountHolder.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceAccountHolder.setClearButtonEnabled(False)
        self.lineEditMyDiceAccountHolder.setObjectName("lineEditMyDiceAccountHolder")
        self.lineEditMyDiceAccountBalance = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditMyDiceAccountBalance.setGeometry(QtCore.QRect(470, 310, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditMyDiceAccountBalance.setFont(font)
        self.lineEditMyDiceAccountBalance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditMyDiceAccountBalance.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditMyDiceAccountBalance.setText("")
        self.lineEditMyDiceAccountBalance.setMaxLength(40)
        self.lineEditMyDiceAccountBalance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditMyDiceAccountBalance.setDragEnabled(False)
        self.lineEditMyDiceAccountBalance.setReadOnly(True)
        self.lineEditMyDiceAccountBalance.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditMyDiceAccountBalance.setClearButtonEnabled(False)
        self.lineEditMyDiceAccountBalance.setObjectName("lineEditMyDiceAccountBalance")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 135, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(60, 285, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(470, 135, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(470, 210, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(470, 285, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(470, 360, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
"color: rgb(0, 55, 104);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButtonComeBack, self.lineEditMyDiceName)
        MainWindow.setTabOrder(self.lineEditMyDiceName, self.lineEditMyDiceSurname)
        MainWindow.setTabOrder(self.lineEditMyDiceSurname, self.lineEditMyDiceCPF)
        MainWindow.setTabOrder(self.lineEditMyDiceCPF, self.lineEditMyDiceAccountNumber)
        MainWindow.setTabOrder(self.lineEditMyDiceAccountNumber, self.lineEditMyDiceAccountHolder)
        MainWindow.setTabOrder(self.lineEditMyDiceAccountHolder, self.lineEditMyDiceAccountBalance)
        MainWindow.setTabOrder(self.lineEditMyDiceAccountBalance, self.lineEditMyDiceAccountLimit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Meus Dados"))
        self.label.setText(_translate("MainWindow", "Evollutte Bank"))
        self.lineEditMyDiceName.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.lineEditMyDiceCPF.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.pushButtonComeBack.setText(_translate("MainWindow", "Voltar"))
        self.lineEditMyDiceSurname.setPlaceholderText(_translate("MainWindow", "Sobrenome"))
        self.label_2.setText(_translate("MainWindow", "Dados Pessoais"))
        self.label_3.setText(_translate("MainWindow", "Dados Bancários"))
        self.lineEditMyDiceAccountNumber.setPlaceholderText(_translate("MainWindow", "Conta"))
        self.lineEditMyDiceAccountLimit.setPlaceholderText(_translate("MainWindow", "Limite"))
        self.lineEditMyDiceAccountHolder.setPlaceholderText(_translate("MainWindow", "Titular"))
        self.lineEditMyDiceAccountBalance.setPlaceholderText(_translate("MainWindow", "Saldo"))
        self.label_4.setText(_translate("MainWindow", "Nome:"))
        self.label_5.setText(_translate("MainWindow", "Sobrenome:"))
        self.label_6.setText(_translate("MainWindow", "CPF:"))
        self.label_7.setText(_translate("MainWindow", "Conta:"))
        self.label_8.setText(_translate("MainWindow", "Titular:"))
        self.label_9.setText(_translate("MainWindow", "Saldo:"))
        self.label_10.setText(_translate("MainWindow", "Limite:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ScreenMyDice()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
