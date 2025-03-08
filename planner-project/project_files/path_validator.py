from pathlib import Path

class PathValidator:

    @staticmethod
    def validate_directory_path(base_path):
        """
        Validate if the given path is a directory and if it's exists.
        """
        path = Path(base_path)
        if not path.exists():
            return f"Path '{base_path}' doesn't exist!"
        if not path.is_dir():
            return f"{base_path} is not a directory!"
        return f"Correct directory path! {base_path}"

    def get_default_path(self):
        # Ścieżka nadrzędna
        parent_path = Path(__file__).parent.parent  # jeden poziom wyżej niż katalog, w którym znajduje się skrypt
        default_path = parent_path / 'created_planner'

        if not default_path.exists():
            default_path.mkdir()
            print(f"Directory '{default_path}' created.")
        else:
            print(f"Directory '{default_path}' already exists!")

        return default_path

    def get_valid_directory_path(self, base_path='created_planner'):
        """
        Prompts the user to enter a directory path and validates it.
        """
        base_path = Path(base_path)

        if not base_path.exists():
            while True:
                base_path_input = input(
                    "Enter the absolute path to your directory, or press Enter to use the default path: ")

                if not base_path_input:
                    base_path = self.get_default_path()
                    print(f"Python planner created at {base_path}")
                    break

                validation_message = self.validate_directory_path(base_path_input)
                print(validation_message)

                if "Correct directory path" in validation_message:
                    base_path = Path(base_path_input)
                    return base_path / 'created_planner'
                else:
                    print("Invalid directory path!")

        return base_path
