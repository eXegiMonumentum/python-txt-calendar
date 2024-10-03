from file_creator import FileCreator
from file_opener import FileOpener
from file_writer import FileWriter
from pprint import pprint


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
    # Display menu options
    print("1: Create txt files for chosen month")
    print("2: Write something to today's file")
    print("3: Check month progress")
    print("4: Check week progress")

    # Get user choice
    choice = get_user_choice()

    # Execute based on user choice
    if choice == 1:
        c_files = FileCreator(create_files=True)
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

#jutro rozwiążę kolejny problem:
# bład wynikający z tego że base_path potrzeba - ale nie mogę wywoływać w inicjalizatorze.