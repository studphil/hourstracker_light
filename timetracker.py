import inquirer
from prettytable import PrettyTable

from datetime import datetime as dt

class TimeTracker:
    """
    The TimeTracker class is responsible for tracking time spent on projects by a consultant. 
    It allows recording of the hours worked, the project details, and additional notes about the work done.
    The class interacts with a database manager to store these records and also uses a command-line interface
    for input and confirmation from the user.

    Attributes:
        db_manager: An instance of a database manager class for interacting with the database.
        consultant: The name of the consultant using this time tracker.
    """

    def __init__(self, db_manager, consultant_name="Philipp Studer"):
        self.db_manager = db_manager
        self.consultant = consultant_name

    def record_hours(self):
        project = self.select_project()
        if not project:
            print("No project selected.")
            return

        record_entry = self.get_hours_entry()
        self.confirm_and_save(record_entry)

    def get_hours_entry(self):
        questions = [
            inquirer.Text('date_of_record', message="Date of Record", default=dt.now().strftime('%Y-%m-%d')),
            inquirer.Text('hours', message="Hours worked today"),
            inquirer.Text('activity_description', message="Quick Description of what has been done"),
            inquirer.Confirm('lunch', message="Did you take lunch?", default=False)
        ]

        answers = inquirer.prompt(questions)
        return {
            'date_of_record': answers['date_of_record'],
            'hours_worked': answers['hours'],
            'activity_description': answers['activity_description'],
            'bool_lunch': 'y' if answers['lunch'] else 'n',
            'consultant': self.consultant,
            'billed': False
        }

    def confirm_and_save(self, record_entry):
        print(self.format_record_as_table(record_entry))

        if self.confirm_action("Do you want to save this record?"):
            self.save_record_to_db(record_entry)
            print("Record inserted successfully.")
        else:
            print("Record insertion cancelled.")

    def format_record_as_table(self, record_entry):
        table = PrettyTable()
        table.field_names = record_entry.keys()
        table.add_row(record_entry.values())
        return table

    def confirm_action(self, message):
        questions = [inquirer.Confirm('confirm', message=message, default=True)]
        answers = inquirer.prompt(questions)
        return answers['confirm']

    def save_record_to_db(self, record_entry):
        query = '''INSERT INTO record_entry (date_of_record, hours_worked, activity_description, consultant, billed)
                   VALUES (:date_of_record, :hours_worked, :activity_description, :consultant, :billed)'''
        self.db_manager.insert_data(query, record_entry)

    def select_project(self):
        project_selector = ProjectSelector(self.db_manager)
        return project_selector.select_project()

class ProjectSelector:
    """
    The ProjectSelector class is responsible for selecting a project from a database.
    It interacts with a database manager to fetch clients and projects data, and allows
    the user to select a client and a project associated with that client through a 
    command-line interface. This class assumes that the database manager provided to it
    has a method `fetch_data` for executing SQL queries.
    """
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def select_project(self):
        client = self.select_client()
        if client is None:
            return None
        return self.select_project_for_client(client)
        
    def select_client(self):
        query = "SELECT id, client FROM clients_companies"
        clients = self.db_manager.fetch_data(query)
        return self.choose_option(clients, "client")

    def select_project_for_client(self, client):
        # Assuming client[0] is the client ID
        query = "SELECT client, project FROM projects WHERE client = ?"
        client = 1
        params = (client,)
        projects = self.db_manager.fetch_data(query, params)
        return self.choose_option(projects, "project")

    def choose_option(self, options, option_type):
        if not options:
            print("No Data found in Database. Please create projects to post to.")
            return None

        self.display_options(options, option_type)
        return self.get_user_choice(options)

    def display_options(self, options, option_type):
        """
        Displays the given options in a table format, allowing the user to choose one.

        Args:
            options: A list of options to be displayed.
            option_type: A string representing the type of option (e.g., 'client', 'project').
        """
        table = PrettyTable()
        table.field_names = [f"Option Number", f"{option_type.title()} Name"]

        for i, option in enumerate(options, start=1):
            table.add_row([i, option[1]])  # Assuming 'option' can be represented as a string directly

        print(table)

    def get_user_choice(self, options):
        while True:
            try:
                choice = int(input("Your choice: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid choice. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class ViewHours:

    def __init__(self, db_manager):
        self.db_manager = db_manager