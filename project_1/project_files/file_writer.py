
from file_opener import FileOpener


class FileWriter(FileOpener):

    def __init__(self, base_path=r"C:\Users\LENOVO\Desktop\first_project_planner\project_1\created_planner", current_month=False):
        super().__init__(base_path, current_month)
        self.duties_list = []

    def __write_lines_to_file(self, added_lines_list, file_content_list):
        try:
            with open(self.todays_path, "a+", encoding="UTF-8") as f:
                for line in added_lines_list:
                    if line not in file_content_list:
                        f.write(line + '\n')
                print(f"{line} was written to a file {self.todays_path}\n")
        except OSError:
            print("File operation failed due to system-related errors.")

        except FileNotFoundError as e:
            print(f"wrong path: {e}")

    def __delete_lines_from_file(self):
        file_content_list = self.read_todays_file()
        try:
            line_number = int(input("Enter the line number to delete "))

            if line_number < 1 or line_number > len(file_content_list):
                print("Invalid line number.")
                return

            deleted_lines = [file_content_list.pop(line_number - 1)]
            print("Deleted lines:", deleted_lines)

            with open(self.todays_path, "w", encoding="UTF-8") as f:
                for line in file_content_list:
                    f.write(line + "\n")

        except ValueError:
            print("Invalid line number (please enter an integer).")
        except OSError:
            print("File operation failed due to system-related errors.")
        except FileNotFoundError as e:
            print(f"Wrong path: {e}")

        for i, line in enumerate(file_content_list, start=1):
            print(f'line: {i}: {line}')

    def file_content_management(self):
        """ write duties from list to file, without duplicates"""
        print("writing duties to a file")
        print("Comand palette:\n---> write: Exit to exit\n---> write Del to delete lines")
        added_lines_list = []
        file_content_list = self.read_todays_file()
        while True:
            tekst = input("enter text: ")
            if tekst == "exit" or tekst == "Exit":
                break

            elif tekst != "Del" and tekst != "del":
                added_lines_list.append(tekst.strip())
                print("newly added lines", added_lines_list)
                self.__write_lines_to_file(added_lines_list, file_content_list)

            else:
                tekst == "Del" or tekst == "del"
                self.__delete_lines_from_file()






