from pathlib import Path

class PathValidator:

    @staticmethod
    def _validate_directory_path(base_path):
        """
        Validate if the given path is a directory and if it exists.
        """
        path = Path(base_path)
        if not path.exists():
            return f"Path '{base_path}' doesn't exist!"
        if not path.is_dir():
            return f"'{base_path}' is not a directory!"
        return f"Correct directory path: {base_path}"

    @staticmethod
    def _create_directory(base_path):
        """ Creates directory 'created_planner' if it doesn't exist. """

        base_path = Path(base_path)  # Niepotrzebne sprawdzanie `isinstance()`

        try:
            base_path.mkdir()
            print(f"Directory '{base_path}' created (or already exists).")
        except FileExistsError:
            if base_path.is_file():
                print(f"Error: A file named '{base_path}' already exists. Deleting it...")
                base_path.unlink()  # Usuwa plik
                base_path.mkdir()  # Tworzy katalog po usunięciu pliku
                print(f"Directory '{base_path}' created after deleting the file.")
            else:
                print(f"Directory '{base_path}' already exists.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return base_path

    def get_valid_directory_path(self):
        """
        Prompts the user to enter a directory path and validates it.
        """
        parent_path = Path.cwd().parent
        base_path = parent_path / 'created_planner'

        while True:
            base_path_input = input(
                "Enter the absolute path to your directory, or press Enter to use the default path: "
            ).strip()

            if not base_path_input:  # Jeśli użytkownik wcisnął Enter
                base_path = self._create_directory(base_path)
                print(f"Python planner created at {base_path}")
                return base_path

            validation_message = self._validate_directory_path(base_path_input)
            print(validation_message)

            if "Correct directory path" in validation_message:
                return Path(base_path_input) / 'created_planner'
            else:
                print("Invalid directory path! Please try again.")
