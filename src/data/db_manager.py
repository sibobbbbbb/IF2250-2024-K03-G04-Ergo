from data.databases import Board, Project, Task

class DatabaseManager:
    def __init__(self, database):
        self.database = database

    def create_boards_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Boards (
            idBoard INTEGER PRIMARY KEY,
            namaBoard TEXT NOT NULL,
            isFavorite INTEGER NOT NULL
        )
        '''
        self.database.execute_query(query)

    def create_board(self, board):
        query = '''INSERT INTO Boards(idBoard, namaBoard, isFavorite) VALUES(?,?,?)'''
        params = (board.idBoard, board.namaBoard, board.isFavorite)
        self.database.execute_query(query, params)

    def get_board(self, idBoard):
        query = '''SELECT * FROM Boards WHERE idBoard = ?'''
        params = (idBoard,)
        board = self.database.execute_query(query, params).fetchone()
        return Board(*board) if board else None

    def update_board(self, board):
        query = '''UPDATE Boards SET namaBoard = ?, isFavorite = ? WHERE idBoard = ?'''
        params = (board.namaBoard, board.isFavorite, board.idBoard)
        self.database.execute_query(query, params)

    def delete_board(self, idBoard):
        query = '''DELETE FROM Boards WHERE idBoard = ?'''
        params = (idBoard,)
        self.database.execute_query(query, params)

    def create_projects_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Projects (
            idProject INTEGER PRIMARY KEY,
            idBoard INTEGER,
            namaProject TEXT NOT NULL,
            tingkatKetuntasan INTEGER,
            deadlineProject TEXT,
            isFavorite INTEGER NOT NULL
        )
        '''
        self.database.execute_query(query)

    def create_project(self, project):
        query = '''INSERT INTO Projects(idProject, idBoard, namaProject, tingkatKetuntasan, deadlineProject, isFavorite) VALUES(?,?,?,?,?,?)'''
        params = (project.idProject, project.idBoard, project.namaProject, project.tingkatKetuntasan, project.deadlineProject, project.isFavorite)
        self.database.execute_query(query, params)

    def get_project(self, idProject):
        query = '''SELECT * FROM Projects WHERE idProject = ?'''
        params = (idProject,)
        project = self.database.execute_query(query, params).fetchone()
        return Project(*project) if project else None

    def get_projects_by_board(self, idBoard):
        query = '''SELECT * FROM Projects WHERE idBoard = ?'''
        params = (idBoard,)
        projects = self.database.execute_query(query, params).fetchall()
        return [Project(*project) for project in projects]

    def update_project(self, project):
        query = '''UPDATE Projects SET idBoard = ?, namaProject = ?, tingkatKetuntasan = ?, deadlineProject = ?, isFavorite = ? WHERE idProject = ?'''
        params = (project.idBoard, project.namaProject, project.tingkatKetuntasan, project.deadlineProject, project.isFavorite, project.idProject)
        self.database.execute_query(query, params)

    def delete_project(self, idProject):
        query = '''DELETE FROM Projects WHERE idProject = ?'''
        params = (idProject,)
        self.database.execute_query(query, params)

    def create_tasks_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Tasks (
            idTask INTEGER PRIMARY KEY,
            idProject INTEGER,
            namaTask TEXT NOT NULL,
            status TEXT,
            kategori TEXT,
            deskripsi TEXT,
            deadlineTask TEXT
        )
        '''
        self.database.execute_query(query)

    def create_task(self, task):
        query = '''INSERT INTO Tasks(idTask, idProject, namaTask, status, kategori, deskripsi, deadlineTask) VALUES(?,?,?,?,?,?,?)'''
        params = (task.idTask, task.idProject, task.namaTask, task.status, task.kategori, task.deskripsi, task.deadlineTask)
        self.database.execute_query(query, params)

    def get_task(self, idTask):
        query = '''SELECT * FROM Tasks WHERE idTask = ?'''
        params = (idTask,)
        task = self.database.execute_query(query, params).fetchone()
        return Task(*task) if task else None

    def get_tasks_by_project(self, idProject):
        query = '''SELECT * FROM Tasks WHERE idProject = ?'''
        params = (idProject,)
        tasks = self.database.execute_query(query, params).fetchall()
        return [Task(*task) for task in tasks]

    def update_task(self, task):
        query = '''UPDATE Tasks SET idProject = ?, namaTask = ?, status = ?, kategori = ?, deskripsi = ?, deadlineTask = ? WHERE idTask = ?'''
        params = (task.idProject, task.namaTask, task.status, task.kategori, task.deskripsi, task.deadlineTask, task.idTask)
        self.database.execute_query(query, params)

    def delete_task(self, idTask):
        query = '''DELETE FROM Tasks WHERE idTask = ?'''
        params = (idTask,)
        self.database.execute_query(query, params)
    

    