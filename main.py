import src.dashboard as dashboard
import src.board as board
import src.task as task
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ergo App")
        self.setGeometry(100, 100, 800, 600)

        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)
        
        icon = (QIcon("img\\logoergo.png")) 
        self.setWindowIcon(icon)

        self.data = None
        
        self.dashboard_scene = dashboard.Dashboard(self.switch_scene)
        self.board_scene = None 
        self.task_scene = None
        self.stack.addWidget(self.dashboard_scene)

    def switch_scene(self, index, data):
        self.data = data
        if index == 0:
            self.stack.removeWidget(self.board_scene)
            self.stack.removeWidget(self.task_scene)
        if index == 1:
            if self.board_scene is not None:
                self.stack.removeWidget(self.board_scene)
            self.board_scene = board.Board(self.switch_scene, self.data)
            self.stack.addWidget(self.board_scene)
        elif index == 2:
            if self.task_scene is not None:
                self.stack.removeWidget(self.task_scene)
            self.task_scene = task.Task(self.switch_scene, self.data)
            self.stack.addWidget(self.task_scene)
        
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())