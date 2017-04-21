
import Definitions


def ask_for_work(currTown):
    """if currTown == "Wallowdale":
        # Do stuff
    if currTown == "Hampstead":
        # Do stuff
    if currTown == "Stawford":
        # Do stuff
    if currTown == "Millstone":
        # Do stuff
    if currTown == "Silverkeep":
        # Do stuff
    """
    print("Work")


def npc_actions(choice, townOptions):
    print(townOptions)
    if townOptions[choice] == "Ruler":
        print(" # Call the Talk to ruler function")

    elif townOptions[choice] == "Work":
        ask_for_work(Definitions.currTown)

    elif townOptions[choice] == "Merchant":
        print("# Call the Merchant function")
