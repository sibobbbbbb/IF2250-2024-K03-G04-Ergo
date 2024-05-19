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

        self.ui.ContainerForSingleTask.setVisible(False)
        self.ui.ContainerForSingleTask_2.setVisible(False)

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
        self.ui.BackToBoardUpper.setGeometry(101, 5, self.ui.BackToBoardUpper.fontMetrics().boundingRect(self.ui.BackToBoardUpper.text()).width(), 21)

        #kalo back dipencet
        # Tambahkan ini di __init__ method
        self.ui.CurrentTaskUpper.setText(f"> {self.dbm.get_projectName_by_id(self.data)}")
        # Dapatkan posisi x dan lebar dari namaboard
        namaboard_x = self.ui.BackToBoardUpper.geometry().x()
        namaboard_width = self.ui.BackToBoardUpper.geometry().width()

        # Hitung posisi x baru untuk namaproject
        namaproject_x = namaboard_x + namaboard_width

        # Set geometry untuk namaproject
        self.ui.CurrentTaskUpper.setGeometry(namaproject_x + 10, 5, self.ui.BackToBoardUpper.fontMetrics().boundingRect(self.ui.BackToBoardUpper.text()).width(), 21)

        self.ui.BackToDashboardUpper.clicked.connect(lambda _, kosong=0 : self.switch_scene(0, kosong))
        self.ui.BackToDashboard.clicked.connect(lambda _, kosong=0 : self.switch_scene(0, kosong))
        self.ui.BackToBoardUpper.clicked.connect(lambda _ : self.switch_scene(1, self.dbm.get_board_by_project(self.data)))
        self.ui.BackToYourBoard.clicked.connect(lambda _ : self.switch_scene(1, self.dbm.get_board_by_project(self.data)))
        # self.ui.BackToYourBoard.setText(f"> {self.dbm.get_board(self.idBoard)[1]}"
        self.ui.TaskNameTitle.setText(f"{self.dbm.get_projectName_by_id(self.data)}")

        # ADD PROJECT BUTTON STYLE
        self.is_AddTaskbutton_clicked = False
        self.ui.AddNewTaskButton.clicked.connect(self.toggle_AddNewTaskButton_style)
        
        # SORT PROJECT BUTTON STYLE
        self.is_Sortbutton_clicked = False
        self.ui.Sorting.clicked.connect(self.toggle_Sortbutton_style)

        # GROUP PROJECT BUTTON STYLE
        self.is_Groupbutton_clicked = False
        self.ui.Grouping.clicked.connect(self.toggle_Groupbutton_style)

    def check_progress_bar(self):
        if self.ui.progressBar.value() == 100:
            self.ui.SemangatTitle.setText("Good Job! You've finished all your tasks! XD <3")
        #jika belum 100% tampilkan "Keep it up, you're almost there :D"
        else:
            self.ui.SemangatTitle.setText("Keep it up, you're almost there :D")

    def show_tambahTask(self):
        self.ui.AddingNewTask.setVisible(True)
    
    def dontshow_tambahTask(self):
        self.ui.AddingNewTask.setVisible(False)
        if self.is_AddTaskbutton_clicked:
                self.reset_AddTaskbutton_style()
                self.is_AddTaskbutton_clicked = False
    
    def dontshow_editTask(self):
        self.ui.EditTask.setVisible(False)

    def add_new_task(self):
        #cek apakah textEdit_2 kosong
        if self.ui.inputTasktitle.text() == "":
            self.ui.inputTasktitle.setPlaceholderText("Task title cannot be empty")
        else:
            self.dontshow_tambahTask()
            # memasukkan input ke dalam database
            self.ui.AddingNewTask.setVisible(False)
            task_title = self.ui.inputTasktitle.text()
            deadline = self.ui.dateEditDeadlineInput.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.BoxInputDescription.toPlainText()
            category = self.ui.CategoryInputBox.currentText()
            status = "Not Yet Started"
            new_task = db.Task(self.dbm.getLastIdTask()+1, self.data ,task_title,status ,category, desc,deadline)
            self.dbm.create_task(new_task)
            self.displayTask(self.dbm.get_tasks_by_project(self.data))
            self.check_progress_bar()
            if self.is_AddTaskbutton_clicked:
                self.reset_AddTaskbutton_style()
                self.is_AddTaskbutton_clicked = False

    def edit_selected_task(self):
    # cek apakah InputEditTaskBox kosong
        if self.ui.InputEditTaskBox.text() == "":
            self.ui.InputEditTaskBox.setPlaceholderText("Task title cannot be empty")
        else:
            self.dontshow_editTask()
            task_title = self.ui.InputEditTaskBox.text()
            deadline = self.ui.DateEditDeadline.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.DescriptionEditBox.toPlainText()
            category = self.ui.CategoryEditComboBox.currentText()
            status = self.ui.StatusComboBox.currentText()

            # Pastikan self.idTask tidak None sebelum melanjutkan
            if self.idTask is not None:
                edited_task = db.Task(self.idTask, self.data, task_title, status, category, desc, deadline)
                self.dbm.update_task(edited_task)
                self.displayTask(self.dbm.get_tasks_by_project(self.data))
                self.update_progress_bar()
                self.check_progress_bar()
            else:
                print("Error: idTask is not set.")

    
    def displaySort(self):
        self.ui.SortingOption.setVisible(not self.ui.SortingOption.isVisible())        
        
    def sort_task_A(self):
        self.ui.SortingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask))
        if self.is_Sortbutton_clicked:
            self.reset_Sortbutton_style()
            self.is_Sortbutton_clicked = False
        
    def sort_task_D(self):
        self.ui.SortingOption.setVisible(False)
        tasks = self.dbm.get_tasks_by_project(self.data)
        self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask, reverse=True))
        if self.is_Sortbutton_clicked:
            self.reset_Sortbutton_style()
            self.is_Sortbutton_clicked = False
        
    
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
        if self.is_Groupbutton_clicked:
            self.reset_Groupbutton_style()
            self.is_Groupbutton_clicked = False
            
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
        if self.is_Groupbutton_clicked:
            self.reset_Groupbutton_style()
            self.is_Groupbutton_clicked = False
        

    def show_widget(self):
        self.ui.AddingNewTask.setVisible(not self.ui.AddingNewTask.isVisible())

    def show_editTask(self, widget, event):
        self.ui.EditTask.setVisible(True)

        # Ambil ID tugas dari nama objek widget
        task_id_str = widget.objectName() 
        self.idTask = task_id_str
        # Konversi ID tugas ke integer
        task_id = int(self.idTask)

        # Ambil tugas dari database
        task = self.dbm.get_task(task_id)

        # Set teks untuk InputEditTaskBox
        self.ui.InputEditTaskBox.setText(task[2])

        # Set tanggal dan waktu untuk DateEditDeadline
        self.ui.DateEditDeadline.setDateTime(QtCore.QDateTime.fromString(task[6], "yyyy-MM-dd hh:mm:ss"))

        # Set teks untuk DescriptionEditBox
        self.ui.DescriptionEditBox.setPlainText(task[5])

        # Set teks untuk StatusComboBox
        self.ui.StatusComboBox.setCurrentText(task[3])

        # Set teks untuk CategoryEditComboBox
        self.ui.CategoryEditComboBox.setCurrentText(task[4])
        
    def displayTask(self, tasks):
        # Bersihkan isi scroll area sebelum menampilkan task baru
        self.clear_layout(self.ui.scrollAreaWidgetContents.layout())

        if self.ui.scrollAreaWidgetContents.layout() is None:
            layout = QtWidgets.QVBoxLayout()  # Membuat objek QVBoxLayout

            # Tambahkan widget Anda ke layout
            for task in tasks:
                task_widget = self.add_task_to_layout(task)
                layout.addWidget(task_widget)

            # Set layout ke scrollAreaWidgetContents
            self.ui.scrollAreaWidgetContents.setLayout(layout)
        else:
            layout = self.ui.scrollAreaWidgetContents.layout()
            for task in tasks:
                task_widget = self.add_task_to_layout(task)
                layout.addWidget(task_widget)

        # Set minimum height of the scroll area content to allow scrolling
        self.ui.scrollAreaWidgetContents.setMinimumHeight(len(tasks) * 71)  # Adjust height based on task widget height

        self.update_progress_bar()

    def add_task_to_layout(self, task):
        widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        widget.setFixedSize(1101, 71)
        widget.setObjectName(f"{task.idTask}")

        # Menambahkan event handler mouseDoubleClickEvent
        widget.mouseDoubleClickEvent = lambda event: self.show_editTask(widget, event)

        checkBox = QtWidgets.QCheckBox(widget)
        checkBox.setGeometry(QtCore.QRect(10, 25, 21, 24))
        checkBox.setText("")
        checkBox.setObjectName(f"checkBoxTask{task.idTask}")
        checkBox.setChecked(task.status == "Completed")
        checkBox.stateChanged.connect(lambda state, t=task: self.update_task_status(t, state))

        task_name = QtWidgets.QLabel(widget)
        task_name.setGeometry(QtCore.QRect(40, 25, 191, 20))
        task_name.setText(task.namaTask)
        task_name.setObjectName(f"TaskName{task.idTask}")

        task_status = QtWidgets.QLabel(widget)
        task_status.setGeometry(QtCore.QRect(260, 25, 181, 20))
        task_status.setText(task.status)
        task_status.setObjectName(f"TaskStatus{task.idTask}")

        task_category = QtWidgets.QLabel(widget)
        task_category.setGeometry(QtCore.QRect(450, 25, 161, 20))
        task_category.setText(task.kategori)
        task_category.setObjectName(f"TaskCategory{task.idTask}")

        task_deadline = QtWidgets.QLabel(widget)
        task_deadline.setGeometry(QtCore.QRect(620, 25, 221, 20))
        task_deadline.setText(task.deadlineTask)
        task_deadline.setObjectName(f"TaskDeadline{task.idTask}")

        task_description = QtWidgets.QTextBrowser(widget)
        task_description.setGeometry(QtCore.QRect(825, 0, 261, 71))
        task_description.setText(task.deskripsi)
        task_description.setObjectName(f"TaskDescription{task.idTask}")

        # Terapkan stylesheet ke widget secara keseluruhan
        widget.setStyleSheet(f"""
            QWidget#{task.idTask} {{
                background-color: #FFFFFF;
            }}
            QLabel#TaskName{task.idTask}, QLabel#TaskStatus{task.idTask}, QLabel#TaskCategory{task.idTask}, QLabel#TaskDeadline{task.idTask}, QTextBrowser#TaskDescription{task.idTask} {{
                background-color: none;
                font-family: "Roboto";
                font-size: 15px;
                font-weight: bold;
                color: #0E49B5;
            }}
            QTextBrowser#TaskDescription{task.idTask} {{
                font-size: 13px;
            }}
            QCheckBox#checkBoxTask{task.idTask} {{
                background-color : none;
            }}
        """)

        return widget

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
        self.update_progress_bar()
        
        # Update the status label directly
        task_widget = self.ui.scrollAreaWidgetContents.findChild(QtWidgets.QWidget, f"Task{task.idTask}")
        if task_widget:
            task_status_label = task_widget.findChild(QtWidgets.QLabel, "Task1Status")
            self.check_progress_bar()
            if task_status_label:
                task_status_label.setText(task.status)
                self.check_progress_bar()


    def update_progress_bar(self):
        tasks = self.dbm.get_tasks_by_project(self.data)
        if tasks:
            completed_tasks = [task for task in tasks if task.status == "Completed"]
            on_progress_tasks = [task for task in tasks if task.status == "On Progress"]
            complete = (len(completed_tasks) / len(tasks)) * 100
            progressing = ((len(on_progress_tasks) / len(tasks)) * 100) // 2
            self.ui.progressBar.setValue(int(complete + progressing))
            self.check_progress_bar()
        else:
            self.ui.progressBar.setValue(0)
            self.check_progress_bar()
        

            
    def search_bar_task(self):
        search_text = self.ui.SearchBoard.text()
        if search_text and not search_text == "Search Your Board":
            tasks = [task for task in self.dbm.get_tasks_by_project(self.data) if search_text.lower() in task.namaTask.lower()] 
            self.displayTask(tasks)
        else:
            self.displayTask(self.dbm.get_tasks_by_project(self.data))

    def change_Sortbutton_style(self):
        self.ui.Sorting.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #1560bd;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #FFFFFF;"
        )

    def reset_Sortbutton_style(self):
        self.ui.Sorting.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #FFFFFF;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #0197F6;"
        )

    def toggle_Sortbutton_style(self):
        if self.is_Sortbutton_clicked:
            self.reset_Sortbutton_style()
        else:
            self.change_Sortbutton_style()
        self.is_Sortbutton_clicked = not self.is_Sortbutton_clicked

    def change_Groupbutton_style(self):
        self.ui.Grouping.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #1560bd;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #FFFFFF;"
        )

    def reset_Groupbutton_style(self):
        self.ui.Grouping.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #FFFFFF;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #0197F6;"
        )

    def toggle_Groupbutton_style(self):
        if self.is_Groupbutton_clicked:
            self.reset_Groupbutton_style()
        else:
            self.change_Groupbutton_style()
        self.is_Groupbutton_clicked = not self.is_Groupbutton_clicked

    def change_AddTaskbutton_style(self):
        self.ui.AddNewTaskButton.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #1560bd;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #FFFFFF;"
        )

    def reset_AddTaskbutton_style(self):
        self.ui.AddNewTaskButton.setStyleSheet(
            "border: 1px solid #0047ab;"
            "background-color: #FFFFFF;"
            "border-radius: 10px;"
            "font-family: \"Roboto\";"
            "font-size: 15px;"
            "font-weight: bold;"
            "color: #0197F6;"
        )

    def toggle_AddNewTaskButton_style(self):
        if self.is_AddTaskbutton_clicked:
            self.reset_AddTaskbutton_style()
        else:
            self.change_AddTaskbutton_style()
        self.is_AddTaskbutton_clicked = not self.is_AddTaskbutton_clicked
            
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Task()
    window.show()
    sys.exit(app.exec_())