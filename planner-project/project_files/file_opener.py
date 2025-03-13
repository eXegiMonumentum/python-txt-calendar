from file_creator import FileCreator
import os


class FileOpener(FileCreator):
    """
    Class responsible for reading planner files.
    """
    def __init__(self, current_month=False):
        """
        Initializes FileOpener.
        :param current_month: Determines if the operation is on the current month.
        """
        super().__init__(current_month=current_month)
        self.f_paths = self.create_paths_for_days_txt_files()
        self.today_path = self.f_paths[self.current_day_int - 1] if self.current_month else None

    def read_today_file(self):
        """
        Reads and prints today's file content.
        :return: List of records from the text file or None in case of an error.
        """
        if not self.current_month:
            raise ValueError("read_today_file() can only be used when current_month=True.")

        if not os.path.exists(self.today_path):
            print(f"File {self.today_path} does not exist! Please create a schedule.")
            return None

        try:
            with open(self.today_path, 'r', encoding='UTF-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                if lines:
                    print("Today's file content:")
                    for i, line in enumerate(lines, start=1):
                        print(f'{i}: {line}')
                else:
                    print(f"File {self.today_path} is empty. Please add content.")
                return lines
        except OSError as e:
            print(f"File operation failed: {e}")
            return None

    def read_files_from_week_of_current_month(self):
        """
        Reads and displays text files from a selected week of the current month.
        """
        if not self.current_month:
            raise ValueError("read_files_from_week_of_current_month() can only be used when current_month=True.")

        _, weeks_dirs = self.creating_chosen_month_and_weeks_directories()

        print(f"Choose a week of {self.chosen_month} to check:")
        for i, week in enumerate(weeks_dirs, start=1):
            print(f'{i} --> {week[-6:]}')

        try:
            choice = int(input("Enter the week number: "))
            if choice < 1 or choice > len(weeks_dirs):
                print("Invalid choice. Please enter a valid week number.")
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        path = weeks_dirs[choice - 1]
        print(f"Content of week {choice} in {self.chosen_month}:")

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                self._print_file_content(file_path)

    def read_files_from_chosen_month(self):
        """
        Reads and returns content from all files in the chosen month.
        :return: Dictionary with file content.
        """
        file_contents = {}

        for day_path in self.f_paths:
            day_key = f'{day_path[-12:-10]} {self.chosen_month}'
            file_contents[day_key] = {}

            try:
                if os.path.exists(day_path):
                    with open(day_path, 'r', encoding='UTF-8') as f:
                        lines = [line.strip() for line in f.readlines() if line.strip()]
                        file_contents[day_key] = {i + 1: line for i, line in enumerate(lines)}
                else:
                    print(f"File for {day_key} does not exist. Please create a schedule.")
            except OSError as e:
                print(f"File operation failed: {e}")

        return file_contents

    def _print_file_content(self, file_path):
        """
        Prints the content of a file.
        """
        print(f"{'-' * 10} Day {file_path[-12:-10]} {'-' * 10}")
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                for i, line in enumerate(lines, start=1):
                    print(f'{i}. {line}' if line else "(empty)")
        except OSError as e:
            print(f"Error reading file: {e}")