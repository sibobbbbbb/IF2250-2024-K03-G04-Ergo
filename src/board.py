import src.uibuilder.board_ui as board_ui
import src.data.db_manager as db_manager
import src.data.databases as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from datetime import datetime

class Board(QtWidgets.QMainWindow):
    def __init__(self, switch_scene):
        super(Board,self).__init__()
        self.ui = board_ui.Ui_Ergo()
        self.switch_scene = switch_scene
        self.ui.setupUi(self)
        icon = (QIcon("img\\logoergo.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database())

        # ADD BOARD LOGIC
        self.ui.AddingProject.setVisible(False)
        self.ui.SortingOption.setVisible(False)
        self.ui.Actions.setVisible(False)
        self.ui.Actions_2.setVisible(False)

        self.ui.AddProjectButton.clicked.connect(self.showAddProject)
        self.ui.Sorting.clicked.connect(self.showSortingOption)
        self.ui.MainSettings.clicked.connect(self.showActions2)
        self.ui.CreateBoard.clicked.connect(self.add_new_project)
        self.ui.Favorite.clicked.connect(self.favorite_project)
        self.ui.DeleteProject.clicked.connect(self.delete_project)
        self.ui.Favorite_2.clicked.connect(self.add_favorite)
        self.ui.DeleteProject_2.clicked.connect(self.delete_board)

        self.ui.SearchBoard.textChanged.connect(self.search_project)
        
        self.ui.back.clicked.connect(lambda: self.switch_scene(0, self))  # Modifikasi ini

        # DISPLAY PROJECTS LOGIC 
        self.displayProjects(self.dbm.get_projects_by_board(1))
        self.displayFavProjects(self.dbm.get_projects_by_board(1))

    # SORT PROJECTS LOGIC
        self.ui.Sort2.clicked.connect(self.sort_ascending)
        self.ui.Sort1.clicked.connect(self.sort_descending)
        
        
    def sort_ascending(self):
        self.ui.SortingOption.setVisible(False)
        projects = self.dbm.get_projects_by_board(1)

        def parse_date(date_string):
            for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
                try:
                    return datetime.strptime(date_string, fmt)
                except ValueError:
                    pass
            raise ValueError(f"time data {date_string} does not match either of the formats %Y-%m-%d or %d/%m/%Y")

        objects_sorted = sorted(projects, key=lambda x: parse_date(x.deadlineProject))
        self.displayProjects(objects_sorted)
        
    def sort_descending(self):
        self.ui.SortingOption.setVisible(False)
        projects = self.dbm.get_projects_by_board(1)

        def parse_date(date_string):
            for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
                try:
                    return datetime.strptime(date_string, fmt)
                except ValueError:
                    pass
            raise ValueError(f"time data {date_string} does not match either of the formats %Y-%m-%d or %d/%m/%Y")

        objects_sorted = sorted(projects, key=lambda x: parse_date(x.deadlineProject), reverse=True)
        self.displayProjects(objects_sorted)

    def displayProjects(self, projects):
        self.clear_project_frames()

        project_container = QtWidgets.QWidget()
        project_layout = QtWidgets.QGridLayout(project_container)
        
        for i, project in enumerate(projects):
            project_frame = QtWidgets.QFrame()
            project_frame.setGeometry(QtCore.QRect(0, 0, 241, 81))
            project_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            project_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            project_frame.setObjectName(f"Project{i+1}f")
            
            project_button = QtWidgets.QPushButton(project.namaProject, parent=project_frame)
            project_button.setGeometry(QtCore.QRect(10, 0, 231, 71))
            project_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 20px;"
                "    font-weight: bold;"
                "    padding-bottom:15px;"
                "    color: #5483B3;"
                "}"
            )
            project_button.setObjectName(f"Project{project.idProject}")
            project_button.clicked.connect(self.switch_scene, 2)
            
            more_button = QtWidgets.QPushButton(parent=project_frame)
            more_button.setGeometry(QtCore.QRect(200, 0, 41, 31))
            more_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 20px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            more_button.setIcon(QtGui.QIcon("img//3dot.png"))
            more_button.setObjectName(f"{project.idProject}")

            label = QtWidgets.QLabel(f"Due to: {project.deadlineProject}", parent=project_frame)
            label.setGeometry(QtCore.QRect(20, 40, 201, 20))
            label.setStyleSheet(
                "QLabel{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 15px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            label.setObjectName(f"label{i+1}")

            project_layout.addWidget(project_frame, i // 3, i % 3)
            more_button.clicked.connect(self.showActions)

        project_container.setLayout(project_layout)
        self.ui.scrollArea.setWidget(project_container)
    
    def displayFavProjects(self, projects):
        self.clear_fav_project_frames()

        fav_project_container = QtWidgets.QWidget()
        fav_project_layout = QtWidgets.QGridLayout(fav_project_container)
        
        favProject = []
        for project in projects:
            if project.isFavorite == 1:
                favProject.append(project)
        
        for i, project in enumerate(favProject):
            fav_project_frame = QtWidgets.QFrame()
            fav_project_frame.setGeometry(QtCore.QRect(0, 0, 241, 81))
            fav_project_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            fav_project_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            fav_project_frame.setObjectName(f"Project{i+1}f")
            
            fav_project_button = QtWidgets.QPushButton(project.namaProject, parent=fav_project_frame)
            fav_project_button.setGeometry(QtCore.QRect(10, 0, 231, 71))
            fav_project_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 20px;"
                "    font-weight: bold;"
                "    padding-bottom:15px;"
                "    color: #5483B3;"
                "}"
            )
            fav_project_button.setObjectName(f"Projectf{project.idProject}")
            
            
            more_button = QtWidgets.QPushButton(parent=fav_project_frame)
            more_button.setGeometry(QtCore.QRect(200, 0, 41, 31))
            more_button.setStyleSheet(
                "QPushButton{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 20px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            more_button.setIcon(QtGui.QIcon("img//3dot.png"))
            more_button.setObjectName(f"MoreButton{project.idProject}")

            label = QtWidgets.QLabel(f"Due to: {project.deadlineProject}", parent=fav_project_frame)
            label.setGeometry(QtCore.QRect(20, 40, 201, 20))
            label.setStyleSheet(
                "QLabel{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 15px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            label.setObjectName(f"label{i+1}")

            fav_project_layout.addWidget(fav_project_frame, i // 3, i % 3)

        fav_project_container.setLayout(fav_project_layout)
        self.ui.scrollArea_2.setWidget(fav_project_container)


    def search_project(self):
        search_text = self.ui.SearchBoard.text()
        if search_text and not search_text == "Search Your Board":
            projects = [project for project in self.dbm.get_all_projects() if search_text.lower() in project.namaProject.lower()] 
            self.displayProjects(projects)
            self.displayFavProjects(projects)
        else:
            self.displayProjects(self.dbm.get_all_projects())
            self.displayFavProjects(self.dbm.get_all_projects())

    def clear_fav_project_frames(self):
        contents = self.ui.scrollArea_2.widget()
        if contents:
            for frame in contents.findChildren(QtWidgets.QFrame):
                frame.deleteLater()

    def clear_project_frames(self):
        contents = self.ui.scrollArea.widget()
        if contents:
            for frame in contents.findChildren(QtWidgets.QFrame):
                frame.deleteLater()

    def back_to_dashboard(self):
        ## back to dashboard
        return

    def delete_board(self):
        self.dbm.delete_board(self.dbm.get_board().idBoard)
        self.back_to_dashboard()
        # kedashboard

    def delete_project(self):
        idProject = self.senderf.objectName()
        self.dbm.delete_project(idProject)
        self.ui.Actions.setVisible(False)
        self.displayProjects(self.dbm.get_projects_by_board(1))
        self.displayFavProjects(self.dbm.get_projects_by_board(1))

    def favorite_project(self):
        idProject = int(self.senderf.objectName())
        project = self.dbm.get_project(idProject)
        newProject = db.Project(idProject, project[1], project[2], project[3], project[4], 1)
        self.dbm.update_project(newProject)
        self.ui.Actions.setVisible(False)
        self.displayFavProjects(self.dbm.get_projects_by_board(1))

    def add_favorite(self):
        ## mengubah board
        newBoard = db.Board(self.dbm.get_board().idBoard, self.dbm.get_board().namaBoard, 1)
        self.dbm.update_board(newBoard)

    def add_new_project(self):
        namaProject = self.ui.inputBoardtitle.text()
        dateProject = self.ui.dateEdit.text()
        newProject = db.Project(self.dbm.getLastIdProject()+1,1, namaProject, 0, dateProject, 0)
        self.dbm.create_project(newProject)
        self.ui.AddingProject.setVisible(False)
        self.displayProjects(self.dbm.get_projects_by_board(1))

    def showAddProject(self):
        self.ui.AddingProject.setVisible(not self.ui.AddingProject.isVisible())
        self.ui.AddingProject.raise_()

    def showSortingOption(self):
        self.ui.SortingOption.setVisible(not self.ui.SortingOption.isVisible())
        self.ui.SortingOption.raise_()
    
    def showActions(self):
        self.senderf = self.sender()
        self.ui.Actions.setVisible(not self.ui.Actions.isVisible())
        self.ui.Actions.raise_()  

    def showActions2(self):
        self.ui.Actions_2.setVisible(not self.ui.Actions_2.isVisible())
        self.ui.Actions_2.raise_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Board()
    window.show()
    sys.exit(app.exec_())