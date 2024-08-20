from file_creator import FileCreator
import os
class FileOpener(FileCreator):

    def __init__(self, current_month=None):
        super().__init__(current_month)
        self.f_paths = self.create_paths_for_days_txt_files()
        self.todays_path = self.f_paths[self.current_day_int - 1]

    def read_todays_file(self):
        if self.current_month is not True:
            raise ValueError(f"Function read today's file only supports opening today's file when current_month=True.")

        print("It's today's file content:\n",20*"-")
        file_content_list = []
        try:
            with open(self.todays_path, 'r', encoding='UTF-8') as f:
                file_content = f.read()
                for i, line in enumerate(file_content.split("\n")):
                    if line:
                        file_content_list.append(line.strip())
                        print(f'line {i+1}: {line}')
                print(20*"-")
                return file_content_list
        except FileNotFoundError as e:
            print(f"Error opening file: {e}")
            return None
        except OSError as e:
            print(f"File operation failed due to system-related errors.: {e}")
            return None

    def read_files_from_week_of_current_month(self):
        if not self.current_month or self.current_month is None:
            raise ValueError("Function read_files_from_week_of_current_month can only be used when current_month=True.")

        _, weeks_dirs = self.creating_chosen_month_and_weeks_directionaries()
        print(f"Choose a week of {self.chosen_month} you want to check:")
        for i, week in enumerate(weeks_dirs, start=1):
            print(f'{i} --> {week[-6:]}')

        choice = int(input("Enter the number of the week: "))
        if choice < 1 or choice > len(weeks_dirs):
            print("Invalid choice. Please choose a valid week number.")
            return

        path = weeks_dirs[choice - 1]
        print(f"Contents of {choice} week of {self.chosen_month}")
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                with open(file_path, 'r', encoding="UTF-8") as file:
                    file_content = file.read()
                    # if file_content:
                    file_content = file_content.strip()
                    file_content = file_content.split("\n")
                    print(10*"-", "Day" ,file_path[-12:-10], 10*"-", )
                    for i, line in enumerate(file_content, start=1):
                        if line:
                            print(f'{i}. {line}')
                        else:
                            print("empty ")

    def read_files_from_chosen_month(self):
        f_content_dict = {}
        for i, day in enumerate(self.f_paths, start=1):
            key1 = f'{day[-12:-10]} {self.chosen_month}'
            f_content_dict[key1] = {}
            try:
                with open(day, 'r', encoding='UTF-8') as f:
                    file_content = f.read()
                    if file_content and os.path.exists(day):
                        file_content = file_content.strip()
                        file_content = file_content.split("\n")

                        for index, single_line in enumerate(file_content, start=1):
                            f_content_dict[key1][index] = single_line
                    else:
                        print(f"file for day {i} is empty")

            except FileNotFoundError as e:
                print(f"File from day {i} Does not exist.-- {e}")
            except OSError as e:
                print(f"File operation failed due to system-related errors.: {e}")

        return f_content_dict

