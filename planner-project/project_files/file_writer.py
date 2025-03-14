from file_opener import FileOpener


class FileWriter(FileOpener):
    """
    Class responsible for writing and managing content in planner files.
    """
    def __init__(self):
        super().__init__(current_month=True)
        self.duties_list = []

    def __write_lines_to_file(self, added_lines_list, file_content_list):
        """
        Appends lines to today's file, ensuring no duplicates.
        """
        try:
            with open(self.today_path, "a+", encoding="UTF-8") as f:
                for line in added_lines_list:
                    if line not in file_content_list:
                        f.write(line + '\n')
                        print(f"{line} was written to file {self.today_path}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except OSError:
            print("File operation failed due to system-related errors.")

    def __delete_lines_from_file(self):
        """
        Deletes a specified line from today's file.
        """
        file_content_list = self.read_today_file()
        if not file_content_list:
            print("File is empty or does not exist.")
            return

        try:
            line_number = int(input("Enter the line number to delete: "))
            if line_number < 1 or line_number > len(file_content_list):
                print("Invalid line number.")
                return

            deleted_line = file_content_list.pop(line_number - 1)
            print(f"Deleted line: {deleted_line}")

            with open(self.today_path, "w", encoding="UTF-8") as f:
                f.writelines(f"{line}\n" for line in file_content_list)
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except OSError:
            print("File operation failed due to system-related errors.")

    def file_content_management(self):
        """
        Manages writing and deleting content from today's file.
        """
        print("Writing duties to a file")
        print("""Command palette:
        ---> Type your text to add
        ---> Type 'Exit' to exit
        ---> Type 'Del' to delete a line""")

        added_lines_list = []
        file_content_list = self.read_today_file() or []

        while True:
            text = input("Enter text: ").strip().capitalize()

            if text and text not in ("Del", "Exit"):
                added_lines_list.append(text)
                print("Newly added lines:", added_lines_list)
                self.__write_lines_to_file(added_lines_list, file_content_list)
            elif text == "Del":
                self.__delete_lines_from_file()
            elif text == "Exit":
                print("Exiting.")
                break