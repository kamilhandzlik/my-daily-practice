from menu import Menu
from show_list_of_things import ShowListOfThings


class MainLoop:
    def __init__(self):
        menu = Menu()
        menu.display_main()
        user_choice = str(input("Chooce option by entering number: "))

        while True:
            if user_choice == "1":
                print("\nYou selected option 1.\n")
                show_list = ShowListOfThings(things=None)
                show_list.display_list_of_things_todo()
            elif user_choice == "2":
                print("\nYou selected option 2.")
            elif user_choice == "3":
                print("\nYou selected option 3.")
            elif user_choice == "4":
                print("\nYou selected option 4.")
            elif user_choice.lower() == "q":
                print("\033[32mExiting the application...\033[0m")
                break
            else:
                print(
                    f"\033[31mYou entered {user_choice}! That isn't correct value.\nChoose correct value between 1, 2, 3, 4, 5\033[0m]\n"
                )

            menu.display_main()
            user_choice = str(input("Chooce option by entering number: "))


if __name__ == "__main__":
    MainLoop()
