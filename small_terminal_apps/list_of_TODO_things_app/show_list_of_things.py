from menu import Menu

class ShowListOfThings:
    def __init__(self, things):
        self.things = things

    def open_file(self):
        try:
            with open('list_of_things_todo.txt', 'r') as file:
                things = file.readlines()
                for idx, thing in enumerate(things, start=1):
                    print(f"\033[33m{idx}. {thing.strip()}\033[0m]]")
        except FileNotFoundError:
            print("\033[31mFile not found. Please make sure the file exists.\033[0m]")
    

    def display_list_of_things_todo(self):
        menu = Menu()
        menu.display_show()
        user_choice = str(input("Chooce option by entering number: "))

        while True:
            menu.display_show()

            if user_choice == '1':
                self.open_file()
            elif user_choice == '2':
                print("\033[32mReturning to main menu...\033[0m")
                break
            else:
                print(f"\033[31mYou entered {user_choice} choose correct value between 1, 2\033[0m]")

            user_choice = str(input("Chooce option by entering number: "))


if __name__ == "__main__":
    things = None  
    show_list = ShowListOfThings(things)
    show_list.display_list_of_things_todo()
        
