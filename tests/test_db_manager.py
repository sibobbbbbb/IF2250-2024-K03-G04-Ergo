import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

from unittest.mock import create_autospec
from src.data.databases import Database, Board, Project, Task
from src.data.db_manager import DatabaseManager

@pytest.fixture
def db_manager():
    # Create a mock Database object
    db = create_autospec(Database, instance=True)
    db_manager = DatabaseManager(db)
    yield db_manager

def test_board_operations(db_manager):
    # Create Board objects
    board1 = Board(1, 'Ini board 1', 0)
    board2 = Board(2, 'Ini board 2', 0)
    board3 = Board(3, 'Ini board 3', 0)

    # Add the Boards to the database
    db_manager.create_board(board1)
    db_manager.create_board(board2)
    db_manager.create_board(board3)

    # Check if the boards were added
    db_manager.database.execute_query.assert_any_call('INSERT INTO Boards(idBoard, namaBoard, isFavorite) VALUES(?,?,?)', (board1.idBoard, board1.namaBoard, board1.isFavorite))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Boards(idBoard, namaBoard, isFavorite) VALUES(?,?,?)', (board2.idBoard, board2.namaBoard, board2.isFavorite))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Boards(idBoard, namaBoard, isFavorite) VALUES(?,?,?)', (board3.idBoard, board3.namaBoard, board3.isFavorite))

    # Update a board
    board1.namaBoard = 'Updated board 1'
    db_manager.update_board(board1)

    # Check if the board was updated
    db_manager.database.execute_query.assert_called_with('UPDATE Boards SET namaBoard = ?, isFavorite = ? WHERE idBoard = ?', (board1.namaBoard, board1.isFavorite, board1.idBoard))

    # Delete a board
    db_manager.delete_board(board2.idBoard)

    # Check if the board was deleted
    db_manager.database.execute_query.assert_called_with('DELETE FROM Boards WHERE idBoard = ?', (board2.idBoard,))

def test_project_operations(db_manager):
    # Create Project objects
    project1 = Project(1, 1, 'Ini project 1', 0, '2022-12-31', 0)
    project2 = Project(2, 1, 'Ini project 2', 0, '2022-12-31', 0)
    project3 = Project(3, 1, 'Ini project 3', 0, '2022-12-31', 0)

    # Add the Projects to the database
    db_manager.create_project(project1)
    db_manager.create_project(project2)
    db_manager.create_project(project3)

    # Check if the projects were added
    db_manager.database.execute_query.assert_any_call('INSERT INTO Projects(idProject, idBoard, namaProject, tingkatKetuntasan, deadlineProject, isFavorite) VALUES(?,?,?,?,?,?)', (project1.idProject, project1.idBoard, project1.namaProject, project1.tingkatKetuntasan, project1.deadlineProject, project1.isFavorite))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Projects(idProject, idBoard, namaProject, tingkatKetuntasan, deadlineProject, isFavorite) VALUES(?,?,?,?,?,?)', (project2.idProject, project2.idBoard, project2.namaProject, project2.tingkatKetuntasan, project2.deadlineProject, project2.isFavorite))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Projects(idProject, idBoard, namaProject, tingkatKetuntasan, deadlineProject, isFavorite) VALUES(?,?,?,?,?,?)', (project3.idProject, project3.idBoard, project3.namaProject, project3.tingkatKetuntasan, project3.deadlineProject, project3.isFavorite))

    # Update a project
    project1.namaProject = 'Updated project 1'
    db_manager.update_project(project1)

    # Check if the project was updated
    db_manager.database.execute_query.assert_called_with('UPDATE Projects SET idBoard = ?, namaProject = ?, tingkatKetuntasan = ?, deadlineProject = ?, isFavorite = ? WHERE idProject = ?', (project1.idBoard, project1.namaProject, project1.tingkatKetuntasan, project1.deadlineProject, project1.isFavorite, project1.idProject))

    # Delete a project
    db_manager.delete_project(project2.idProject)

    # Check if the project was deleted
    db_manager.database.execute_query.assert_called_with('DELETE FROM Projects WHERE idProject = ?', (project2.idProject,))

def test_task_operations(db_manager):
    # Create Task objects
    task1 = Task(1, 1, 'Ini task 1', 0, 'Kategori 1', 'Deskripsi task 1', '2022-12-31')
    task2 = Task(2, 1, 'Ini task 2', 0, 'Kategori 2', 'Deskripsi task 2', '2022-12-31')
    task3 = Task(3, 1, 'Ini task 3', 0, 'Kategori 3', 'Deskripsi task 3', '2022-12-31')

    # Add the Tasks to the database
    db_manager.create_task(task1)
    db_manager.create_task(task2)
    db_manager.create_task(task3)

    # Check if the tasks were added
    db_manager.database.execute_query.assert_any_call('INSERT INTO Tasks(idTask, idProject, namaTask, status, kategori, deskripsi, deadlineTask) VALUES(?,?,?,?,?,?,?)', (task1.idTask, task1.idProject, task1.namaTask, task1.status, task1.kategori, task1.deskripsi, task1.deadlineTask))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Tasks(idTask, idProject, namaTask, status, kategori, deskripsi, deadlineTask) VALUES(?,?,?,?,?,?,?)', (task2.idTask, task2.idProject, task2.namaTask, task2.status, task2.kategori, task2.deskripsi, task2.deadlineTask))
    db_manager.database.execute_query.assert_any_call('INSERT INTO Tasks(idTask, idProject, namaTask, status, kategori, deskripsi, deadlineTask) VALUES(?,?,?,?,?,?,?)', (task3.idTask, task3.idProject, task3.namaTask, task3.status, task3.kategori, task3.deskripsi, task3.deadlineTask))

    # Update a task
    task1.namaTask = 'Updated task 1'
    db_manager.update_task(task1)

    # Check if the task was updated
    db_manager.database.execute_query.assert_called_with('UPDATE Tasks SET idProject = ?, namaTask = ?, status = ?, kategori = ?, deskripsi = ?, deadlineTask = ? WHERE idTask = ?', (task1.idProject, task1.namaTask, task1.status, task1.kategori, task1.deskripsi, task1.deadlineTask, task1.idTask))

    # Delete a task
    db_manager.delete_task(task2.idTask)

    # Check if the task was deleted
    db_manager.database.execute_query.assert_called_with('DELETE FROM Tasks WHERE idTask = ?', (task2.idTask,))