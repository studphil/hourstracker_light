# Importing local modules
from database_manager import DatabaseManager
from timetracker import TimeTracker
from menu import Menu

# Importing modules from Python API
from datetime import datetime as dt
import sqlite3

# Initialize Database
db_manager = DatabaseManager('hourstracker.db')
db_manager.connect()
db_manager.create_tables_from_file('schema.sql')

time_tracker = TimeTracker(db_manager)

menu = Menu(time_tracker, db_manager)

# Display menu
menu.show_menu()

# Close Database
db_manager.close()