# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boardUIBaru.ui'
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
        self.back_2 = QtWidgets.QPushButton(self.Navbar)
        self.back_2.setGeometry(QtCore.QRect(50, 230, 91, 31))
        self.back_2.setStyleSheet("#back_2\n"
" {\n"
"    font: 15px \"Roboto\";\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color:  #FFFFFF;\n"
"}")
        self.back_2.setObjectName("back_2")
        self.MainSection = QtWidgets.QWidget(Ergo)
        self.MainSection.setGeometry(QtCore.QRect(200, 60, 1811, 1031))
        self.MainSection.setStyleSheet("#MainSection{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #97C9ED);\n"
"}")
        self.MainSection.setObjectName("MainSection")
        self.BoardName = QtWidgets.QLabel(self.MainSection)
        self.BoardName.setGeometry(QtCore.QRect(40, 40, 561, 71))
        self.BoardName.setStyleSheet("#BoardName{\n"
"    font: 45px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.BoardName.setObjectName("BoardName")
        self.Containerforwords = QtWidgets.QWidget(self.MainSection)
        self.Containerforwords.setGeometry(QtCore.QRect(30, 130, 621, 111))
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
        self.WelcomeProject = QtWidgets.QLabel(self.Containerforwords)
        self.WelcomeProject.setGeometry(QtCore.QRect(20, 70, 591, 31))
        self.WelcomeProject.setStyleSheet("#WelcomeProject {\n"
"    font: bold 18px \"Roboto\";\n"
"    color: #FFFFFF\n"
"}")
        self.WelcomeProject.setObjectName("WelcomeProject")
        self.YourProject = QtWidgets.QLabel(self.MainSection)
        self.YourProject.setGeometry(QtCore.QRect(50, 300, 291, 51))
        self.YourProject.setStyleSheet("#YourProject{\n"
"    font: 40px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.YourProject.setObjectName("YourProject")
        self.AddProjectButton = QtWidgets.QPushButton(self.MainSection)
        self.AddProjectButton.setGeometry(QtCore.QRect(260, 370, 171, 31))
        self.AddProjectButton.setStyleSheet("#AddProjectButton{\n"
"    border : 1px solid #0047ab;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #0197F6;\n"
"}")
        self.AddProjectButton.setObjectName("AddProjectButton")
        self.Sorting = QtWidgets.QPushButton(self.MainSection)
        self.Sorting.setGeometry(QtCore.QRect(50, 370, 171, 31))
        self.Sorting.setStyleSheet("#Sorting{\n"
"    border : 1px solid #0047ab;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #0197F6;\n"
"}")
        self.Sorting.setObjectName("Sorting")
        self.MainSettings = QtWidgets.QPushButton(self.MainSection)
        self.MainSettings.setGeometry(QtCore.QRect(1660, 20, 41, 41))
        self.MainSettings.setStyleSheet("#MainSettings{\n"
"    border : none;\n"
"}")
        self.MainSettings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainSettings.setIcon(icon)
        self.MainSettings.setObjectName("MainSettings")
        self.Actions_2 = QtWidgets.QWidget(self.MainSection)
        self.Actions_2.setGeometry(QtCore.QRect(1390, 30, 271, 171))
        self.Actions_2.setStyleSheet("#Actions_2{\n"
"    border: 0.5px solid #052659;\n"
"    background-color: #87ceeb;\n"
"    border-radius: 17px;\n"
"}")
        self.Actions_2.setObjectName("Actions_2")
        self.BoardTitle_4 = QtWidgets.QLabel(self.Actions_2)
        self.BoardTitle_4.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.BoardTitle_4.setStyleSheet("#BoardTitle_4{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle_4.setObjectName("BoardTitle_4")
        self.Favorite_2 = QtWidgets.QPushButton(self.Actions_2)
        self.Favorite_2.setGeometry(QtCore.QRect(10, 50, 251, 41))
        self.Favorite_2.setStyleSheet("#Favorite_2{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Favorite_2.setIcon(icon1)
        self.Favorite_2.setObjectName("Favorite_2")
        self.DeleteProject_2 = QtWidgets.QPushButton(self.Actions_2)
        self.DeleteProject_2.setGeometry(QtCore.QRect(10, 100, 251, 41))
        self.DeleteProject_2.setToolTipDuration(-1)
        self.DeleteProject_2.setStyleSheet("#DeleteProject_2{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/trashcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteProject_2.setIcon(icon2)
        self.DeleteProject_2.setObjectName("DeleteProject_2")
        self.namaboard = QtWidgets.QLabel(self.MainSection)
        self.namaboard.setGeometry(QtCore.QRect(130, 5, 161, 21))
        self.namaboard.setStyleSheet("#namaboard {\n"
"    color : #5483B3\n"
"}")
        self.namaboard.setObjectName("namaboard")
        self.back = QtWidgets.QPushButton(self.MainSection)
        self.back.setGeometry(QtCore.QRect(50, 0, 71, 31))
        self.back.setStyleSheet("#back {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color:  #0E49B5;;\n"
"}")
        self.back.setObjectName("back")
        self.SortingOption = QtWidgets.QWidget(self.MainSection)
        self.SortingOption.setGeometry(QtCore.QRect(50, 405, 271, 121))
        self.SortingOption.setStyleSheet("#SortingOption\n"
"{\n"
"    border: 0.5px solid #052659;\n"
"    background-color: #87ceeb;\n"
"    border-radius: 17px;\n"
"}")
        self.SortingOption.setObjectName("SortingOption")
        self.Sort1 = QtWidgets.QPushButton(self.SortingOption)
        self.Sort1.setGeometry(QtCore.QRect(10, 60, 251, 41))
        self.Sort1.setStyleSheet("#Sort1{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Downloads/down (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sort1.setIcon(icon3)
        self.Sort1.setObjectName("Sort1")
        self.Sort2 = QtWidgets.QPushButton(self.SortingOption)
        self.Sort2.setGeometry(QtCore.QRect(10, 10, 251, 41))
        self.Sort2.setStyleSheet("#Sort2{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../Downloads/top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Sort2.setIcon(icon4)
        self.Sort2.setObjectName("Sort2")
        self.widget = QtWidgets.QWidget(self.MainSection)
        self.widget.setGeometry(QtCore.QRect(30, 430, 631, 581))
        self.widget.setStyleSheet("#widget{\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"    border-radius : 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 601, 561))
        self.scrollArea.setStyleSheet("#scrollArea, QScrollArea QWidget{\n"
"    border-radius: 10px;\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 601, 561))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.Project1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Project1.setGeometry(QtCore.QRect(10, 10, 271, 91))
        self.Project1.setStyleSheet("#Project1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Project1.setObjectName("Project1")
        self.label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label1.setGeometry(QtCore.QRect(20, 75, 201, 16))
        self.label1.setStyleSheet("#label1{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 41, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #5483B3;\n"
"}")
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/3dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName("pushButton")
        self.Project1_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Project1_3.setGeometry(QtCore.QRect(310, 10, 271, 91))
        self.Project1_3.setStyleSheet("#Project1_3{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Project1_3.setObjectName("Project1_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.AddingProject = QtWidgets.QWidget(self.MainSection)
        self.AddingProject.setGeometry(QtCore.QRect(435, 370, 271, 241))
        self.AddingProject.setStyleSheet("#AddingProject{\n"
"    border: 0.5px solid #052659;\n"
"    background-color: #87ceeb;\n"
"    border-radius: 17px;\n"
"}")
        self.AddingProject.setObjectName("AddingProject")
        self.BoardTitle = QtWidgets.QLabel(self.AddingProject)
        self.BoardTitle.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.BoardTitle.setStyleSheet("#BoardTitle{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle.setObjectName("BoardTitle")
        self.inputBoardtitle = QtWidgets.QLineEdit(self.AddingProject)
        self.inputBoardtitle.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.inputBoardtitle.setStyleSheet("#inputBoardtitle{\n"
"    border-radius : 10px;\n"
"}")
        self.inputBoardtitle.setObjectName("inputBoardtitle")
        self.CreateBoard = QtWidgets.QPushButton(self.AddingProject)
        self.CreateBoard.setGeometry(QtCore.QRect(10, 180, 251, 41))
        self.CreateBoard.setStyleSheet("#CreateBoard{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.CreateBoard.setObjectName("CreateBoard")
        self.BoardTitle_5 = QtWidgets.QLabel(self.AddingProject)
        self.BoardTitle_5.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.BoardTitle_5.setStyleSheet("#BoardTitle_5{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle_5.setObjectName("BoardTitle_5")
        self.dateEdit = QtWidgets.QDateEdit(self.AddingProject)
        self.dateEdit.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.dateEdit.setStyleSheet("#dateEdit { \n"
"}")
        self.dateEdit.setObjectName("dateEdit")
        self.FavoriteProject = QtWidgets.QLabel(self.MainSection)
        self.FavoriteProject.setGeometry(QtCore.QRect(760, 300, 351, 51))
        self.FavoriteProject.setStyleSheet("#FavoriteProject{\n"
"    font: 40px \"Roboto\";\n"
"    color: #0E49B5;\n"
"    font-weight: bold;\n"
"}")
        self.FavoriteProject.setObjectName("FavoriteProject")
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
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 601, 561))
        self.scrollArea_2.setStyleSheet("#scrollArea_2, QScrollArea QWidget{\n"
"    border-radius: 10px;\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #73c2fb, stop:1 #1560bd);\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 601, 561))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.Project1_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.Project1_2.setGeometry(QtCore.QRect(10, 10, 271, 91))
        self.Project1_2.setStyleSheet("#Project1_2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Project1_2.setObjectName("Project1_2")
        self.Project1_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.Project1_6.setGeometry(QtCore.QRect(320, 10, 271, 91))
        self.Project1_6.setStyleSheet("#Project1_6{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding-bottom:15 px;\n"
"   color: #5483B3;\n"
"}")
        self.Project1_6.setObjectName("Project1_6")
        self.label1_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label1_2.setGeometry(QtCore.QRect(20, 75, 201, 16))
        self.label1_2.setStyleSheet("#label1_2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.label1_2.setObjectName("label1_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 10, 41, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 10, 41, 31))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    background-color: #F6F6F6;\n"
"    border-radius: 10px;\n"
"    font-family: \"Roboto\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   color: #5483B3;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.Actions = QtWidgets.QWidget(self.MainSection)
        self.Actions.setGeometry(QtCore.QRect(1410, 440, 271, 171))
        self.Actions.setStyleSheet("#Actions{\n"
"    border: 0.5px solid #052659;\n"
"    background-color: #87ceeb;\n"
"    border-radius: 17px;\n"
"}")
        self.Actions.setObjectName("Actions")
        self.BoardTitle_3 = QtWidgets.QLabel(self.Actions)
        self.BoardTitle_3.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.BoardTitle_3.setStyleSheet("#BoardTitle_3{\n"
"    font-family: Rubik;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.BoardTitle_3.setObjectName("BoardTitle_3")
        self.Favorite = QtWidgets.QPushButton(self.Actions)
        self.Favorite.setGeometry(QtCore.QRect(10, 50, 251, 41))
        self.Favorite.setStyleSheet("#Favorite{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.Favorite.setIcon(icon1)
        self.Favorite.setObjectName("Favorite")
        self.DeleteProject = QtWidgets.QPushButton(self.Actions)
        self.DeleteProject.setGeometry(QtCore.QRect(10, 100, 251, 41))
        self.DeleteProject.setToolTipDuration(-1)
        self.DeleteProject.setStyleSheet("#DeleteProject{\n"
"    font-family: Rubik;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"   color: #052659;\n"
"}")
        self.DeleteProject.setIcon(icon2)
        self.DeleteProject.setObjectName("DeleteProject")
        self.Containerforwords.raise_()
        self.YourProject.raise_()
        self.AddProjectButton.raise_()
        self.BoardName.raise_()
        self.Sorting.raise_()
        self.MainSettings.raise_()
        self.Actions_2.raise_()
        self.namaboard.raise_()
        self.back.raise_()
        self.widget.raise_()
        self.AddingProject.raise_()
        self.FavoriteProject.raise_()
        self.QuickAccess.raise_()
        self.widget_2.raise_()
        self.SortingOption.raise_()
        self.Actions.raise_()
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../if2250-2024-k03-g04-ergo/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon6)
        self.SearchButton.setObjectName("SearchButton")
        self.Searchbar.raise_()
        self.MainSection.raise_()
        self.Navbar.raise_()

        self.retranslateUi(Ergo)
        QtCore.QMetaObject.connectSlotsByName(Ergo)

    def retranslateUi(self, Ergo):
        _translate = QtCore.QCoreApplication.translate
        Ergo.setWindowTitle(_translate("Ergo", "Ergo"))
        self.back_2.setText(_translate("Ergo", "Dashboard"))
        self.BoardName.setText(_translate("Ergo", "Mobile Developement"))
        self.Welcome.setText(_translate("Ergo", "Welcome!"))
        self.WelcomeProject.setText(_translate("Ergo", "This section will show you every projects you have on this board"))
        self.YourProject.setText(_translate("Ergo", "Your Projects"))
        self.AddProjectButton.setText(_translate("Ergo", "+ Add New Project"))
        self.Sorting.setText(_translate("Ergo", "Sort By"))
        self.BoardTitle_4.setText(_translate("Ergo", "Actions"))
        self.Favorite_2.setText(_translate("Ergo", " Add to Favorite"))
        self.DeleteProject_2.setText(_translate("Ergo", " Delete Board"))
        self.namaboard.setText(_translate("Ergo", "> board name"))
        self.back.setText(_translate("Ergo", "Dashboard"))
        self.Sort1.setText(_translate("Ergo", "Sort Descending"))
        self.Sort2.setText(_translate("Ergo", "Sort Ascending"))
        self.Project1.setText(_translate("Ergo", "Build UI"))
        self.label1.setText(_translate("Ergo", "Due to :"))
        self.Project1_3.setText(_translate("Ergo", "Dummy"))
        self.BoardTitle.setText(_translate("Ergo", "Project Title"))
        self.CreateBoard.setText(_translate("Ergo", "Create Project"))
        self.BoardTitle_5.setText(_translate("Ergo", "Deadline"))
        self.FavoriteProject.setText(_translate("Ergo", "Favorite Projects"))
        self.QuickAccess.setText(_translate("Ergo", "Get quick access to your favorite project by giving a star on them"))
        self.Project1_2.setText(_translate("Ergo", "Build UI"))
        self.Project1_6.setText(_translate("Ergo", "Dummy"))
        self.label1_2.setText(_translate("Ergo", "Due to :"))
        self.BoardTitle_3.setText(_translate("Ergo", "Actions"))
        self.Favorite.setText(_translate("Ergo", " Add to Favorite"))
        self.DeleteProject.setText(_translate("Ergo", " Delete Project"))
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
