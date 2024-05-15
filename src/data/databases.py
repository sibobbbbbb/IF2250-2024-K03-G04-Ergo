import os
import sqlite3

class Database:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), "ergo.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor

    def close(self):
        self.conn.close()

class Board:
    def __init__(self, idBoard, namaBoard, isFavorite):
        self.idBoard = idBoard
        self.namaBoard = namaBoard
        self.isFavorite = isFavorite
        self.projects = []

class Project:
    def __init__(self, idProject, idBoard, namaProject, tingkatKetuntasan, deadlineProject, isFavorite):
        self.idProject = idProject
        self.idBoard = idBoard
        self.namaProject = namaProject
        self.tingkatKetuntasan = tingkatKetuntasan
        self.deadlineProject = deadlineProject
        self.isFavorite = isFavorite
        self.tasks = []

class Task:
    def __init__(self, idTask, idProject, namaTask, status, kategori, deskripsi, deadlineTask):
        self.idTask = idTask
        self.idProject = idProject
        self.namaTask = namaTask
        self.status = status
        self.kategori = kategori
        self.deskripsi = deskripsi
        self.deadlineTask = deadlineTask