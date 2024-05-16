import src.data.db_manager as db_manager
import src.data.databases as db
import src.uibuilder.newtask as task_ui
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

        self.ui.tambahTask.setVisible(False)
        self.ui.pushButton.clicked.connect(self.show_widget)
        self.ui.editTask.setVisible(False)

        # Display task logic
        self.displayTask(self.dbm.get_tasks_by_project(self.data))
        
        # Sort task logic
        self.ui.comboBox_2.currentIndexChanged.connect(self.sort_task)
        
        # Group By Task Logic
        self.ui.comboBox.currentIndexChanged.connect(self.group_by_task)
        
        #buat tambah task
        self.ui.tambahTask.setVisible(False)
        self.ui.pushButton.clicked.connect(self.show_tambahTask)

        #buat edit task
        self.ui.editTask.setVisible(False)

        #buat tombol cancel
        self.ui.pushButton_4.clicked.connect(self.dontshow_tambahTask)
        self.ui.pushButton_6.clicked.connect(self.dontshow_editTask)

        #buat label "task name required"
        self.ui.label_25.setVisible(False)
        self.ui.label_31.setVisible(False)

        #buat tombol create ditekan
        self.ui.pushButton_2.clicked.connect(self.add_new_task)

        #buat tombol apply ditekan
        self.ui.pushButton_5.clicked.connect(self.edit_selected_task)
        
        # Inisialisasi progress bar
        self.update_progress_bar()
        
        # Search board logic
        self.ui.lineEdit.textChanged.connect(self.search_bar_task)

        #cari idBoard dari idProject yang dimiliki
        self.idBoard = self.dbm.get_board_by_project(self.data)

        #kalo namaboard dipencet
        self.ui.namaboard.setText(f"> {self.dbm.get_board(self.idBoard)[1]}")
        #set agar namaboard geometry sesuai dengan ukuran text nya tetapi tetap di x dan y yang sama
        self.ui.namaboard.setGeometry(100, 0, self.ui.namaboard.fontMetrics().boundingRect(self.ui.namaboard.text()).width(), 31)

        
        
        #kalo back dipencet
        # Tambahkan ini di __init__ method
        self.ui.namaproject.setText(f"> {self.dbm.get_projectName_by_id(self.data)}")
        # Dapatkan posisi x dan lebar dari namaboard
        namaboard_x = self.ui.namaboard.geometry().x()
        namaboard_width = self.ui.namaboard.geometry().width()

        # Hitung posisi x baru untuk namaproject
        namaproject_x = namaboard_x + namaboard_width

        # Set geometry untuk namaproject
        self.ui.namaproject.setGeometry(namaproject_x + 10, 0, self.ui.namaboard.fontMetrics().boundingRect(self.ui.namaboard.text()).width(), 31)

        self.ui.back.clicked.connect(lambda _, kosong=0 : self.switch_scene(0, kosong))
        self.ui.namaboard.clicked.connect(lambda _ : self.switch_scene(1, self.dbm.get_board_by_project(self.data)))

        self.ui.Greetings.setText(f"{self.dbm.get_projectName_by_id(self.data)}")

    def show_tambahTask(self):
        self.ui.tambahTask.setVisible(True)
    
    def dontshow_tambahTask(self):
        self.ui.tambahTask.setVisible(False)

    def show_editTask(self, event):
        self.ui.editTask.setVisible(True)
    
    def dontshow_editTask(self):
        self.ui.editTask.setVisible(False)

    def add_new_task(self):
        #cek apakah textEdit_2 kosong
        if self.ui.textEdit.toPlainText() == "":
            self.ui.label_25.setVisible(True)
        else:
            self.dontshow_tambahTask()
            # memasukkan input ke dalam database
            self.ui.tambahTask.setVisible(False)
            task_title = self.ui.textEdit.toPlainText()
            deadline = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.textEdit_2.toPlainText()
            category = self.ui.comboBox_3.currentText()
            status = "Not Yet Started"
            new_task = db.Task(self.dbm.getLastIdTask()+1, self.data ,task_title,status ,category, desc,deadline)
            self.dbm.create_task(new_task)
            self.displayTask(self.dbm.get_tasks_by_project(self.data))

    def edit_selected_task(self):
        #cek apakah textEdit_2 kosong
        if self.ui.textEdit_3.toPlainText() == "":
            self.ui.label_31.setVisible(True)
        else:
            self.dontshow_editTask()
            task_title = self.ui.textEdit_3.toPlainText()
            deadline = self.ui.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm")
            desc = self.ui.textEdit_4.toPlainText()
            category = self.ui.comboBox_4.currentText()
            status = self.ui.comboBox_5.currentText()
            edited_task = db.Task(int(self.idTask), self.data, task_title, status, category, desc, deadline)
            self.dbm.update_task(edited_task)
            self.displayTask(self.dbm.get_tasks_by_project(self.data))
            self.update_progress_bar()
        
    def sort_task(self):
        sort_by = self.ui.comboBox_2.currentText()
        tasks = self.dbm.get_tasks_by_project(self.data)
        if sort_by == "Ascending":
            self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask))
        else:
            self.displayTask(sorted(tasks, key=lambda x: x.deadlineTask, reverse=True))
    
    def group_by_task(self):
        group_by = self.ui.comboBox.currentText()
        tasks = self.dbm.get_tasks_by_project(self.data)
        if group_by == "Category":
            urutan = ["Low", "Medium", "High"]
            grouped_tasks = {kategori: [] for kategori in urutan}
            for task in tasks:
                if task.kategori in grouped_tasks:
                    grouped_tasks[task.kategori].append(task)
                
            result = [task for kategori in urutan for task in grouped_tasks[kategori]]
        else :
            urutan = ["Not Yet Started", "On Progress", "Completed"]
            grouped_tasks = {status: [] for status in urutan}
            for task in tasks:
                if task.status in grouped_tasks:
                    grouped_tasks[task.status].append(task)
                
            result = [task for status in urutan for task in grouped_tasks[status]]
        
        self.displayTask(result)

    def show_widget(self):
        self.ui.tambahTask.setVisible(not self.ui.tambahTask.isVisible())

    def show_editTask(self, task_widget ,event):
        self.ui.editTask.setVisible(not self.ui.editTask.isVisible())
        self.idTask = task_widget.objectName()  
        task = self.dbm.get_task(int(self.idTask))
        self.ui.textEdit_3.setPlainText(task[2])
        self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.fromString(task[6], "yyyy-MM-dd hh:mm"))
        self.ui.textEdit_4.setPlainText(task[5])
        self.ui.comboBox_5.setCurrentText(task[3])
        self.ui.comboBox_4.setCurrentText(task[4])
        
        
    def displayTask(self, tasks):
        # Bersihkan isi scroll area sebelum menampilkan task baru
        self.clear_layout(self.ui.verticalLayout)

        # Tampilkan setiap task
        for task in tasks:
            self.add_task_to_layout(task)

        # Set minimum height of the scroll area content to allow scrolling
        self.ui.scrollAreaWidgetContents.setMinimumHeight(len(tasks) * 144)

        self.update_progress_bar()

    def add_task_to_layout(self, task):
        widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        widget.setFixedSize(1655, 144)  # Set the fixed size for each task widget
        widget.setStyleSheet("")
        widget.setObjectName(f"{task.idTask}")

        # Menambahkan event handler mouseDoubleClickEvent
        widget.mouseDoubleClickEvent = lambda event: self.show_editTask(widget, event)

        horizontalLayout = QtWidgets.QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")

        checkBox = QtWidgets.QCheckBox(widget)
        checkBox.setText("")
        checkBox.setObjectName("checkBox")
        checkBox.setChecked(task.status == "Completed")
        checkBox.stateChanged.connect(lambda state: self.update_task_status(task, state))
        horizontalLayout.addWidget(checkBox)

        label_10 = QtWidgets.QLabel(widget)
        label_10.setObjectName("label_10")
        label_10.setText(task.namaTask)  # Set nama task
        label_10.setFont(QtGui.QFont("Arial", 12))  
        horizontalLayout.addWidget(label_10)

        spacerItem = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)

        label_11 = QtWidgets.QLabel(widget)
        label_11.setObjectName("label_11")
        label_11.setText(task.status)  # Set status task
        label_11.setFont(QtGui.QFont("Arial", 12))  
        horizontalLayout.addWidget(label_11)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem1)

        label_12 = QtWidgets.QLabel(widget)
        label_12.setObjectName("label_12")
        label_12.setText(task.kategori)  # Set kategori task
        label_12.setFont(QtGui.QFont("Arial", 12))
        horizontalLayout.addWidget(label_12)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem2)

        label_13 = QtWidgets.QLabel(widget)
        label_13.setObjectName("label_13")
        label_13.setText(task.deadlineTask)  # Set deadline task
        label_13.setFont(QtGui.QFont("Arial", 12))
        horizontalLayout.addWidget(label_13)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem3)

        label_14 = QtWidgets.QLabel(widget)
        label_14.setObjectName("label_14")
        label_14.setText(task.deskripsi)  # Set deskripsi task
        label_14.setFont(QtGui.QFont("Arial", 12))
        horizontalLayout.addWidget(label_14)

        self.ui.verticalLayout.addWidget(widget)
        
    
    def clear_layout(self, layout):
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