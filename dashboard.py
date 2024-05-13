import src.uibuilder.full as full
import src.data.db_manager as db_manager
import src.data.databases as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dashboard,self).__init__()
        self.ui = full.Ui_Ergo()
        self.ui.setupUi(self)
        icon = (QIcon("assets\\ERGO.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database('ergo.db'))
        
        # ADD BOARD LOGIC
        self.ui.AddingBoard.setVisible(False)
        self.ui.AddBoardButton.clicked.connect(self.show_adding_board)
        self.ui.CreateBoard.clicked.connect(self.add_new_board)
        
        # DISPLAY BOARDS LOGIC
        self.displayBoards()

        # DISPLAY FAV BOARDS LOGIC
        self.displayFavBoards()

    def displayBoards(self):
        boards = self.dbm.get_all_boards()
        self.clear_board_buttons()

        board_container = QtWidgets.QWidget()
        board_layout = QtWidgets.QGridLayout(board_container)

        for i, board in enumerate(boards):
            board_button = QtWidgets.QPushButton(board.namaBoard)
            board_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border: 2px solid #9FB0CC;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 10px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            board_button.setMinimumSize(QtCore.QSize(221, 61))
            row = i // 3
            col = i % 3
            board_layout.addWidget(board_button, row, col)
        
        self.ui.ContainerForBoards.setWidget(board_container)
        
    def displayFavBoards(self):
        boards = self.dbm.get_all_boards()
        self.clear_fav_board_buttons()

        fav_board_container = QtWidgets.QWidget()
        fav_board_layout = QtWidgets.QGridLayout(fav_board_container)

        favBoards = []
        for board in boards:
            if board.isFavorite == 1:
                favBoards.append(board)
 
        for i, board in enumerate(favBoards):
            fav_board_button = QtWidgets.QPushButton(board.namaBoard)
            fav_board_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border: 2px solid #9FB0CC;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 10px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            fav_board_button.setMinimumSize(QtCore.QSize(221, 61))
            row = i // 3
            col = i % 3
            fav_board_layout.addWidget(fav_board_button, row, col)
        
        self.ui.ContainerForBoards_2.setWidget(fav_board_container)

    def clear_board_buttons(self):
        contents = self.ui.ContainerForBoards.widget()
        if contents:
            for button in contents.findChildren(QtWidgets.QPushButton):
                button.deleteLater()
    
    def clear_fav_board_buttons(self):
        contents = self.ui.ContainerForBoards_2.widget()
        if contents:
            for button in contents.findChildren(QtWidgets.QPushButton):
                button.deleteLater()

    def show_adding_board(self): 
        self.ui.AddingBoard.setVisible(not self.ui.AddingBoard.isVisible())
        self.ui.AddingBoard.raise_()

    def add_new_board(self):
        board_title = self.ui.inputBoardtitle.text()
        new_board = db.Board(self.dbm.getLastIdBoard()+1, board_title, 0)
        if board_title and not self.dbm.isInDatabase(board_title):
            self.dbm.create_board(new_board)
            self.ui.AddingBoard.setVisible(False)
            self.displayBoards()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
