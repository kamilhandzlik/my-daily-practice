from interface_elements import InterfaceElements


class Menu:
    def __init__(self):
        self.interface = InterfaceElements()

    def display_main(self):
        self.interface.display_separator()
        self.interface.display_logo()
        self.interface.display_main_menu_header()
        self.interface.display_separator()
        print("\n")
        print("\033[34mWelcome to the TODO list application!\033[0m")
        print("\033[35m1. Show things to do.\033[0m")
        print("\033[35m2. Create file.\033[0m")
        print("\033[35m3. Delete file.\033[0m")
        print("\033[35m4. Rename todo file.\033[0m")
        print("\033[35m5. Press q or 5 to exit application.\033[0m")
        print(
            "\033[35mChose option by pressing one of the options 1, 2, 3, 4, 5\033[0m"
        )
        self.interface.display_separator()
        print("\n")

    def display_show(self):
        self.interface.display_separator()
        self.interface.display_show_menu_header()
        self.interface.display_separator()
        print(
            "\033[35m1. Choose one of the files by typing their index number example 1: .\033[0m"
        )
        print("\033[35m2. Press q to go to main menu\033[0m\n")
        self.interface.display_separator()
        print("\n")

    def display_whats_in_the_file(self):
        self.interface.display_separator()
        self.interface.display_file_content_menu_header()
        self.interface.display_separator()
        print("\033[35m\n1. Display whats in the file.\033[0m")
        print("\033[35m2. Display content of file and ADD new things to file.\033[0m")
        print("\033[35m3. Display content of file and DELETE from file.\033[0m")
        print("\033[35m4. Press q to go to main menu\033[0m\n")
        print("\033[35mChose option by pressing one of the options 1, 2, 3, q\033[0m")
        self.interface.display_separator()
        print("\n")

    def display_add(self):
        self.interface.display_separator()
        self.interface.display_add_menu_header()
        self.interface.display_separator()
        print("\033[35m1. Display whats in the file.\033[0m")
        print("\033[35m1. Add to file.\033[0m")
        print("\033[35m2. Press q to go to main menu\033[0m\n")
        print("\033[35mChose option by pressing one of the options 1, 2, q\033[0m")
        self.interface.display_separator()
        print("\n")
