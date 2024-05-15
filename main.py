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

        self.dashboard_scene = dashboard.Dashboard(self.switch_scene)
        self.project_scene = board.Board(self.switch_scene)
        self.task_scene = task.Task(self.switch_scene)

        self.stack.addWidget(self.dashboard_scene)
        self.stack.addWidget(self.project_scene)
        self.stack.addWidget(self.task_scene)

    def switch_scene(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())