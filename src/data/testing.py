# Import your classes
from databases import Database, Board, Project, Task
from db_manager import DatabaseManager

# Create a Database object
db = Database('ergo.db')

# Create a DatabaseManager object
db_manager = DatabaseManager(db)

# Create the tables
db_manager.create_boards_table()
db_manager.create_projects_table()
db_manager.create_tasks_table()

# Create Board objects
board1 = Board(1, 'Ini board 1', 0)
board2 = Board(2, 'Ini board 2', 0)
board3 = Board(3, 'Ini board 3', 0)

# Add the Boards to the database
db_manager.create_board(board1)
db_manager.create_board(board2)
db_manager.create_board(board3)

# Create Project objects
project1 = Project(1, 1, 'Ini project 1', 0, '2022-12-31', 0)
project2 = Project(2, 1, 'Ini project 2', 0, '2021-12-31', 0)
project3 = Project(3, 1, 'Ini project 3', 0, '2020-12-31', 0)
project4 = Project(4, 1, 'Ini project 4', 0, '2022-10-31', 0)
project5 = Project(5, 1, 'Ini project 5', 0, '2022-10-06', 0)
project6 = Project(6, 1, 'Ini project 6', 0, '2022-01-31', 0)
project7 = Project(7, 1, 'Ini project 7', 0, '2022-03-04', 0)
project8 = Project(8, 1, 'Ini project 8', 0, '2022-01-04', 0)
project9 = Project(9, 1, 'Ini project 9', 0, '2022-01-01', 0)
project10 = Project(10, 1, 'Ini project 10', 0, '2002-12-31', 0)
project11 = Project(11, 1, 'Ini project 11', 0, '2003-12-31', 1)

# Add the Projects to the database
db_manager.create_project(project1)
db_manager.create_project(project2)
db_manager.create_project(project3)
db_manager.create_project(project4)
db_manager.create_project(project5)
db_manager.create_project(project6)
db_manager.create_project(project7)
db_manager.create_project(project8)
db_manager.create_project(project9)
db_manager.create_project(project10)
db_manager.create_project(project11)

# Retrieve the Projects from the database
projects = db_manager.get_projects_by_board(board1.idBoard)

# Print the retrieved Projects
for project in projects:
    print(f"Project ID: {project.idProject}, Board ID: {project.idBoard}, Project Name: {project.namaProject}")

# Create Task objects
task1 = Task(1, 1, 'Ini task 1', "Not Yet Started", 'Kategori 1', 'Deskripsi task 1', '2022-12-31 00:00')
task2 = Task(2, 1, 'Ini task 2', "Not Yet Started", 'Kategori 2', 'Deskripsi task 2', '2022-12-31 23:59')
task3 = Task(3, 1, 'Ini task 3', "Not Yet Started", 'Kategori 3', 'Deskripsi task 3', '2022-12-31 23:59')
task4 = Task(4, 1, 'Ini task 4', "Not Yet Started", 'Kategori 2', 'Deskripsi task 4', '2022-12-31 23:59')
task5 = Task(5, 1, 'Ini task 5', "Not Yet Started", 'Kategori 3', 'Deskripsi task 5', '2022-12-31 23:59')
task6 = Task(6, 1, 'Ini task 6', "Not Yet Started", 'Kategori 2', 'Deskripsi task 6', '2022-12-31 23:59')
task7 = Task(7, 1, 'Ini task 7', "Not Yet Started", 'Kategori 3', 'Deskripsi task 7', '2022-12-31 23:59')

# Add the Tasks to the database
db_manager.create_task(task1)
db_manager.create_task(task2)
db_manager.create_task(task3)
db_manager.create_task(task4)
db_manager.create_task(task5)
db_manager.create_task(task6)
db_manager.create_task(task7)

# Retrieve the Tasks from the database
tasks = db_manager.get_tasks_by_project(project1.idProject)

# Print the retrieved Tasks
for task in tasks:
    print(f"Task ID: {task.idTask}, Project ID: {task.idProject}, Task Name: {task.namaTask}")


# Close the database connection
db.close()