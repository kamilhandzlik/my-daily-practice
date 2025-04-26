from menu import Menu
from filemanager import FileManager, FileChooser


class ShowListOfThings:
    def __init__(self, things):
        self.things = things

    def display_list_of_things_todo(self):
        menu = Menu()
        file_name = FileChooser.choose_file()

        if file_name:
            open_file = FileManager(file_name)
        else:
            print("\033[31mNo file selected. Exiting...\033[0m")
            return

        menu.display_whats_in_the_file()
        user_choice = input(
            "\033[33mChoose option by entering number (or 'q' to quit): \033[0m\n"
        ).strip()

        show_menu = False

        while True:
            if show_menu:
                menu.display_show()

            if user_choice == "1":
                menu.display_whats_in_the_file()
                open_file.open_file_to_display()

            elif user_choice.lower() == "q":
                print("\033[32mReturning to main menu...\033[0m")
                break
            else:
                print(
                    f"\033[31mYou entered {user_choice}! That isn't correct value.\nChoose correct value between 1, 2\033[0m]"
                )

            user_choice = input(
                "\033[33mChoose option by entering number (or 'q' to quit): \033[0m\n"
            ).strip()


if __name__ == "__main__":
    things = None
    show_list = ShowListOfThings(things)
    show_list.display_list_of_things_todo()
