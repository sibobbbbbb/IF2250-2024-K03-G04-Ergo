import pytest
from src.data.databases import Database, Board, Project, Task
from src.data.db_manager import DatabaseManager

@pytest.fixture
def db_manager():
    db = Database()
    db_manager = DatabaseManager(db)
    db_manager.create_boards_table()
    db_manager.create_projects_table()
    db_manager.create_tasks_table()
    yield db_manager
    db.close()

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
    assert db_manager.get_board(board1.idBoard) is not None
    assert db_manager.get_board(board2.idBoard) is not None
    assert db_manager.get_board(board3.idBoard) is not None

    # Update a board
    board1.namaBoard = 'Updated board 1'
    db_manager.update_board(board1)

    # Check if the board was updated
    assert db_manager.get_board(board1.idBoard).namaBoard == 'Updated board 1'

    # Delete a board
    db_manager.delete_board(board2.idBoard)

    # Check if the board was deleted
    assert db_manager.get_board(board2.idBoard) is None

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
    assert db_manager.get_project(project1.idProject) is not None
    assert db_manager.get_project(project2.idProject) is not None
    assert db_manager.get_project(project3.idProject) is not None

    # Update a project
    project1.namaProject = 'Updated project 1'
    db_manager.update_project(project1)

    # Check if the project was updated
    assert db_manager.get_project(project1.idProject).namaProject == 'Updated project 1'

    # Delete a project
    db_manager.delete_project(project2.idProject)

    # Check if the project was deleted
    assert db_manager.get_project(project2.idProject) is None

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
    assert db_manager.get_task(task1.idTask) is not None
    assert db_manager.get_task(task2.idTask) is not None
    assert db_manager.get_task(task3.idTask) is not None

    # Update a task
    task1.namaTask = 'Updated task 1'
    db_manager.update_task(task1)

    # Check if the task was updated
    assert db_manager.get_task(task1.idTask).namaTask == 'Updated task 1'

    # Delete a task
    db_manager.delete_task(task2.idTask)

    # Check if the task was deleted
    assert db_manager.get_task(task2.idTask) is None