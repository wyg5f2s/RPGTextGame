
import Definitions
import Classes


# Add up all total values for each character stat
def update_char_stats(item, charStats):
    # Checks if item has specific attribute and is equipped
    if item.itemType == "Weapon" and item.isEquipped:

        # Add item's stat value to player's current stats
        charStats["Damage"] += item.damage

    elif item.itemType == "Armor" and item.isEquipped:
        charStats["Armor"] += item.armor

    # Updates player's global stats.
    return charStats


# Equip/unequip item funtion
def equip_unequip_item(item):
    choice = None

    while choice != "1" and choice != "2":

        # Checks if item is equipped/unequipped
        if item.isEquipped:
            print("\nWould you like to unequip this item?: ")
        elif not item.isEquipped:
            print("\nWould you like to equip this item?: ")

        print("""
        1: Yes
        2: No
        """)

        choice = input("Please make a selection: ")

        # Checks the choice entered and calls equip/unequip function
        if choice == "1":
            Classes.Inventory.equip_Unequip_Item(item, item)
        elif choice == "2":
            break
        else:
            print("\nThat is not an available option. Please try again.")


# Function that selects item players chooses.
def select_item(item):
    print(Definitions.item_desc(item.name, item.itemType))

    # Checks the item type of the item
    if item.itemType == "Weapon":
        print("\nDamage: +", item.damage)

    elif item.itemType == "Armor":
        print("\nArmor: +", item.armor)

    # Calls the unequip/equip function and passes it the current item
    equip_unequip_item(item)

    # Updates the players stats
    update_char_stats(item, Definitions.charStats)


# Function lists items in inventory, equip/unequip said items, and list stats
def item_list(inventory):
    choice = None

    print("\nWelcome to your inventory")

    while choice != 0:
        print("""
        0: Exit Inventory
        1: Examine and Equip Items
        2: List Current Stats
        """)

        choice = input("Please select an option: ")

        if choice == "0":
            break

        elif choice == "1":

            itmchoice = None

            while itmchoice != "0":
                print(inventory)

                # Prompts the user to make a selection
                itmchoice = input("\nSelect an item to examine: ")

                # Checks the number user enter, selects item or exits screen.
                if itmchoice == "0":
                    break

                # Prints out a description and corresponding stat for item
                elif itmchoice <= str(len(inventory.items)) and itmchoice > "0":
                    select_item(inventory.items[int(itmchoice)])

                else:
                    print("That is not an available option. Please try again.")

        # Prints each stat and its respective value
        elif choice == "2":
            for stat in Definitions.charStats:
                print("\n", "\nTotal", stat + ":", Definitions.charStats[stat])
