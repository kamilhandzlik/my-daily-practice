import os
from filemanager import FileChooser


class FileRenamer:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def rename_file(self):
        files = FileChooser.display_files()

        if not files:
            print("\033[31mNo available files to rename.\033[0m")
            return

        while True:
            user_choice = input(
                "\033[33mChoose a file to rename by entering its number (or 'q' to quit): \033[0m\n"
            ).strip()
            if user_choice.lower() == "q":
                print("\033[32mExiting file renamer.\033[0m\n")
                break

            if user_choice.isdigit() and 1 <= int(user_choice) <= len(files):
                chosen_file = files[int(user_choice) - 1]
                print(f"\033[32mYou chose: {chosen_file}\033[0m")
                break
            else:
                print(
                    f"\033[31mInvalid choice: {user_choice}. Please choose a valid number.\033[0m"
                )

        new_name = input(
            "\033[33mEnter the new name for the file (with .txt extension): \033[0m\n"
        ).strip()

        if not new_name.endswith(".txt"):
            print("\033[31mError: The new file name must end with '.txt'.\033[0m")
            return

        old_path = os.path.join(self.base_dir, chosen_file)
        new_path = os.path.join(self.base_dir, new_name)

        try:
            os.rename(old_path, new_path)
            print(
                f"\033[32mFile renamed successfully from '{chosen_file}' to '{new_name}'.\033[0m"
            )
        except FileExistsError:
            print(
                f"\033[31mError: A file with the name '{new_name}' already exists.\033[0m"
            )
        except FileNotFoundError:
            print(
                f"\033[31mError: The file '{chosen_file}' was not found. It may have been moved or deleted.\033[0m"
            )
        except Exception as e:
            print(f"\033[31mAn unexpected error occurred: {e}\033[0m")
