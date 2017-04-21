import Classes

# Creates a dictionary of character stats with a starting value of zero
charStats = {
    "Armor": 0,
    "Damage": 0,
    "Health": 10
}

itemDesc = {
    "Wooden Sword": "A Shabby wooden Sword. Doesn't do much.",
    "Wooden Chestplate": "A sturdy wooden chestplate protects you from minor hits."
}

townDesc = {
    "Wallowdale": "Wallowdale",
    "Hampstead": "Hampstead",
    "Stawford": "Stawford",
    "Millstone": "Millstone",
    "Silverkeep": "Silverkeep"
}


# Adds items to player's inventory
inventory = Classes.Inventory()
inventory.add_Item(Classes.Item('Wooden Sword', 'Weapon', [5], False))
inventory.add_Item(Classes.Item('Wooden Chestplate', 'Armor', [5], False))

# Creates towns and connections


# for name in townNames:
# townDict[name] = Classes.Town()
# Sets the current town player is in.
currTown = "Stawford"
