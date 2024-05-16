# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeUIBaru.ui'
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
        self.Navbar.setGeometry(QtCore.QRect(0, 0, 201, 1081))
        self.Navbar.setStyleSheet("#Navbar{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"}")
        self.Navbar.setObjectName("Navbar")
        self.LogoErgo = QtWidgets.QLabel(self.Navbar)
        self.LogoErgo.setGeometry(QtCore.QRect(-15, 20, 221, 211))
        self.LogoErgo.setStyleSheet("")
        self.LogoErgo.setText("")
        self.LogoErgo.setPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/logoergo.png"))
        self.LogoErgo.setScaledContents(True)
        self.LogoErgo.setObjectName("LogoErgo")
        self.MainSection = QtWidgets.QWidget(Ergo)
        self.MainSection.setGeometry(QtCore.QRect(200, 60, 1811, 1031))
        self.MainSection.setStyleSheet("#MainSection{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #97C9ED);\n"
"}")
        self.MainSection.setObjectName("MainSection")
        self.HiUser = QtWidgets.QLabel(self.MainSection)
        self.HiUser.setGeometry(QtCore.QRect(40, 20, 181, 71))
        self.HiUser.setStyleSheet("#HiUser{\n"
"    font: 45px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.HiUser.setObjectName("HiUser")
        self.Containerforwords = QtWidgets.QWidget(self.MainSection)
        self.Containerforwords.setGeometry(QtCore.QRect(30, 100, 381, 111))
        self.Containerforwords.setStyleSheet("#Containerforwords{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"    border-radius: 15px;\n"
"}")
        self.Containerforwords.setObjectName("Containerforwords")
        self.Welcome = QtWidgets.QLabel(self.Containerforwords)
        self.Welcome.setGeometry(QtCore.QRect(20, 20, 171, 31))
        self.Welcome.setStyleSheet("#Welcome {\n"
"    font: bold 25px \"Roboto\";\n"
"    color: #FFFFFF;\n"
"}")
        self.Welcome.setObjectName("Welcome")
        self.ChooseBoard = QtWidgets.QLabel(self.Containerforwords)
        self.ChooseBoard.setGeometry(QtCore.QRect(20, 70, 351, 31))
        self.ChooseBoard.setStyleSheet("#ChooseBoard {\n"
"    font: bold 18px \"Roboto\";\n"
"    color: #FFFFFF\n"
"}")
        self.ChooseBoard.setObjectName("ChooseBoard")
        self.YourBoard = QtWidgets.QLabel(self.MainSection)
        self.YourBoard.setGeometry(QtCore.QRect(50, 290, 291, 51))
        self.YourBoard.setStyleSheet("#YourBoard{\n"
"    font: 40px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.YourBoard.setObjectName("YourBoard")
        self.AddBoardButton = QtWidgets.QPushButton(self.MainSection)
        self.AddBoardButton.setGeometry(QtCore.QRect(50, 370, 171, 31))
        self.AddBoardButton.setStyleSheet("#AddBoardButton{\n"
"    border : 1px solid #0047ab;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #0197F6;\n"
"}")
        self.AddBoardButton.setObjectName("AddBoardButton")
        self.widget = QtWidgets.QWidget(self.MainSection)
        self.widget.setGeometry(QtCore.QRect(30, 430, 631, 581))
        self.widget.setStyleSheet("#widget{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"    border-radius : 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.ContainerForBoards = QtWidgets.QScrollArea(self.widget)
        self.ContainerForBoards.setGeometry(QtCore.QRect(10, 10, 601, 561))
        self.ContainerForBoards.setStyleSheet("#ContainerForBoards, QScrollArea QWidget{\n"
"    border-radius: 10px;\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"}")
        self.ContainerForBoards.setWidgetResizable(True)
        self.ContainerForBoards.setObjectName("ContainerForBoards")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 601, 561))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Board1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board1.setGeometry(QtCore.QRect(10, 10, 271, 91))
        self.Board1.setStyleSheet("#Board1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Board1.setObjectName("Board1")
        self.Board2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Board2.setGeometry(QtCore.QRect(310, 10, 271, 91))
        self.Board2.setStyleSheet("#Board2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Board2.setObjectName("Board2")
        self.ContainerForBoards.setWidget(self.scrollAreaWidgetContents)
        self.AddingBoard = QtWidgets.QWidget(self.MainSection)
        self.AddingBoard.setGeometry(QtCore.QRect(225, 370, 271, 161))
        self.AddingBoard.setStyleSheet("#AddingBoard{\n"
"    border: 0.5px solid #052659;\n"
"    background-color: #87ceeb;\n"
"    border-radius: 17px;\n"
"}")
        self.AddingBoard.setObjectName("AddingBoard")
        self.BoardTitle = QtWidgets.QLabel(self.AddingBoard)
        self.BoardTitle.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.BoardTitle.setStyleSheet("#BoardTitle{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle.setObjectName("BoardTitle")
        self.inputBoardtitle = QtWidgets.QLineEdit(self.AddingBoard)
        self.inputBoardtitle.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.inputBoardtitle.setStyleSheet("#inputBoardtitle{\n"
"    border-radius : 10px;\n"
"}")
        self.inputBoardtitle.setObjectName("inputBoardtitle")
        self.CreateBoard = QtWidgets.QPushButton(self.AddingBoard)
        self.CreateBoard.setGeometry(QtCore.QRect(10, 110, 251, 41))
        self.CreateBoard.setStyleSheet("#CreateBoard{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.CreateBoard.setObjectName("CreateBoard")
        self.FavoriteBoard = QtWidgets.QLabel(self.MainSection)
        self.FavoriteBoard.setGeometry(QtCore.QRect(760, 300, 351, 51))
        self.FavoriteBoard.setStyleSheet("#FavoriteBoard{\n"
"    font: 40px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.FavoriteBoard.setObjectName("FavoriteBoard")
        self.QuickAccess = QtWidgets.QLabel(self.MainSection)
        self.QuickAccess.setGeometry(QtCore.QRect(770, 370, 661, 31))
        self.QuickAccess.setStyleSheet("#QuickAccess\n"
"{\n"
"    font: 20px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.QuickAccess.setObjectName("QuickAccess")
        self.widget_2 = QtWidgets.QWidget(self.MainSection)
        self.widget_2.setGeometry(QtCore.QRect(770, 430, 631, 581))
        self.widget_2.setStyleSheet("#widget_2\n"
"{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"    border-radius : 10px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.ContainerForBoards_2 = QtWidgets.QScrollArea(self.widget_2)
        self.ContainerForBoards_2.setGeometry(QtCore.QRect(10, 10, 601, 561))
        self.ContainerForBoards_2.setStyleSheet("#ContainerForBoards_2, QScrollArea QWidget{\n"
"    border-radius: 10px;\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"}")
        self.ContainerForBoards_2.setWidgetResizable(True)
        self.ContainerForBoards_2.setObjectName("ContainerForBoards_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 601, 561))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Favboard1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Favboard1.setGeometry(QtCore.QRect(10, 10, 271, 91))
        self.Favboard1.setStyleSheet("#Favboard1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Favboard1.setObjectName("Favboard1")
        self.Favboard2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Favboard2.setGeometry(QtCore.QRect(320, 10, 271, 91))
        self.Favboard2.setStyleSheet("#Favboard2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Favboard2.setObjectName("Favboard2")
        self.ContainerForBoards_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Containerforwords.raise_()
        self.YourBoard.raise_()
        self.AddBoardButton.raise_()
        self.HiUser.raise_()
        self.widget.raise_()
        self.AddingBoard.raise_()
        self.FavoriteBoard.raise_()
        self.QuickAccess.raise_()
        self.widget_2.raise_()
        self.Searchbar = QtWidgets.QWidget(Ergo)
        self.Searchbar.setGeometry(QtCore.QRect(200, 0, 1721, 61))
        self.Searchbar.setStyleSheet("#Searchbar{\n"
"    background: qlineargradient(x1:0, y1:0, x2:2, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
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
        self.SmileyFace.setGeometry(QtCore.QRect(1530, 10, 41, 41))
        self.SmileyFace.setText("")
        self.SmileyFace.setPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/smileyface.png"))
        self.SmileyFace.setScaledContents(True)
        self.SmileyFace.setObjectName("SmileyFace")
        self.UserErgo = QtWidgets.QLabel(self.Searchbar)
        self.UserErgo.setGeometry(QtCore.QRect(1580, 20, 71, 21))
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
        icon.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon)
        self.SearchButton.setObjectName("SearchButton")
        self.Searchbar.raise_()
        self.MainSection.raise_()
        self.Navbar.raise_()

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
        self.Board1.setText(_translate("Ergo", "Build UI"))
        self.Board2.setText(_translate("Ergo", "Dummy"))
        self.BoardTitle.setText(_translate("Ergo", "Board Title"))
        self.CreateBoard.setText(_translate("Ergo", "Create Project"))
        self.FavoriteBoard.setText(_translate("Ergo", "Favorite Boards"))
        self.QuickAccess.setText(_translate("Ergo", "Get quick access to your favorite boards by giving a star on them"))
        self.Favboard1.setText(_translate("Ergo", "Build UI"))
        self.Favboard2.setText(_translate("Ergo", "Dummy"))
        self.SearchBoard.setText(_translate("Ergo", "          Search Your Board"))
        self.UserErgo.setText(_translate("Ergo", "  User Ergo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ergo = QtWidgets.QWidget()
    ui = Ui_Ergo()
    ui.setupUi(Ergo)
    Ergo.show()
    sys.exit(app.exec_())
