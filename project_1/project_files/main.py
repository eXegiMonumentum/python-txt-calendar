from file_creator import FileCreator
from file_opener import FileOpener
from file_writer import FileWriter
from pprint import pprint


base_path = r"C:\Users\LENOVO\Desktop\first_project_planner\project_1\created_planner"
duties_list = []



print("1/2/3/4")
print("Enter what do you want to do: ")
print("1: Create txt files for chosen month")
print("2 : Write sth to today's file")
print("3 : Check month progress")
print("4 : Check week progress")

choice = int(input("Enter your choice: "))

if choice == 1:
    c_files = FileCreator()
    c_files.create_txt_files_for_chosen_month()

if choice == 2:
    w_files = FileWriter(current_month=True)
    w_files.file_content_management()
    w_files.read_todays_file()

elif choice == 3:
    r_files = FileOpener()
    pprint(r_files.read_files_from_chosen_month())

elif choice == 4:
    r_files = FileOpener(current_month=True)
    r_files.read_files_from_week_of_current_month()

# zmiana w projekcie:
# użytkownik wprowadza w main za pomocą input ; swoją ścieżkę, na której chce utwrzyć python_planner -
# czyli podzielić miesiąc na dokumenty tekstowe na określony dzień - w których może zapisywać co zrobił, co się nauczył :)