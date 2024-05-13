import src.uibuilder.board_ui as board_ui
import src.data.db_manager as db_manager
import src.data.databases as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Board(QtWidgets.QMainWindow):
    def __init__(self):
        super(Board,self).__init__()
        self.ui = board_ui.Ui_Ergo()
        self.ui.setupUi(self)
        icon = (QIcon("assets\\logoergo.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database('ergo.db'))

        # ADD BOARD LOGIC
        self.ui.AddingProject.setVisible(False)
        self.ui.SortingOption.setVisible(False)
        self.ui.Actions.setVisible(False)
        self.ui.Actions_2.setVisible(False)

        self.ui.AddProjectButton.clicked.
    
