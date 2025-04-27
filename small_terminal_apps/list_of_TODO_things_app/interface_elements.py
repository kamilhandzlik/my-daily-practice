class InterfaceElements:
    def display_logo(self):
        print("\n")
        print("\033[36m")
        print("   _____________________________________________________")
        print("  /                                                     \\")
        print(" |   __  __       _       _                             |")
        print(" |  |  \\/  | __ _| |_ ___| |__   ___                    |")
        print(" |  | |\\/| |/ _` | __/ __| '_ \\ / _ \\                   |")
        print(" |  | |  | | (_| | || (__| | | |  __/                   |")
        print(" |  |_|  |_|\\__,_|\\__\\___|_| |_|\\___|                   |")
        print(" |                                                      |")
        print(" |                    TODO App                          |")
        print("  \\_____________________________________________________/")
        print("\033[0m")
        print("\n")

    def display_separator(self):
        print("\033[33m" + "=" * 56 + "\033[0m")

    def display_main_menu_header(self):
        print("\033[36m")
        print("   _______________")
        print("  |               |")
        print("  |   MAIN MENU   |")
        print("  |_______________|")
        print("\033[0m")

    def display_show_menu_header(self):
        print("\033[36m")
        print("   ____________________")
        print("  |                    |")
        print("  |   FILE SELECTION   |")
        print("  |____________________|")
        print("\033[0m")

    def display_file_content_menu_header(self):
        print("\033[36m")
        print("   __________________________")
        print("  |                          |")
        print("  |   FILE CONTENT OPTIONS   |")
        print("  |__________________________|")
        print("\033[0m")

    def display_add_menu_header(self):
        print("\033[36m")
        print("   ________________")
        print("  |                |")
        print("  |   ADD TO FILE  |")
        print("  |________________|")
        print("\033[0m")

    def display_add_file_header(self):
        print("\033[36m")
        print("   _______________")
        print("  |               |")
        print("  |   ADD  FILE   |")
        print("  |_______________|")
        print("\033[0m")

    def display_delete_file_header(self):
        print("\033[36m")
        print("   _______________")
        print("  |               |")
        print("  |  DELETE FILE  |")
        print("  |_______________|")
        print("\033[0m")

    def display_rename_file_header(self):
        print("\033[36m")
        print("   _______________")
        print("  |               |")
        print("  |  RENAME FILE  |")
        print("  |_______________|")
        print("\033[0m")
