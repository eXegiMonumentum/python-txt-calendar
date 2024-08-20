import datetime
import calendar
import os
#I imported the variable from the main file
from main import base_path

class FileCreator:

    weeks_range = []
    chosen_month = datetime.datetime.now().strftime("%B")

    current_day_int = datetime.datetime.now().day
    current_month_int = int(datetime.datetime.now().strftime("%m"))
    current_year_int = int(datetime.datetime.now().strftime("%Y"))

    def __init__(self, current_month=False):
        self.base_path = base_path
        self.current_month = current_month
        self.__month_number = None
    def __divide_chosen_month_to_weeks(self):
        """Creating a list of weeks for the chosen month,
         where the 0th index represents Monday, the 1st index represents Tuesday, and so on.

        Example:
            For January:
            weeks = [[1, 2, 3, 4, 5, 6, 7], ..., [29, 30, 31, 0, 0, 0, 0]]

        input:
            chosen_month (int): The chosen month, e.g., "1" for chose January".
        """

        months = list(calendar.month_name)[1:]

        if self.current_month:
            self.__month_number = self.current_month_int

        else:
            for i, month in enumerate(months, start=1):
                print(f'{i:2}, --> {month}')
            try:
                self.__month_number = int(input(f"Enter the month number (1 to 12) of {self.current_year_int}r. you would like to chose: "))
                if self.__month_number not in range(1, 13):
                    raise ValueError("Month number must be between 1 and 12")
            except:
                raise ValueError("Invalid input. Please enter a valid month number.")

        chosen_month = months[self.__month_number - 1]
        weeks = calendar.monthcalendar(self.current_year_int, self.__month_number)
        return chosen_month, weeks

    def __get_weeks_range(self):
        """Create a list of tuples, which contain the range of days for each week of the selected month.


            :returns:  chosen month (str) and weeks_range (list of tuples representing the range of days for each week
            :Example: chosen_month = January, weeks range = [(1, 7), (8, 14), (15, 21), (22, 28), (29, 31)])
            """
        weeks_range = []
        chosen_month, weeks = self.__divide_chosen_month_to_weeks()
        for i, week in enumerate(weeks, start=1):
            week = list(filter(lambda x: x != 0, week))
            weeks_range.append((min((week)), max(week)))
        self.__class__.weeks_range = weeks_range
        self.__class__.chosen_month = chosen_month
        return chosen_month, weeks_range


    def creating_chosen_month_and_weeks_directionaries(self):
        """Creating directories for chosen month and separated into weeks"""

        chosen_month, weeks_range = self.__get_weeks_range()
        chosen_month_directory = os.path.join(self.base_path, chosen_month)
        os.makedirs(chosen_month_directory, exist_ok=True)
        weeks_dirs = []

        for i in range(1, len(weeks_range) + 1):
            dir_name = f'{i}_week'
            week_directory = os.path.join(self.base_path, chosen_month, dir_name)
            weeks_dirs.append(week_directory)
            os.makedirs(week_directory, exist_ok=True)
        return chosen_month_directory, weeks_dirs


    def create_paths_for_days_txt_files(self):
        """creating path's for the days of the month"""

        _, weeks_dirs = self.creating_chosen_month_and_weeks_directionaries()
        weeks_iterator = 0
        f_paths = []
        for week_index, week in enumerate(self.weeks_range, start=1):
            start, end = week
            for day in range(start, end + 1):
                f_name = f'{day:02d}{self.current_month_int:02d}{self.current_year_int:04d}.txt'
                f_paths.append(os.path.join(self.base_path, weeks_dirs[weeks_iterator], f_name))
            if weeks_iterator < len(weeks_dirs):
                weeks_iterator += 1
        return f_paths

    def create_txt_files_for_chosen_month(self):
        """for each day of the selected month will create a text file"""
        f_paths = self.create_paths_for_days_txt_files()
        for path in f_paths:
            try:
                with open(path, 'x') as f:
                    pass
            except FileExistsError:
                print("File already exist")

            except OSError as e:
                print(f"File operation failed due to system-related errors.: {e}")
                return None


