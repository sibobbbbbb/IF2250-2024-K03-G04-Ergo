# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ergo(object):
        def setupUi(self, Ergo):
                Ergo.setObjectName("Ergo")
                Ergo.resize(586, 442)
                self.Navbar = QtWidgets.QWidget(Ergo)
                self.Navbar.setGeometry(QtCore.QRect(0, 0, 111, 451))
                self.Navbar.setStyleSheet("#Navbar{\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5483B3, stop:1 #24384D);\n"
        "}")
                self.Navbar.setObjectName("Navbar")
                self.label_3 = QtWidgets.QLabel(self.Navbar)
                self.label_3.setGeometry(QtCore.QRect(-20, 10, 141, 141))
                self.label_3.setText("")
                self.label_3.setPixmap(QtGui.QPixmap("assets/ERGO.png"))
                self.label_3.setScaledContents(True)
                self.label_3.setObjectName("label_3")
                self.MainSection = QtWidgets.QWidget(Ergo)
                self.MainSection.setGeometry(QtCore.QRect(110, 40, 491, 421))
                self.MainSection.setStyleSheet("#MainSection{\n"
        "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DAD9D8, stop:1 #97C9ED);\n"
        "}")
                self.MainSection.setObjectName("MainSection")
                self.Greetings = QtWidgets.QLabel(self.MainSection)
                self.Greetings.setGeometry(QtCore.QRect(20, 10, 121, 31))
                self.Greetings.setStyleSheet("#Greetings{\n"
        "    font: 30px \"Roboto\";\n"
        "    color: #5483B3;\n"
        "    font-weight: bold;\n"
        "}")
                self.Greetings.setObjectName("Greetings")
                self.Containerforwords = QtWidgets.QWidget(self.MainSection)
                self.Containerforwords.setGeometry(QtCore.QRect(10, 50, 211, 61))
                self.Containerforwords.setStyleSheet("#Containerforwords{\n"
        "    border: 2px solid #9FB0CC;\n"
        "    background-color: #ECECF3;\n"
        "    border-radius: 17px;\n"
        "}")
                self.Containerforwords.setObjectName("Containerforwords")
                self.label = QtWidgets.QLabel(self.Containerforwords)
                self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
                self.label.setStyleSheet("#label {\n"
        "    font: bold 15px \"Roboto\";\n"
        "    color: #7DA0CA;\n"
        "}")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.Containerforwords)
                self.label_2.setGeometry(QtCore.QRect(10, 40, 211, 16))
                self.label_2.setStyleSheet("#label_2 {\n"
        "    font: bold 10px \"Roboto\";\n"
        "    color: #7DA0CA;\n"
        "}")
                self.label_2.setObjectName("label_2")
                self.Greetings_2 = QtWidgets.QLabel(self.MainSection)
                self.Greetings_2.setGeometry(QtCore.QRect(20, 130, 131, 31))
                self.Greetings_2.setStyleSheet("#Greetings_2{\n"
        "    font: 20px \"Roboto\";\n"
        "    color: #5483B3;\n"
        "    font-weight: bold;\n"
        "}")
                self.Greetings_2.setObjectName("Greetings_2")
                self.pushButton = QtWidgets.QPushButton(self.MainSection)
                self.pushButton.setGeometry(QtCore.QRect(20, 160, 111, 24))
                self.pushButton.setStyleSheet("#pushButton{\n"
        "    border: 2px solid #9FB0CC;\n"
        "    background-color: #ECECF3;\n"
        "    border-radius: 10px;\n"
        "    font-family: \"Roboto\";\n"
        "    font-size: 11px;\n"
        "    font-weight: bold;\n"
        "    color: #5483B3;\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(self.MainSection)
                self.pushButton_2.setGeometry(QtCore.QRect(20, 190, 131, 51))
                self.pushButton_2.setStyleSheet("#pushButton_2{\n"
        "    background-color: #F6F6F6;\n"
        "    border-radius: 10px;\n"
        "    font-family: \"Roboto\";\n"
        "    font-size: 10px;\n"
        "    font-weight: bold;\n"
        "   color: #5483B3;\n"
        "}")
                self.pushButton_2.setObjectName("pushButton_2")
                self.Greetings_3 = QtWidgets.QLabel(self.MainSection)
                self.Greetings_3.setGeometry(QtCore.QRect(20, 260, 171, 31))
                self.Greetings_3.setStyleSheet("#Greetings_3{\n"
        "    font: 20px \"Roboto\";\n"
        "    color: #5483B3;\n"
        "    font-weight: bold;\n"
        "}")
                self.Greetings_3.setObjectName("Greetings_3")
                self.Greetings_4 = QtWidgets.QLabel(self.MainSection)
                self.Greetings_4.setGeometry(QtCore.QRect(20, 290, 351, 31))
                self.Greetings_4.setStyleSheet("#Greetings_4\n"
        "{\n"
        "    font: 10px \"Roboto\";\n"
        "    color: #5483B3;\n"
        "    font-weight: bold;\n"
        "}")
                self.Greetings_4.setObjectName("Greetings_4")
                self.pushButton_4 = QtWidgets.QPushButton(self.MainSection)
                self.pushButton_4.setGeometry(QtCore.QRect(20, 320, 131, 51))
                self.pushButton_4.setStyleSheet("#pushButton_4{\n"
        "    background-color: #F6F6F6;\n"
        "    border-radius: 10px;\n"
        "    font-family: \"Roboto\";\n"
        "    font-size: 10px;\n"
        "    font-weight: bold;\n"
        "   color: #5483B3;\n"
        "}")
                self.pushButton_4.setObjectName("pushButton_4")
                self.AddingBoard = QtWidgets.QWidget(self.MainSection)
                self.AddingBoard.setGeometry(QtCore.QRect(130, 160, 111, 101))
                self.AddingBoard.setStyleSheet("#AddingBoard{\n"
        "    border: 2px solid #052659;\n"
        "    background-color: #D0E3FF;\n"
        "    border-radius: 17px;\n"
        "}")
                self.AddingBoard.setObjectName("AddingBoard")
                self.BoardTitle = QtWidgets.QLabel(self.AddingBoard)
                self.BoardTitle.setGeometry(QtCore.QRect(10, 10, 71, 16))
                self.BoardTitle.setStyleSheet("#BoardTitle{\n"
        "    font-family: Rubik;\n"
        "    font-size: 9px;\n"
        "    font-weight: bold;\n"
        "   color: #052659;\n"
        "}")
                self.BoardTitle.setObjectName("BoardTitle")
                self.inputBoardtitle = QtWidgets.QLineEdit(self.AddingBoard)
                self.inputBoardtitle.setGeometry(QtCore.QRect(10, 30, 91, 20))
                self.inputBoardtitle.setStyleSheet("#inputBoardtitle{\n"
        "    border-radius : 10px;\n"
        "}")
                self.inputBoardtitle.setObjectName("inputBoardtitle")
                self.BoardTitle_2 = QtWidgets.QLabel(self.AddingBoard)
                self.BoardTitle_2.setGeometry(QtCore.QRect(10, 50, 91, 16))
                self.BoardTitle_2.setStyleSheet("#BoardTitle_2{\n"
        "    font-family: Rubik;\n"
        "    font-size: 7px;\n"
        "    font-weight: bold;\n"
        "   color: #052659;\n"
        "}")
                self.BoardTitle_2.setObjectName("BoardTitle_2")
                self.CreateBoard = QtWidgets.QPushButton(self.AddingBoard)
                self.CreateBoard.setGeometry(QtCore.QRect(10, 70, 91, 20))
                self.CreateBoard.setStyleSheet("#CreateBoard{\n"
        "    font-family: Rubik;\n"
        "    font-size: 12px;\n"
        "    font-weight: bold;\n"
        "   color: #052659;\n"
        "}")
                self.CreateBoard.setObjectName("CreateBoard")
                self.Containerforwords.raise_()
                self.Greetings_2.raise_()
                self.pushButton.raise_()
                self.pushButton_2.raise_()
                self.Greetings_3.raise_()
                self.Greetings_4.raise_()
                self.Greetings.raise_()
                self.pushButton_4.raise_()
                self.AddingBoard.raise_()
                self.Searchbar = QtWidgets.QWidget(Ergo)
                self.Searchbar.setGeometry(QtCore.QRect(100, 0, 551, 41))
                self.Searchbar.setStyleSheet("#Searchbar{\n"
        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5483B3, stop:1 #4D6D8F);\n"
        "}")
                self.Searchbar.setObjectName("Searchbar")
                self.lineEdit = QtWidgets.QLineEdit(self.Searchbar)
                self.lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 22))
                self.lineEdit.setStyleSheet("#lineEdit{\n"
        "    border-radius : 10px;\n"
        "    font-family : Rubik;\n"
        "    color : #6C6C6C;\n"
        "    font-size : 10px;\n"
        "}")
                self.lineEdit.setObjectName("lineEdit")
                self.label_4 = QtWidgets.QLabel(self.Searchbar)
                self.label_4.setGeometry(QtCore.QRect(400, 10, 21, 21))
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap("assets/SMILE.png"))
                self.label_4.setScaledContents(True)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.Searchbar)
                self.label_5.setGeometry(QtCore.QRect(420, 10, 51, 16))
                self.label_5.setStyleSheet("#label_5{\n"
        "    font-family : Rubik;\n"
        "    font-size : 9px;\n"
        "}")
                self.label_5.setObjectName("label_5")
                self.pushButton_3 = QtWidgets.QPushButton(self.Searchbar)
                self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 31, 21))
                self.pushButton_3.setStyleSheet("#pushButton_3{\n"
        "    border : none;\n"
        "}")
                self.pushButton_3.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("assets/SEARCH.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_3.setIcon(icon)
                self.pushButton_3.setObjectName("pushButton_3")

                self.retranslateUi(Ergo)
                QtCore.QMetaObject.connectSlotsByName(Ergo)
        
        def retranslateUi(self, Ergo):
                _translate = QtCore.QCoreApplication.translate
                Ergo.setWindowTitle(_translate("Ergo", "Ergo"))
                self.Greetings.setText(_translate("Ergo", "Hi User"))
                self.label.setText(_translate("Ergo", "Welcome!"))
                self.label_2.setText(_translate("Ergo", "Choose a board to begin your journey"))
                self.Greetings_2.setText(_translate("Ergo", "Your Boards"))
                self.pushButton.setText(_translate("Ergo", "+ Add New Board"))
                self.pushButton_2.setText(_translate("Ergo", "Mobile Development"))
                self.Greetings_3.setText(_translate("Ergo", "Favorite Boards"))
                self.Greetings_4.setText(_translate("Ergo", "Get quick access to your favorite boards by giving a star on them"))
                self.pushButton_4.setText(_translate("Ergo", "Mobile Development"))
                self.BoardTitle.setText(_translate("Ergo", "Board Title"))
                self.BoardTitle_2.setText(_translate("Ergo", "Board Title is required"))
                self.CreateBoard.setText(_translate("Ergo", "Create"))
                self.lineEdit.setText(_translate("Ergo", "              Search Your Board"))
                self.label_5.setText(_translate("Ergo", "  User Ergo"))