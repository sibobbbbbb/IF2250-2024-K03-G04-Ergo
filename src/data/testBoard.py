# Import your classes
import databases as db
import db_manager as dbm

# Create a Database object
db = db.Database('ergo.db')

db_manager = dbm.DatabaseManager(db)

db_manager.print_all_boards()

# Close the database connection
db.close()