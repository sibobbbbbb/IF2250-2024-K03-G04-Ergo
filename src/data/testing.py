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
project2 = Project(2, 1, 'Ini project 2', 0, '2022-12-31', 0)
project3 = Project(3, 1, 'Ini project 3', 0, '2022-12-31', 0)

# Add the Projects to the database
db_manager.create_project(project1)
db_manager.create_project(project2)
db_manager.create_project(project3)

# Retrieve the Projects from the database
projects = db_manager.get_projects_by_board(board1.idBoard)

# Print the retrieved Projects
for project in projects:
    print(f"Project ID: {project.idProject}, Board ID: {project.idBoard}, Project Name: {project.namaProject}")

# Create Task objects
task1 = Task(1, 1, 'Ini task 1', 0, 'Kategori 1', 'Deskripsi task 1', '2022-12-31')
task2 = Task(2, 1, 'Ini task 2', 0, 'Kategori 2', 'Deskripsi task 2', '2022-12-31')
task3 = Task(3, 1, 'Ini task 3', 0, 'Kategori 3', 'Deskripsi task 3', '2022-12-31')

# Add the Tasks to the database
db_manager.create_task(task1)
db_manager.create_task(task2)
db_manager.create_task(task3)

# Retrieve the Tasks from the database
tasks = db_manager.get_tasks_by_project(project1.idProject)

# Print the retrieved Tasks
for task in tasks:
    print(f"Task ID: {task.idTask}, Project ID: {task.idProject}, Task Name: {task.namaTask}")


# Close the database connection
db.close()