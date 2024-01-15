from datetime import datetime as dt
import sqlite3

# DatabaseManager Class
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to the SQLite database."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables_from_file(self, file_path):
        """Create tables from an SQL file."""
        with open(file_path, 'r') as file:
            # Read the entire file and split it into individual SQL statements
            sql_script = file.read()
            sql_statements = sql_script.split(';')

            # Execute each SQL statement
            for statement in sql_statements:
                if statement.strip():
                    self.cursor.execute(statement)

    def print_tables(self):
        """Print the list of tables in the database."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])


    def insert_data(self, query, data):
        """Insert data into the table."""
        data['date_time'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query, params=()):
        """Execute a SELECT query and return the results."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()

