# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ergo(object):
    def setupUi(self, Ergo):
        Ergo.setObjectName("Ergo")
        Ergo.resize(1920, 1080)
        self.Navbar = QtWidgets.QWidget(Ergo)
        self.Navbar.setGeometry(QtCore.QRect(0, 0, 131, 1081))
        self.Navbar.setStyleSheet("#Navbar{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5483B3, stop:1 #24384D);\n"
"}")
        self.Navbar.setObjectName("Navbar")
        self.LogoErgo = QtWidgets.QLabel(self.Navbar)
        self.LogoErgo.setGeometry(QtCore.QRect(-40, 30, 201, 191))
        self.LogoErgo.setStyleSheet("")
        self.LogoErgo.setText("")
        self.LogoErgo.setPixmap(QtGui.QPixmap("img\\logoergo.png"))
        self.LogoErgo.setScaledContents(True)
        self.LogoErgo.setObjectName("LogoErgo")
        self.MainSection = QtWidgets.QWidget(Ergo)
        self.MainSection.setGeometry(QtCore.QRect(130, 50, 1811, 1031))
        self.MainSection.setStyleSheet("#MainSection{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DAD9D8, stop:1 #97C9ED);\n"
"}")
        self.MainSection.setObjectName("MainSection")
        self.HiUser = QtWidgets.QLabel(self.MainSection)
        self.HiUser.setGeometry(QtCore.QRect(20, 20, 201, 71))
        self.HiUser.setStyleSheet("#HiUser{\n"
"    font: 50px \"Roboto\";\n"
"    color: #5483B3;\n"
"    font-weight: bold;\n"
"}")
        self.HiUser.setObjectName("HiUser")
        self.Containerforwords = QtWidgets.QWidget(self.MainSection)
        self.Containerforwords.setGeometry(QtCore.QRect(10, 100, 401, 121))
        self.Containerforwords.setStyleSheet("#Containerforwords{\n"
"    border: 2px solid #9FB0CC;\n"
"    background-color: #ECECF3;\n"
"    border-radius: 17px;\n"
"}")
        self.Containerforwords.setObjectName("Containerforwords")
        self.Welcome = QtWidgets.QLabel(self.Containerforwords)
        self.Welcome.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.Welcome.setStyleSheet("#Welcome {\n"
"    font: bold 30px \"Roboto\";\n"
"    color: #7DA0CA;\n"
"}")
        self.Welcome.setObjectName("Welcome")
        self.ChooseBoard = QtWidgets.QLabel(self.Containerforwords)
        self.ChooseBoard.setGeometry(QtCore.QRect(10, 70, 471, 31))
        self.ChooseBoard.setStyleSheet("#ChooseBoard {\n"
"    font: bold 20px \"Roboto\";\n"
"    color: #7DA0CA;\n"
"}")
        self.ChooseBoard.setObjectName("ChooseBoard")
        self.YourBoard = QtWidgets.QLabel(self.MainSection)
        self.YourBoard.setGeometry(QtCore.QRect(20, 240, 341, 91))
        self.YourBoard.setStyleSheet("#YourBoard{\n"
"    font: 45px \"Roboto\";\n"
"    color: #5483B3;\n"
"    font-weight: bold;\n"
"}")
        self.YourBoard.setObjectName("YourBoard")
        self.AddBoardButton = QtWidgets.QPushButton(self.MainSection)
        self.AddBoardButton.setGeometry(QtCore.QRect(20, 330, 151, 31))
        self.AddBoardButton.setStyleSheet("#AddBoardButton{\n"
"    border: 2px solid #9FB0CC;\n"
"    background-color: #ECECF3;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #5483B3;\n"
"}")
        self.AddBoardButton.setObjectName("AddBoardButton")
        self.FavoriteBoard = QtWidgets.QLabel(self.MainSection)
        self.FavoriteBoard.setGeometry(QtCore.QRect(20, 620, 371, 91))
        self.FavoriteBoard.setStyleSheet("#FavoriteBoard{\n"
"    font: 45px \"Roboto\";\n"
"    color: #5483B3;\n"
"    font-weight: bold;\n"
"}")
        self.FavoriteBoard.setObjectName("FavoriteBoard")
        self.QuickAccess = QtWidgets.QLabel(self.MainSection)
        self.QuickAccess.setGeometry(QtCore.QRect(20, 700, 661, 31))
        self.QuickAccess.setStyleSheet("#QuickAccess\n"
"{\n"
"    font: 20px \"Roboto\";\n"
"    color: #5483B3;\n"
"    font-weight: bold;\n"
"}")
        self.QuickAccess.setObjectName("QuickAccess")
        self.AddingBoard = QtWidgets.QWidget(self.MainSection)
        self.AddingBoard.setGeometry(QtCore.QRect(180, 330, 271, 211))
        self.AddingBoard.setStyleSheet("#AddingBoard{\n"
"    border: 2px solid #052659;\n"
"    background-color: #D0E3FF;\n"
"    border-radius: 17px;\n"
"}")
        self.AddingBoard.setObjectName("AddingBoard")
        self.BoardTitle = QtWidgets.QLabel(self.AddingBoard)
        self.BoardTitle.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.BoardTitle.setStyleSheet("#BoardTitle{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle.setObjectName("BoardTitle")
        self.BoardTitle_2 = QtWidgets.QLabel(self.AddingBoard)
        self.BoardTitle_2.setGeometry(QtCore.QRect(20, 90, 181, 21))
        self.BoardTitle_2.setStyleSheet("#BoardTitle_2{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle_2.setObjectName("BoardTitle_2")
        self.inputBoardtitle = QtWidgets.QLineEdit(self.AddingBoard)
        self.inputBoardtitle.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.inputBoardtitle.setStyleSheet("#inputBoardtitle{\n"
"    border-radius : 10px;\n"
"}")
        self.inputBoardtitle.setObjectName("inputBoardtitle")
        self.CreateBoard = QtWidgets.QPushButton(self.AddingBoard)
        self.CreateBoard.setGeometry(QtCore.QRect(10, 150, 251, 41))
        self.CreateBoard.setStyleSheet("#CreateBoard{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.CreateBoard.setObjectName("CreateBoard")
        self.ContainerForBoards = QtWidgets.QScrollArea(self.MainSection)
        self.ContainerForBoards.setGeometry(QtCore.QRect(20, 370, 821, 241))
        self.ContainerForBoards.setStyleSheet("#ContainerForBoards, QScrollArea QWidget {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5F84A2, stop:1 #91AEC4);\n"
"}")
        self.ContainerForBoards.setWidgetResizable(True)
        self.ContainerForBoards.setObjectName("ContainerForBoards")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 821, 241))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Board1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board1.setGeometry(QtCore.QRect(20, 20, 221, 61))
        self.Board1.setStyleSheet("#Board1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.Board1.setObjectName("Board1")
        self.Board2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board2.setGeometry(QtCore.QRect(320, 20, 221, 61))
        self.Board2.setStyleSheet("#Board2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.Board2.setObjectName("Board2")
        self.Board3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board3.setGeometry(QtCore.QRect(560, 20, 221, 61))
        self.Board3.setStyleSheet("#Board3{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.Board3.setObjectName("Board3")
        self.Board4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board4.setGeometry(QtCore.QRect(20, 100, 221, 61))
        self.Board4.setStyleSheet("#Board4{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.Board4.setObjectName("Board4")
        self.ContainerForBoards.setWidget(self.scrollAreaWidgetContents)
        self.ContainerForBoards_2 = QtWidgets.QScrollArea(self.MainSection)
        self.ContainerForBoards_2.setGeometry(QtCore.QRect(20, 750, 821, 241))
        self.ContainerForBoards_2.setStyleSheet("#ContainerForBoards_2, QScrollArea QWidget {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5F84A2, stop:1 #91AEC4);\n"
"}")
        self.ContainerForBoards_2.setWidgetResizable(True)
        self.ContainerForBoards_2.setObjectName("ContainerForBoards_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 821, 241))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Favboard1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Favboard1.setGeometry(QtCore.QRect(20, 20, 221, 61))
        self.Favboard1.setStyleSheet("#Favboard1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.Favboard1.setObjectName("Favboard1")
        self.ContainerForBoards_2.setWidget(self.scrollAreaWidgetContents_2)
        self.ContainerForBoards.raise_()
        self.Containerforwords.raise_()
        self.YourBoard.raise_()
        self.AddBoardButton.raise_()
        self.FavoriteBoard.raise_()
        self.QuickAccess.raise_()
        self.HiUser.raise_()
        self.AddingBoard.raise_()
        self.ContainerForBoards_2.raise_()
        self.Searchbar = QtWidgets.QWidget(Ergo)
        self.Searchbar.setGeometry(QtCore.QRect(130, 0, 1851, 61))
        self.Searchbar.setStyleSheet("#Searchbar{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5483B3, stop:1 #4D6D8F);\n"
"    border : none;\n"
"}")
        self.Searchbar.setObjectName("Searchbar")
        self.SearchBoard = QtWidgets.QLineEdit(self.Searchbar)
        self.SearchBoard.setGeometry(QtCore.QRect(20, 20, 811, 31))
        self.SearchBoard.setStyleSheet("#SearchBoard{\n"
"    border-radius : 10px;\n"
"    font-family : Rubik;\n"
"    color : #6C6C6C;\n"
"    font-size : 15px;\n"
"}")
        self.SearchBoard.setObjectName("SearchBoard")
        self.SmileyFace = QtWidgets.QLabel(self.Searchbar)
        self.SmileyFace.setGeometry(QtCore.QRect(1620, 10, 41, 41))
        self.SmileyFace.setText("")
        self.SmileyFace.setPixmap(QtGui.QPixmap("img\\smileyface.png"))
        self.SmileyFace.setScaledContents(True)
        self.SmileyFace.setObjectName("SmileyFace")
        self.UserErgo = QtWidgets.QLabel(self.Searchbar)
        self.UserErgo.setGeometry(QtCore.QRect(1660, 20, 71, 21))
        self.UserErgo.setStyleSheet("#UserErgo{\n"
"    font-family : Rubik;\n"
"    font-size : 13px;\n"
"}")
        self.UserErgo.setObjectName("UserErgo")
        self.SearchButton = QtWidgets.QPushButton(self.Searchbar)
        self.SearchButton.setGeometry(QtCore.QRect(830, 20, 41, 31))
        self.SearchButton.setStyleSheet("#SearchButton{\n"
"    border : none;\n"
"}")
        self.SearchButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img\\search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon)
        self.SearchButton.setObjectName("SearchButton")

        self.retranslateUi(Ergo)
        QtCore.QMetaObject.connectSlotsByName(Ergo)

    def retranslateUi(self, Ergo):
        _translate = QtCore.QCoreApplication.translate
        Ergo.setWindowTitle(_translate("Ergo", "Ergo"))
        self.HiUser.setText(_translate("Ergo", "Hi User"))
        self.Welcome.setText(_translate("Ergo", "Welcome!"))
        self.ChooseBoard.setText(_translate("Ergo", "Choose a board to begin your journey"))
        self.YourBoard.setText(_translate("Ergo", "Your Boards"))
        self.AddBoardButton.setText(_translate("Ergo", "+ Add New Board"))
        self.FavoriteBoard.setText(_translate("Ergo", "Favorite Boards"))
        self.QuickAccess.setText(_translate("Ergo", "Get quick access to your favorite boards by giving a star on them"))
        self.BoardTitle.setText(_translate("Ergo", "Board Title"))
        self.BoardTitle_2.setText(_translate("Ergo", "Board Title is required"))
        self.CreateBoard.setText(_translate("Ergo", "Create Board"))
        self.Board1.setText(_translate("Ergo", "Mobile Development"))
        self.Board2.setText(_translate("Ergo", "Mobile Development"))
        self.Board3.setText(_translate("Ergo", "Mobile Development"))
        self.Board4.setText(_translate("Ergo", "Mobile Development"))
        self.Favboard1.setText(_translate("Ergo", "Mobile Development"))
        self.UserErgo.setText(_translate("Ergo", "  User Ergo"))
