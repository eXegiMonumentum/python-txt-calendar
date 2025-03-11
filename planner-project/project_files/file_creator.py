from path_validator import PathValidator
import datetime
import calendar
import os


class FileCreator:
    base_path = 'created_planner'
    chosen_month = datetime.datetime.now().strftime("%B")  # Default: current month

    now = datetime.datetime.now()
    current_day_int = now.day
    current_month_int = now.month
    current_year_int = now.year

    def __init__(self, current_month=False, create_files=False, chosen_month_number=None):
        """
        Initializes the FileCreator class.
        - current_month: If True, uses the current month. Otherwise, the user selects a month.
        - create_files: If True, files are created in the validated directory.
        - chosen_month_number: If provided, sets the month directly.
        """
        self.current_month = current_month
        self.chosen_month_number = chosen_month_number if chosen_month_number else None
        self.__initialize_base_path(create_files=create_files)

    def __initialize_base_path(self, create_files=False):
        """Initializes the base path for file creation."""
        if create_files:
            path_valid = PathValidator()
            FileCreator.base_path = path_valid.get_valid_directory_path()

    def __divide_chosen_month_to_weeks(self):
        """Divides the chosen month into weekly segments."""
        months = list(calendar.month_name)[1:]

        if self.current_month:
            self.chosen_month_number = self.current_month_int
        elif not self.chosen_month_number:
            for i, month in enumerate(months, start=1):
                print(f'{i:2}, --> {month}')

            while True:
                try:
                    self.chosen_month_number = int(input("Enter the month number (1-12): "))
                    if 1 <= self.chosen_month_number <= 12:
                        break
                    print("Invalid choice! Please enter a number between 1 and 12.")
                except ValueError:
                    print("Invalid input. Please enter a number.")


        chosen_month = months[self.chosen_month_number - 1]
        weeks = calendar.monthcalendar(self.current_year_int, self.chosen_month_number)

        return chosen_month, weeks

    def __get_weeks_range(self):
        """Generates a list of tuples containing the start and end days of each week."""
        weeks_range = []
        chosen_month, weeks = self.__divide_chosen_month_to_weeks()
        for week in weeks:
            week = list(filter(lambda x: x != 0, week))  # Remove padding zeros
            weeks_range.append((min(week), max(week)))
        return chosen_month, weeks_range

    def creating_chosen_month_and_weeks_directories(self):
        """Creates directories for the selected month and its weeks."""
        chosen_month, weeks_range = self.__get_weeks_range()
        chosen_month_directory = os.path.join(self.base_path, chosen_month)
        os.makedirs(chosen_month_directory, exist_ok=True)

        weeks_dirs = []
        for i in range(1, len(weeks_range) + 1):
            dir_name = f'{i}_week'
            week_directory = os.path.join(chosen_month_directory, dir_name)
            os.makedirs(week_directory, exist_ok=True)
            weeks_dirs.append(week_directory)

        return chosen_month_directory, weeks_dirs, weeks_range

    def create_paths_for_days_txt_files(self):
        """Generates a list of file paths for each day of the selected month."""
        _, weeks_dirs, weeks_range = self.creating_chosen_month_and_weeks_directories()
        f_paths = []

        for week_index, (start, end) in enumerate(weeks_range):
            for day in range(start, end + 1):
                f_name = f'{day:02d}{self.chosen_month_number:02d}{self.current_year_int:04d}.txt'
                f_paths.append(os.path.join(weeks_dirs[week_index], f_name))

        return f_paths

    def create_txt_files_for_chosen_month(self):
        """Creates text files for each day of the selected month."""
        f_paths = self.create_paths_for_days_txt_files()
        alerts = []

        for path in f_paths:
            try:
                with open(path, 'x'):
                    print(f"Created {path}!")
            except FileExistsError:
                alerts.append(f"File {path} already exists")
            except OSError as e:
                print(f"File operation failed due to system-related errors: {e}")
                return None

        if alerts:
            print("Some files already existed:")
            for alert in alerts:
                print(alert)
