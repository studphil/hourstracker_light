import inquirer

class Menu:
    def __init__(self, time_tracker, db_manager):
        self.time_tracker = time_tracker
        self.db_manager = db_manager

    def show_menu(self):
        main_menu_choices = [
            'Time Tracker',
            'Projects',
            'Clients',
            'Closing',
            'Exit'
        ]

        while True:
            main_menu_question = [
                inquirer.List('choice',
                              message="Select an option",
                              choices=main_menu_choices,
                              ),
            ]
            main_answer = inquirer.prompt(main_menu_question)
            choice = main_answer['choice']

            if choice == 'Time Tracker':
                self.handle_time_tracker_options()
            elif choice == 'Projects':
                self.handle_projects()
            elif choice == 'Clients':
                self.handle_clients()
            elif choice == 'Closing':
                self.handle_closing()
            elif choice == 'Exit':
                break

    def handle_time_tracker_options(self):
        time_tracker_menu_choices = [
            'Log New Hours',
            'View Logged Hours',
            'Back to Main Menu'
        ]
        time_tracker_question = [
            inquirer.List('subchoice',
                          message="Time Tracker Options",
                          choices=time_tracker_menu_choices,
                          )
        ]
        time_tracker_answer = inquirer.prompt(time_tracker_question)
        subchoice = time_tracker_answer['subchoice']

        if subchoice == 'Log New Hours':
            record_entry = self.time_tracker.record_hours()
            print(record_entry)
            print("...hours saved")
        elif subchoice == 'View Logged Hours':
            # Logic to view logged hours
            pass

    def handle_projects(self):
        # Logic for handling project-related options
        handle_projects_menu_choices = [
            'Create New Project',
            'View Projects',
            'Back to Main Menu'
        ]
        pass

    def handle_clients(self):
        # Logic for handling client-related options
        pass

    def handle_closing(self):
        # Logic for handling closing-related options
        handle_closing_menu_choices = [
            'Submit Hours',
            'Export Hours to Conactive ERP',
            'Export Hours to Partner ERP',
            'Back to Main Menu'
        ]

        handle_closing_question = [
            inquirer.List('subchoice',
                          message="Time Tracker Options",
                          choices=handle_closing_menu_choices,
                          )
        ]
        handle_closing_answer = inquirer.prompt(handle_closing_question)
        subchoice = handle_closing_answer['subchoice']

        if subchoice == 'Submit Hours':
            pass
            # Save record_entry to database or CSV
        elif subchoice == 'Export Hours to Conactive ERP':
            # Logic to view logged hours
            pass
        elif subchoice == 'Export Hours to Partner ERP':
            # Logic to view logged hours
            pass
        elif subchoice == 'Back to Main Menu':
            # Logic to view logged hours
            pass


    def create_new_project(self):
        project_name = inquirer.prompt([inquirer.Text('name', message="Enter new project name")])['name']
        # Insert the new project into the database
        print("New project created.")
        # Implement the logic to insert project_name into the database
