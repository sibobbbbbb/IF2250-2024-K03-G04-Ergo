import src.uibuilder.new as new
import src.data.db_manager as db_manager
import src.data.databases as db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dashboard,self).__init__()
        self.ui = new.Ui_Ergo()
        self.ui.setupUi(self)
        icon = (QIcon("assets\\ERGO.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database('ergo.db'))
        
        # ADD BOARD LOGIC
        self.ui.AddingBoard.setVisible(False)
        self.ui.pushButton.clicked.connect(self.show_adding_board)
        self.ui.CreateBoard.clicked.connect(self.add_new_board)

    def show_adding_board(self): 
        self.ui.AddingBoard.setVisible(not self.ui.AddingBoard.isVisible())

    def add_new_board(self):
        board_title = self.ui.inputBoardtitle.text()
        new_board = db.Board(self.dbm.getLastIdBoard()+1, board_title, 0)
        if board_title and not self.dbm.isInDatabase(board_title):
            self.dbm.create_board(new_board)
            self.ui.AddingBoard.setVisible(False)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
