from pathlib import Path


class PathValidator:

    @staticmethod
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

    @staticmethod
    def get_valid_directory_path():
        """
        Prompts the user to enter a directory path and validates it.

        :return: A valid directory path
        """
        while True:
            base_path = input(
                "Enter the absolute path to your directory, where you want to create the Python planner: ")
            if '"' in base_path:
                base_path = base_path.replace('"', '')

            validation_message = PathValidator.validate_directory_path(base_path)
            print(validation_message)

            if "correct and it's a directory" in validation_message:
                return base_path
            else:
                print("Please enter a valid directory path.")