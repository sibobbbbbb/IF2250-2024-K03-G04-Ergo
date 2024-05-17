import src.data.db_manager as db_manager
import src.data.databases as db
import src.uibuilder.taskUIBaru as task_ui
from PyQt5 import QtWidgets , QtGui , QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Task(QtWidgets.QMainWindow):
    # memunculkan task
    def __init__(self, switch_scene, data):
        super(Task,self).__init__()
        #self.switch_scene = switch_scene
        self.data = data
        self.ui = task_ui.Ui_Ergo()
        self.ui.setupUi(self)
        self.switch_scene = switch_scene
        icon = (QIcon("assets\\ERGO.png"))
        self.setWindowIcon(icon)
        self.dbm = db_manager.DatabaseManager(db.Database())
        self.stack = QtWidgets.QStackedWidget()

        self.ui.AddingNewTask.setVisible(False)
        self.ui.AddNewTaskButton.clicked.connect(self.show_widget)
        self.ui.EditTask.setVisible(False)

        # Display task logic
        self.displayTask(self.dbm.get_tasks_by_project(self.data))
        
        # Sort task logic
        self.ui.Sorting.clicked.connect(self.displaySort)
        self.ui.SortingOption.setVisible(False)
        self.ui.SortAscending.clicked.connect(self.sort_task_A)
        self.ui.SortDescending.clicked.connect(self.sort_task_D)
        
        # Group By Task Logic
        self.ui.Grouping.clicked.connect(self.displayGroup)
        self.ui.GroupingOption.setVisible(False)
        self.ui.GroupByCategory.clicked.connect(self.group_by_task_C)
        self.ui.GroupByStatus.clicked.connect(self.group_by_task_S)
        
        #buat tambah task
        self.ui.AddingNewTask.setVisible(False)
        self.ui.AddNewTaskButton.clicked.connect(self.show_tambahTask)

        #buat edit task
        self.ui.EditTask.setVisible(False)

        #buat tombol cancel
        self.ui.CancelCreationTask.clicked.connect(self.dontshow_tambahTask)
        self.ui.CancelingEdit.clicked.connect(self.dontshow_editTask)

        #buat tombol create ditekan
        self.ui.CreateTask.clicked.connect(self.add_new_task)

        #buat tombol apply ditekan
        self.ui.ApplyChangesButton.clicked.connect(self.edit_selected_task)
        
        # Inisialisasi progress bar
        self.update_progress_bar()
        
        # Search board logic
        self.ui.SearchBoard.textChanged.connect(self.search_bar_task)

        #cari idBoard dari idProject yang dimiliki
        self.idBoard = self.dbm.get_board_by_project(self.data)

        #kalo namaboard dipencet
        self.ui.BackToBoardUpper.setText(f"> {self.dbm.get_board(self.idBoard)[1]}")
        #set agar namaboard geometry sesuai dengan ukuran text nya tetapi tetap di x dan y yang sama
        self.ui.BackToBoardUpper.setGeometry(100, 0, self.ui.BackToBoardUpper.fontMetrics().boundingRect(self.ui.BackToBoardUpper.text()).width(), 31)

        #kalo back dipencet
        # Tambahkan ini di __init__ method
        self.ui.CurrentTaskUpper.setText(f"> {self.dbm.get_projectName_by_id(self.data)}")
        # Dapatkan posisi x dan lebar dari namaboard
        namaboard_x = self.ui.BackToBoardUpper.geometry().x()
        namaboard_width = self.ui.BackToBoardUpper.geometry().width()

        # Hitung posisi x baru untuk namaproject
        namaproject_x = namaboard_x + namaboard_width

        # Set geometry untuk namaproject
        self.ui.CurrentTaskUpper.setGeometry(namaproject_x + 10, 0, self.ui.BackToBoardUpper.fontMetrics().boundingRect(self.ui.BackToBoardUpper.text()).width(), 31)

        self.ui.BackToDashboardUpper.clicked.connect(lambda _, kosong=0 : self.switch_scene(0, kosong))
        self.ui.BackToDashboard.clicked.connect(lambda _, kosong=0 : self.switch_scene(0, kosong))
        self.ui.BackToBoardUpper.clicked.connect(lambda _ : self.switch_scene(1, self.dbm.get_board_by_project(self.data)))
        self.ui.BackToYourBoard.clicked.connect(lambda _ : self.switch_scene(1, self.dbm.get_board_by_project(self.data)))
        # self.ui.BackToYourBoard.setText(f"> {self.dbm.get_board(self.idBoard)[1]}"
        self.ui.TaskNameTitle.setText(f"{self.dbm.get_projectName_by_id(self.data)}")

    def show_tambahTask(self):
        self.ui.AddingNewTask.setVisible(True)
    
    def dontshow_tambahTask(self):
        self.ui.AddingNewTask.setVisible(False)

    def show_editTask(self, event):
        self.ui.EditTask.setVisible(True)
    
    def dontshow_editTask(self):
        self.ui.EditTask.setVisible(False)

    def add_new_task(self):
        #cek apakah textEdit_2 kosong
        if self.ui.inputTasktitle.toPlainText():
            self.dontshow_tambahTask()
            # memasukkan input ke dalam database
            self.ui.AddingNewTask.setVisible(False)
            task_title = self.ui.inputTasktitle.toPlainText()
            deadline = self.ui.dateEditDeadlineInput.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.BoxInputDescription.toPlainText()
            category = self.ui.CategoryInputBox.currentText()
            status = "Not Yet Started"
            new_task = db.Task(self.dbm.getLastIdTask()+1, self.data ,task_title,status ,category, desc,deadline)
            self.dbm.create_task(new_task)
            self.displayTask(self.dbm.get_tasks_by_project(self.data))

    def edit_selected_task(self):
        #cek apakah textEdit_2 kosong
        if self.ui.InputEditTaskBox.toPlainText():
            self.dontshow_editTask()
            task_title = self.ui.InputEditTaskBox.toPlainText()
            deadline = self.ui.DateEditDeadline.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.DescriptionEditBox.toPlainText()
            category = self.ui.CategoryEditComboBox.currentText()
            status = self.ui.StatusComboBox.currentText()
            edited_task = db.Task(int(self.idTask), self.data, task_title, status, category, desc, deadline)
            self.dbm.update_task(edited_task)
            self.displayTask(self.dbm.get_tasks_by_project(self.data))
            self.update_progress_bar()
    
    def displaySort(self):
        self.ui.SortingOption.setVisible(not self.ui.SortingOption.isVisible())        
        
    def sort_task_A(self):
        self.ui.SortingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask))
        
    def sort_task_D(self):
        self.ui.SortingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask, reverse=True))
    
    def displayGroup(self):
        self.ui.GroupingOption.setVisible(not self.ui.GroupingOption.isVisible())
    
    def group_by_task_C(self):
        self.ui.GroupingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        urutan = ["Low", "Medium", "High"]
        grouped_tasks = {kategori: [] for kategori in urutan}
        for task in tasks:
            if task.kategori in grouped_tasks:
                grouped_tasks[task.kategori].append(task)
            
        result = [task for kategori in urutan for task in grouped_tasks[kategori]]
        self.displayTask(result)
            
    def group_by_task_S(self):
        self.ui.GroupingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        urutan = ["Not Yet Started", "On Progress", "Completed"]
        grouped_tasks = {status: [] for status in urutan}
        for task in tasks:
            if task.status in grouped_tasks:
                grouped_tasks[task.status].append(task)
            
        result = [task for status in urutan for task in grouped_tasks[status]]
        self.displayTask(result)
        

    def show_widget(self):
        self.ui.AddingNewTask.setVisible(not self.ui.AddingNewTask.isVisible())

    def show_editTask(self, task_widget ,event):
        self.ui.EditTask.setVisible(not self.ui.EditTask.isVisible())
        self.idTask = task_widget.objectName()  
        task = self.dbm.get_task(int(self.idTask))
        self.ui.InputEditTaskBox.setPlainText(task[2])
        self.ui.DateEditDeadline.setDateTime(QtCore.QDateTime.fromString(task[6], "yyyy-MM-dd hh:mm"))
        self.ui.DescriptionEditBox.setPlainText(task[5])
        self.ui.StatusComboBox.setCurrentText(task[3])
        self.ui.CategoryEditComboBox.setCurrentText(task[4])
        
        
    def displayTask(self, tasks):
        # Bersihkan isi scroll area sebelum menampilkan task baru
        self.clear_layout(self.ui.scrollAreaWidgetContents.layout())

        layout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents.setLayout(layout)

        # Tampilkan setiap task
        for task in tasks:
            self.add_task_to_layout(task, layout)

        # Set minimum height of the scroll area content to allow scrolling
        self.ui.scrollAreaWidgetContents.setMinimumHeight(len(tasks) * 71)  # Adjust height based on task widget height

        self.update_progress_bar()

    def add_task_to_layout(self, task, layout):
        widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        widget.setFixedSize(1101, 71)  # Set the fixed size for each task widget
        widget.setStyleSheet("")
        widget.setObjectName(f"Task{task.idTask}")

        # Menambahkan event handler mouseDoubleClickEvent
        widget.mouseDoubleClickEvent = lambda event: self.show_editTask(widget, event)

        checkBox = QtWidgets.QCheckBox(widget)
        checkBox.setGeometry(QtCore.QRect(10, 25, 21, 24))
        checkBox.setText("")
        checkBox.setObjectName("checkBox")
        checkBox.setChecked(task.status == "Completed")
        checkBox.stateChanged.connect(lambda state: self.update_task_status(task, state))

        task_name = QtWidgets.QLabel(widget)
        task_name.setGeometry(QtCore.QRect(40, 25, 191, 20))
        task_name.setText(task.namaTask)
        task_name.setStyleSheet("#Task1Name{"
                                "    background-color : none;"
                                "    font-family: \"Roboto\";"
                                "    font-size: 15px;"
                                "    font-weight: bold;"
                                "    color: #0E49B5;"
                                "}")
        task_name.setObjectName("TaskName")

        task_status = QtWidgets.QLabel(widget)
        task_status.setGeometry(QtCore.QRect(260, 25, 181, 20))
        task_status.setText(task.status)
        task_status.setStyleSheet("#Task1Status{"
                                "    background-color : none;"
                                "    font-family: \"Roboto\";"
                                "    font-size: 15px;"
                                "    font-weight: bold;"
                                "    color: #0E49B5;"
                                "}")
        task_status.setObjectName("TaskStatus")

        task_category = QtWidgets.QLabel(widget)
        task_category.setGeometry(QtCore.QRect(450, 25, 161, 20))
        task_category.setText(task.kategori)
        task_category.setStyleSheet("#Task1Category{"
                                    "    background-color : none;"
                                    "    font-family: \"Roboto\";"
                                    "    font-size: 15px;"
                                    "    font-weight: bold;"
                                    "    color: #0E49B5;"
                                    "}")
        task_category.setObjectName("TaskCategory")

        task_deadline = QtWidgets.QLabel(widget)
        task_deadline.setGeometry(QtCore.QRect(620, 25, 221, 20))
        task_deadline.setText(task.deadlineTask)
        task_deadline.setStyleSheet("#Task1Deadline{"
                                    "    background-color : none;"
                                    "    font-family: \"Roboto\";"
                                    "    font-size: 15px;"
                                    "    font-weight: bold;"
                                    "    color: #0E49B5;"
                                    "}")
        task_deadline.setObjectName("TaskDeadline")

        task_description = QtWidgets.QTextBrowser(widget)
        task_description.setGeometry(QtCore.QRect(825, 0, 261, 71))
        task_description.setText(task.deskripsi)
        task_description.setStyleSheet("#Task1Description{"
                                    "    background-color : none;"
                                    "    font-family: \"Roboto\";"
                                    "    font-size: 13px;"
                                    "    font-weight: bold;"
                                    "    color: #0E49B5;"
                                    "}")
        task_description.setObjectName("TaskDescription")

        layout.addWidget(widget)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()


    def update_task_status(self, task, state):
        if state == QtCore.Qt.Checked:
            task.status = "Completed"
        else:
            task.status = "Not Yet Started"
        self.dbm.update_task(task)
        self.displayTask(self.dbm.get_tasks_by_project(self.data))
        self.update_progress_bar()

    def update_progress_bar(self):
        tasks = self.dbm.get_tasks_by_project(self.data)
        if tasks:
            completed_tasks = [task for task in tasks if task.status == "Completed"]
            on_progress_tasks = [task for task in tasks if task.status == "On Progress"]
            complete = (len(completed_tasks) / len(tasks)) * 100
            progressing = ((len(on_progress_tasks) / len(tasks)) * 100) // 2
            self.ui.progressBar.setValue(int(complete + progressing))
        else:
            self.ui.progressBar.setValue(0)
            
    def search_bar_task(self):
        search_text = self.ui.lineEdit.text()
        if search_text and not search_text == "Search Your Board":
            tasks = [task for task in self.dbm.get_tasks_by_project(self.data) if search_text.lower() in task.namaTask.lower()] 
            self.displayTask(tasks)
        else:
            self.displayTask(self.dbm.get_tasks_by_project(self.data))
            
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Task()
    window.show()
    sys.exit(app.exec_())