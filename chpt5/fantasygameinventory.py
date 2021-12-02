#You are creating a fantasy video game.
#The data structure for the inventory will be a dictionary
#the keys are strings describing the item
#the valuea are integers detailing how many of that item the player has.
#ex: dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#means the player has 1 rope, 6 torches, 42 gold coins

#Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
#Hint: You can use a for loop to loop through all the keys in a dictionary.

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v,k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
