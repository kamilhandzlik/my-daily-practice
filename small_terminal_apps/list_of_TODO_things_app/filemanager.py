import os
from menu import Menu


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def open_file_to_display(self):
        try:
            file_path = os.path.join(self.base_dir, self.filename)
            with open(file_path, "r") as file:
                things = file.readlines()
                for idx, thing in enumerate(things, start=1):
                    print(f"\033[33m{idx}. {thing.strip()}\033[0m")
        except FileNotFoundError:
            print("\033[31mFile not found. Please make sure the file exists.\033[0m\n")

    def add_to_file(self):
        try:
            file_path = os.path.join(self.base_dir, self.filename)
            with open(file_path, "a+") as file:
                # showing whats in the file
                file.seek(0)
                print("\033[34mCurrent file contents:\033[0m")
                print(file.read())

                # adding new thing to the file
                print("\033[33mEnter q to abort adding new thing.\n\033[0m")
                new_thing = str(
                    input("\033[33mEnter new thing to add: \033[0m\n")
                ).strip()

                if new_thing.lower() == "q":
                    print("\033[32mExiting...\033[0m\n")
                    return

                if new_thing:
                    file.write(new_thing + "\n")
                    print(f"\033[32mAdded '{new_thing}' to the file.\033[0m")
                else:
                    print(
                        "\033[31mYou entered empty string. Please enter a valid thing.\033[0m\n"
                    )

        except FileNotFoundError:
            print("\033[31mFile not found. Please make sure the file exists.\033[0m\n")

    def delete_from_file(self):
        try:
            file_path = os.path.join(self.base_dir, self.filename)
            with open(file_path, "r") as file:
                things = file.readlines()

            if not things:
                print("\033[31mThe file is empty. Nothing to delete.\033[0m\n")
                return

            print("\033[34mCurrent file contents:\033[0m")
            for idx, thing in enumerate(things, start=1):
                print(f"\33[33m{idx}. {thing.strip()}\33[0m")

            while True:
                user_choice = input(
                    "\033[33mEnter the number of the item to delete (or 'q' to quit): \033[0m\n"
                ).strip()

                if user_choice.lower() == "q":
                    print("\033[32mExiting...\033[0m\n")
                    return

                if user_choice.isdigit() and 1 <= int(user_choice) <= len(things):
                    index_to_delete = int(user_choice) - 1
                    deleted_item = things.pop(index_to_delete).strip()
                    print(f"\033[32mDeleting '{deleted_item}' from the file.\033[0m")
                    break
                else:
                    print(
                        f"\033[31mInvalid choice: {user_choice}. Please choose a valid number.\033[0m\n"
                    )
            print(f"Modified contents to save: {things}")
            print(f"Saving changes to: {file_path}")

            with open(file_path, "w") as file:
                file.writelines(things)
            print("\033[32mFile updated successfully.\033[0m\n")

            with open(file_path, "r") as file:
                print(f"File contents after save: {file.read()}")

        except FileNotFoundError:
            print("\033[31mFile not found. Please make sure the file exists.\033[0m\n")
            return
        except Exception as e:
            print(f"\033[31mAn unexpected error occurred: {e}\033[0m\n")


class FileChooser:
    def __init__(self, filename):
        self.filename = filename
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def display_files():
        menu = Menu()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        show_menu = True
        files = [f for f in os.listdir(base_dir) if f.endswith(".txt")]

        if not files:
            print("\033[31mNo .txt files found in the current directory.\033[0m\n")
        else:
            if show_menu:
                menu.display_show()
            print("\033[34mAvailable .txt files:\033[0m\n")
            for idx, file in enumerate(files, 1):
                print(f"\033[36m{idx}. {file}\033[0m")
            show_menu = False
        return files

    @staticmethod
    def choose_file():
        files = FileChooser.display_files()

        if not files:
            return None

        while True:
            user_choice = input(
                "\033[33mChoose option by entering number (or 'q' to quit): \033[0m\n"
            ).strip()
            if user_choice.lower() == "q":
                print("\033[32mExiting file chooser.\033[0m\n")
                break
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(files):
                chosen_file = files[int(user_choice) - 1]
                print(f"\033[32mYou chose: {chosen_file}\033[0m\n")
                return chosen_file
            else:
                print(
                    f"\033[31mInvalid choice: {user_choice}. Please choose a valid number.\033[0m\n"
                )
