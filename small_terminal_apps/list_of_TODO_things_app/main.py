from menu import Menu
from show_list_of_things import ShowListOfThings
from file_creator import FileCreator
from file_deleter import FileDeleter
from file_renamer import FileRenamer


class MainLoop:
    def __init__(self):
        menu = Menu()

        while True:
            menu.display_main()
            user_choice = str(
                input(
                    "\033[33mChoose option by entering number (or 'q' to quit): \033[0m\n"
                )
            ).strip()

            if user_choice == "1":
                show_list = ShowListOfThings(things=None)
                show_list.display_list_of_things_todo()
            elif user_choice == "2":
                create_file = FileCreator()
                create_file.create_new_file()
            elif user_choice == "3":
                delete_file = FileDeleter()
                delete_file.delete_file()
            elif user_choice == "4":
                rename_file = FileRenamer()
                rename_file.rename_file()
            elif user_choice.lower() == "q" or user_choice == "5":
                print("\033[32mExiting the application...\033[0m")
                break
            else:
                print(
                    f"\033[31mYou entered {user_choice}! That isn't correct value.\nChoose correct value between 1, 2, 3, 4, 5\033[0m\n"
                )


if __name__ == "__main__":
    MainLoop()
