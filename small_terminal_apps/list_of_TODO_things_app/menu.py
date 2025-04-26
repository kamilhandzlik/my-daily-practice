class Menu:
    def display_main(self):
        print("\n")
        print("\033[34mWelcome to the TODO list application!\033[0m")
        print("\033[35m1. Show things to do\033[0m")
        print("\033[35m2. Add thing todo\033[0m")
        print("\033[35m3. delete thing todo\033[0m")
        print("\033[35m4. Change thing todo\033[0m")
        print("\033[35m5. Press q to exit application\033[0m")
        print("\n")
        print(
            "\033[35mChose option by pressing one of the options 1, 2, 3, 4, 5\033[0m"
        )
        print("\n")

    def display_show(self):
        print("\033[35m1. Show things to do\033[0m")
        print("\033[35m2. Press q to go to main menu\033[0m\n")
        print("\033[35mChose option by pressing one of the options 1, q\033[0m")
        print("\n")
