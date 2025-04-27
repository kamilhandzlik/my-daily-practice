import os
from filemanager import FileChooser
from interface_elements import InterfaceElements


class FileCreator:
    def __init__(self, base_dir="."):
        self.base_dir = base_dir
        self.interface = InterfaceElements()

    def create_new_file(self):
        self.interface.display_separator()
        self.interface.display_add_file_header()
        self.interface.display_separator()
        print("\033[34mChecking existing .txt files in the directory...\033[0m\n")
        FileChooser.display_files_simple()

        print(
            "\033[33mEnter the name of the new file (without extension) or 'q' to cancel:\033[0m"
        )
        file_name = input().strip()

        if file_name.lower() == "q":
            print("\033[32mFile creation aborted.\033[0m")
            return

        if not file_name:
            print(
                "\033[31mNo file name entered or entred name was improper. Please try again.\033[0m"
            )
            return None

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join(self.base_dir, file_name)

        if os.path.exists(file_path):
            print(
                f"\033[31mFile '{file_name}' already exists. Choose a different name.\033[0m"
            )
            return None

        try:
            with open(file_path, "w") as file:
                file.write("")
            print(f"\033[32mFile '{file_name}' created successfully.\033[0m")
            return file_name
        except Exception as e:
            print(f"\033[31mAn error occurred while creating the file: {e}\033[0m")
            return None
