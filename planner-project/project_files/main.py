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
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))
            if choice in [1, 2, 3, 4, 5, 6]:
                return choice
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """
    Main function to handle user input and execute appropriate actions.
    """
    while True:
        print(20*"-")
        print("1: Read today's file")
        print("2: Write something to today's file")
        print("3: Check progress for chosen month")
        print("4: Check progress for current month")
        print("5: Check progress for chosen week in current month")
        print("6: Plann your month !")


        choice = get_user_choice()

        if choice == 1:
            r_files = FileOpener(current_month=True)
            r_files.read_today_file()

        elif choice == 2:
            w_files = FileWriter()
            w_files.file_content_management()
        elif choice == 3:
            r_files = FileOpener(current_month=False)
            pprint(r_files.read_files_from_chosen_month())
        elif choice == 4:
            r_files = FileOpener(current_month=True)
            pprint(r_files.read_files_from_chosen_month())
        elif choice == 5:
            r_files = FileOpener(current_month=True)
            r_files.read_files_from_week_of_current_month()
        elif choice == 6:
            c_files = FileCreator(create_files=True)
            c_files.create_txt_files_for_chosen_month()

if __name__ == "__main__":
    main()



