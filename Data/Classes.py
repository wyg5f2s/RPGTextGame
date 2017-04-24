import Definitions


def inventory_Menu():
    print('\nInv: Access your inventory' + '\t' + 'Menu: Access menu')


class Item():
    """Class that creates a new item for player(Weapon, armor, card, etc)"""

    def __init__(self, name, itemType, stats, isEquipped):
        self.name = name
        self.itemType = itemType
        self.stats = []
        self.isEquipped = isEquipped

        if itemType == 'Weapon':
            self.damage = stats[0]

        elif itemType == 'Armor':
            self.armor = stats[0]

    def __str__(self, name):
        return Definitions.itemDesc[name]


class Inventory():
    """Creates Player's inventory and enables adding/deleting,
        equipping/unequipping, and printing current items"""

    def __init__(self):
        self.items = []
        self.items.append('Exit')

    def add_Item(self, item):
        self.items.append(item)

    def delete_Item(self, item):
        self.items.remove(item)

    def equip_Unequip_Item(self, item):
        if item.isEquipped:
            item.isEquipped = False

        elif not item.isEquipped:
            for x, invItem in enumerate(self.items):

                while True:
                    if self.items[x].isEquipped:
                        print('You already have ' + invItem.name + ' Equipped')
                        print('Do you want to equip new item or keep old one?')

                        print("""
                        1: Equip
                        2: Keep
                        """)

                        choice = input('Please select an option: ')

                        if choice == '1':
                            self.items[x].isEquipped = False
                            item.isEquipped = True
                            break

                        elif choice == '2':
                            break

                        else:
                            print('That is not an option. Try again.')

                    elif not self.items[x].isEquipped:
                        item.isEquipped = True
                        break

    def __str__(self):
        out = ''
        for x, item in enumerate(self.items):
            if self.items[x] == 'Exit':
                out += '\n' + '\t' + str(x) + ': ' + self.items[x]

            elif self.items[x].isEquipped:
                out += '\n' + '\t' + str(x) + ': ' + item.name + ' -Equipped'

            elif not self.items[x].isEquipped:
                out += '\n' + '\t' + str(x) + ': ' + item.name
        return out


class Npc():
    """Creates a new Npc"""

    def __init__(self, npcType, name, hasQuest):
        self.npcType = npcType
        self.name = name
        self.hasQuest = hasQuest

    def npc_Functions(self, npcType):
        if npcType == 'Priest':
            print(Npc)
            # ask_For_Work()
        elif npcType == 'Merchant':
            print(Npc)
            # vist_the_Merchant()

    def __str__(self, name):
        return Definitions.npcDesc[name]


class Town():
    """Creates a town and enables adding/delete npc to a town
    and printing npc actions"""

    def __init__(self, name):
        self.town = []
        self.town.append('Leave Town')
        self.name = name
        self.townConnections = []
        self.townConnections.append('Enter Town')

    def add_Connection(self, connection):
        self.townConnections.append(connection)

    def delete_Connection(self, connection):
        self.townConnections.remove(connection)

    def add_Npc(self, npc):
        self.town.append(npc)

    def delete_Npc(self, npc):
        self.town.remove(npc)

    def __str__(self):
        out = ''
        for x, npc in enumerate(self.town):
            if self.town[x] == 'Leave Town':
                out += '\n' + str(x) + ': ' + self.town[x]

            elif self.town[x].npcType == 'Priest':
                out += '\n' + str(x) + ': ' + 'Talk to the Priest'

            elif self.town[x].npcType == 'Merchant':
                out += '\n' + str(x) + ': ' + 'Visit the Merchant'

            elif self.town[x].npcType == 'Ruler':
                out += '\n' + str(x) + ': ' + 'Discuss with the Ruler'
                inventory_Menu()
        return out

    def description(self, name):
        return Definitions.townDesc[name]


class TownMasterList():
    """Creates a class for managing the towns and adding/deleting them to a list
    also allow the printing of different towns to visit."""

    def __init__(self):
        self.townMasterList = []

    def add_Town(self, town):
        self.townMasterList.append(town)

    def delete_Town(self, town):
        self.townMasterList.remove(town)

    def __str__(self):
        out = ''
        for x, town in enumerate(Town.townConnections):
            if Town.townConnections[x] == 'Enter Town':
                out += '\n' + str(x) + ': ' + Town.townConnections[x]

            else:
                out += '\n' + str(x) + ': ' + Town.townConnections[x]
        return out
