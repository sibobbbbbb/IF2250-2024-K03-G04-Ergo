import src.uibuilder.boardUIBaru as boardUIBaru
import src.data.db_manager as db_manager
import src.data.databases as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from datetime import datetime

class Board(QtWidgets.QMainWindow):
    def __init__(self, switch_scene ,data):
        super(Board,self).__init__()
        self.data = data
        self.ui = boardUIBaru.Ui_Ergo()
        self.switch_scene = switch_scene
        self.ui.setupUi(self)
        icon = (QIcon("img\\logoergo.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database())

        # Set label nama board
        self.ui.BoardName.setText(self.dbm.get_board(self.data)[1])
        self.ui.namaboard.setText("> " + self.dbm.get_board(self.data)[1])
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
        self.ui.back_2.clicked.connect(lambda: self.switch_scene(0, self))  # Modifikasi ini
        
        # DISPLAY PROJECTS LOGIC 
        self.displayProjects(self.dbm.get_projects_by_board(self.data))
        self.displayFavProjects(self.dbm.get_projects_by_board(self.data))

        # SORT PROJECTS LOGIC
        self.ui.Sort2.clicked.connect(self.sort_ascending)
        self.ui.Sort1.clicked.connect(self.sort_descending)
        
        
        
    def sort_ascending(self):
        self.ui.SortingOption.setVisible(False)
        projects = self.dbm.get_projects_by_board(self.data)

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
        projects = self.dbm.get_projects_by_board(self.data)

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

        common_stylesheet = (
        "background-color: #F6F6F6;\n"
        "border-radius: 10px;\n"
        "font-family: \"Roboto\";\n"
        "font-size: 20px;\n"
        "font-weight: bold;\n"
        "color: #5483B3;\n"
    )

        project_container = QtWidgets.QWidget()
        project_layout = QtWidgets.QGridLayout(project_container)

        for i, project in enumerate(projects):
            project_frame = QtWidgets.QFrame()
            project_frame.setGeometry(QtCore.QRect(0, 0, 271, 91))
            project_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            project_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            project_frame.setObjectName(f"Project{i+1}f")

            project_button = QtWidgets.QPushButton(project.namaProject, parent=project_frame)
            project_button.setGeometry(QtCore.QRect(10, 10, 271, 91))
            project_button.setStyleSheet(common_stylesheet)
            project_button.setObjectName(f"ProjectButton{i+1}")
            project_button.clicked.connect(lambda _, project_id=project.idProject: self.switch_scene(2, project_id))

            more_button = QtWidgets.QPushButton(parent=project_frame)
            more_button.setGeometry(QtCore.QRect(240, 10, 41, 31))
            more_button.setStyleSheet(common_stylesheet)
            more_button.setIcon(QtGui.QIcon("img//3dot.png"))
            more_button.setObjectName(f"{project.idProject}")

            label = QtWidgets.QLabel(f"Due to: {project.deadlineProject}", parent=project_frame)
            label.setGeometry(QtCore.QRect(20, 75, 201, 16))
            label.setStyleSheet(
                "background-color: #F6F6F6;\n"
                "border-radius: 10px;\n"
                "font-family: \"Roboto\";\n"
                "font-size: 15px;\n"
                "font-weight: bold;\n"
                "color: #5483B3;\n"
            )
            label.setObjectName(f"Label{i+1}")

            project_layout.addWidget(project_frame, i // 2, i % 2)
            more_button.clicked.connect(self.showActions)

        project_container.setLayout(project_layout)
        self.ui.scrollArea.setWidget(project_container)

    
    def displayFavProjects(self, projects):
        self.clear_fav_project_frames()
        
        common_stylesheet = (
        "background-color: #F6F6F6;\n"
        "border-radius: 10px;\n"
        "font-family: \"Roboto\";\n"
        "font-size: 20px;\n"
        "font-weight: bold;\n"
        "color: #5483B3;\n"
        )
        
        fav_project_container = QtWidgets.QWidget()
        fav_project_layout = QtWidgets.QGridLayout(fav_project_container)

        favProjects = [project for project in projects if project.isFavorite == 1]

        for i, project in enumerate(favProjects):
            fav_project_frame = QtWidgets.QFrame()
            fav_project_frame.setGeometry(QtCore.QRect(0, 0, 271, 91))
            fav_project_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            fav_project_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            fav_project_frame.setObjectName(f"FavProject{i+1}f")

            fav_project_button = QtWidgets.QPushButton(project.namaProject, parent=fav_project_frame)
            fav_project_button.setGeometry(QtCore.QRect(10, 10, 271, 91))
            fav_project_button.setStyleSheet(common_stylesheet)
            fav_project_button.setObjectName("{project.idProject}")
            fav_project_button.clicked.connect(lambda _, project_id=project.idProject: self.switch_scene(2, project_id))

            more_button = QtWidgets.QPushButton(parent=fav_project_frame)
            more_button.setGeometry(QtCore.QRect(240, 10, 41, 31))
            more_button.setStyleSheet(common_stylesheet)
            more_button.setIcon(QtGui.QIcon("img//3dot.png"))
            more_button.setObjectName(f"{project.idProject}")
            more_button.clicked.connect(self.showActions)

            label = QtWidgets.QLabel(f"Due to: {project.deadlineProject}", parent=fav_project_frame)
            label.setGeometry(QtCore.QRect(20, 75, 201, 16))
            label.setStyleSheet(
                "#FavLabel{"
                "    background-color: #F6F6F6;"
                "    border-radius: 10px;"
                "    font-family: \"Roboto\";"
                "    font-size: 15px;"
                "    font-weight: bold;"
                "    color: #5483B3;"
                "}"
            )
            label.setObjectName("FavLabel")

            fav_project_layout.addWidget(fav_project_frame, i // 2, i % 2)

        fav_project_container.setLayout(fav_project_layout)
        self.ui.scrollArea_2.setWidget(fav_project_container)


    def search_project(self):
        search_text = self.ui.SearchBoard.text()
        if search_text and not search_text == "Search Your Board":
            projects = [project for project in self.dbm.get_all_project_by_board(self.data) if search_text.lower() in project.namaProject.lower()] 
            self.displayProjects(projects)
            self.displayFavProjects(projects)
        else:
            self.displayProjects(self.dbm.get_all_project_by_board(self.data))
            self.displayFavProjects(self.dbm.get_all_project_by_board(self.data))

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

    def delete_board(self):
        self.dbm.delete_board(self.data)
        self.ui.Actions_2.setVisible(False)
        self.switch_scene(0,0)
        # kedashboard

    def delete_project(self):
        idProject = self.senderf.objectName()
        self.dbm.delete_project(idProject)
        self.ui.Actions.setVisible(False)
        self.displayProjects(self.dbm.get_projects_by_board(self.data))
        self.displayFavProjects(self.dbm.get_projects_by_board(self.data))

    def favorite_project(self):
        idProject = int(self.senderf.objectName())
        project = self.dbm.get_project(idProject)
        newProject = db.Project(idProject, project[1], project[2], project[3], project[4], 1)
        self.dbm.update_project(newProject)
        self.ui.Actions.setVisible(False)
        self.displayFavProjects(self.dbm.get_projects_by_board(self.data))

    def add_favorite(self):
        ## mengubah board
        board = self.dbm.get_board(self.data)
        newBoard = db.Board(board[0], board[1], 1)
        self.dbm.update_board(newBoard)
        self.ui.Actions_2.setVisible(False)

    def add_new_project(self):
        namaProject = self.ui.inputBoardtitle.text()
        dateProject = self.ui.dateEdit.text()
        newProject = db.Project(self.dbm.getLastIdProject()+1,self.data, namaProject, 0, dateProject, 0)
        self.dbm.create_project(newProject)
        self.ui.AddingProject.setVisible(False)
        self.displayProjects(self.dbm.get_projects_by_board(self.data))

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