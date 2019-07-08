def displayInventory(inv):
    print('Inventory:')
    total= 0
    for inv,amt in inv.items():
        print(amt,inv)
        total+=amt
    print('Total number of items:',total)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory
    
    
if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
