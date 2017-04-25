import Inv_Statst
import Definitions


# Function that sets up start screen with naming your character
def start_screen():
    choice = None

    print("RPG-TEXT ADVENTURE")

    # Print a list of available options for the start screen while choice != 0
    while choice != "0":
        print("""
        0: Exit Game
        1: Start New Character
        """)

        choice = input("Please select an option: ")

        if choice == "0":
            print("Thanks for playing!")
            input("Press enter to exit.")
        elif choice == "1":
            name = input("Please enter a name for your character: ")
            print("Welcome,", name)
            print("\n")
            break
        else:
            print("That is not an available option. Try again.")


def town_screen(town):
    choice = ''
    print(town.description(town.name))
    print('What do you want to do?: ')

    while choice != '0':
        print(town)

        choice = input('Please select an option: ')

        if choice == '0':
            # leave_Town()
            pass

        elif choice <= str(len(town.npcs)) and choice != '0':


start_screen()
town_screen(Definitions.currTown)
