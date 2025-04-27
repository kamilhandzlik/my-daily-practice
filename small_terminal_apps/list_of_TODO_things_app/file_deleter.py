import os
from filemanager import FileChooser
from interface_elements import InterfaceElements


class FileDeleter:
    def __init__(self, base_dir="."):
        self.base_dir = base_dir
        self.interface = InterfaceElements()

    def delete_file(self):
        self.interface.display_separator()
        self.interface.display_delete_file_header()
        self.interface.display_separator()
        print("\033[34mChecking existing .txt files in the directory...\033[0m\n")
        list_of_files = FileChooser.display_files_simple()

        if not list_of_files:
            print("\033[31mThere are no txt files to delete. Exiting...\033[0m")
            return

        print(
            "\033[33mEnter the index of the file you want to delet or 'q' to cancel:\033[0m"
        )
        user_input = input().strip()

        if user_input.lower() == "q":
            print("\033[32mFile creation aborted.\033[0m")
            return

        if not user_input.isdigit():
            print(
                "\033[31mInvalid input. Please enter a number. (Index of file you want to delete.)\033[0m"
            )
            return

        index = int(user_input) - 1

        if index < 0 or index >= len(list_of_files):
            print("\033[31mInvalid index. Please select a correct number.\033[0m")
            return

        file_name = list_of_files[index]
        file_path = os.path.join(self.base_dir, file_name)

        try:
            os.remove(file_path)
            print(f"\033[32mFile '{file_name}' deleted successfully.\033[0m")
        except Exception as e:
            print(f"\033[31mAn error occurred while deleting the file: {e}\033[0m")
