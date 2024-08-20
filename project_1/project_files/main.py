from file_creator import FileCreator
from file_opener import FileOpener
from file_writer import FileWriter
from pprint import pprint
from pathlib import Path


def validate_directory_path(path_str):
    """
    Validate if the given path is a directory and exists.

    :param path_str: Path to validate
    :return: A message indicating the result of validation
    """
    path = Path(path_str)
    if not path.exists():
        return f"Path '{path_str}' doesn't exist."

    if not path.is_dir():
        return f"The path '{path_str}' exists, but it's not a directory."

    return f"Path '{path_str}' is correct and it's a directory."


def get_valid_directory_path():
    """
    Prompts the user to enter a directory path and validates it.

    :return: A valid directory path
    """
    while True:
        base_path = input(
            "Enter the absolute path to your directory, where you want to create the Python planner: ")
        validation_message = validate_directory_path(base_path)
        print(validation_message)

        if "correct and it's a directory" in validation_message:
            return base_path
        else:
            print("Please enter a valid directory path.")


def get_user_choice():
    """
    Prompts the user to enter a choice and validates it.

    :return: A valid choice
    """
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4).")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    # Get and validate directory path
    base_path = get_valid_directory_path()

    # Display menu options
    print("1: Create txt files for chosen month")
    print("2: Write something to today's file")
    print("3: Check month progress")
    print("4: Check week progress")

    # Get user choice
    choice = get_user_choice()

    # Execute based on user choice
    if choice == 1:
        c_files = FileCreator()
        c_files.create_txt_files_for_chosen_month()

    elif choice == 2:
        w_files = FileWriter(current_month=True)
        w_files.file_content_management()
        w_files.read_todays_file()

    elif choice == 3:
        r_files = FileOpener()
        pprint(r_files.read_files_from_chosen_month())

    elif choice == 4:
        r_files = FileOpener(current_month=True)
        r_files.read_files_from_week_of_current_month()


if __name__ == "__main__":
    main()

# zmiana w projekcie:
# naprawię import error,- zmienną w file creator,-nie ma tej zmiennej w main.