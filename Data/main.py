import Inv_Stat
import Definitions
import NPCFunctions


# Function that sets up start screen with naming your character
def start_screen():
    choice = None

    print("RPG-TEXT ADVENTURE")
    print("\nBY BRENDAN KAILUKAITIS")

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


start_screen()
