#loot is represented as a list of strings like this: dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#Write function addToInventory(inventory, addedItems) where
#the "inventory" is a dictionary representing the player’s inventory
#and "addedItems" is a list like dragonLoot.
#The function should return a dictionary that represents the updated inventory.
#Note that the addedItems list can contain multiples of the same item.


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v,k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)+1
        inventory[item]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
