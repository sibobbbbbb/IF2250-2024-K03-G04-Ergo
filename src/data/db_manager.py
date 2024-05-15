from .databases import Database, Board, Project, Task

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
        return self.database.execute_query(query, params).fetchone()
    
    def get_all_boards(self):
        query = '''SELECT * FROM Boards'''
        boards_data = self.database.execute_query(query).fetchall()
        boards = []
        for board_data in boards_data:
            board = Board(*board_data)
            boards.append(board)
        return boards
    
    def get_all_projects(self):
        query = '''SELECT * FROM Projects'''
        projects_data = self.database.execute_query(query).fetchall()
        projects = []
        for project_data in projects_data:
            project = Project(*project_data)
            projects.append(project)
        return projects
    
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
        return self.database.execute_query(query, params).fetchone()

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
        return self.database.execute_query(query, params).fetchone()

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
    
    def print_all_boards(self):
        boards = self.get_all_boards()
        if boards:
            print("Daftar Boards:")
            for board in boards:
                print(board.idBoard)
                print(board.namaBoard) 
        else:
            print("Tidak ada board yang tersimpan di database.")
            
    def isInDatabase(self, namaBoard):
        boards = self.get_all_boards()
        for board in boards:
            if board.namaBoard == namaBoard:
                return True
        return False
        
    def getLastIdBoard(self):
        boards = self.get_all_boards()
        if boards:
            return boards[-1].idBoard
        return 0
    
    def getLastIdProject(self):
        projects = self.get_all_projects()
        if projects:
            return projects[-1].idProject
        return 0

    def getLastIdTask(self):
        tasks = self.get_all_tasks()
        if tasks:
            return tasks[-1].idTask
        return 0
    
    def get_all_tasks(self):
        query = '''SELECT * FROM Tasks'''
        tasks_data = self.database.execute_query(query).fetchall()
        tasks = []
        for task_data in tasks_data:
            task = Task(*task_data)
            tasks.append(task)
        return tasks
    
    def get_board_by_project(self, idproject):
        #dari idproject yang diberi, dicari idboardnya
        query = '''SELECT idBoard FROM Projects WHERE idProject = ?'''
        params = (idproject,)
        result = self.database.execute_query(query, params).fetchone()
        if result:
            return result[0]
        else:
            return None
        
    def get_projectName_by_id(self, idproject):
        query = '''SELECT namaProject FROM Projects WHERE idProject = ?'''
        params = (idproject,)
        result = self.database.execute_query(query, params).fetchone()
        if result:
            return result[0]
        else:
            return None
        
    def get_boardName_by_id(self, idboard):
        query = '''SELECT namaBoard FROM Boards WHERE idBoard = ?'''
        params = (idboard,)
        result = self.database.execute_query(query, params).fetchone()
        if result:
            return result[0]
        else:
            return None