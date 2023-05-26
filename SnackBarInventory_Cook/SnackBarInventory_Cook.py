'''
SnackBarInventory
Samantha Cook
4/25/2023
Python II
'''

import os


def main_menu():
    '''
    Main menu for the application.
    '''
    while True:
        
        print('1 - Add items')
        print('2 - Change item quantity')
        print('3 - View inventory')
        print('4 - Exit')
        option = input('Please enter your selection (1-4) >> ')
        if option == '1':
            add_items()
        elif option == '2':
            change_quantity('inventory.txt')
        elif option == '3':
            view_inventory()
        elif option == '4':
            break
        else:
            print('Invaild option selected!')
        print()
        
def add_items():
    repeat = 'y'
    while repeat == 'y':
        item_name = input('Enter the name of the item >> ')
        price = float(input('Enter the price of the item >> '))
        quantity = int(input('Enter the ammount of the items in stock >>'))
        file = open('inventory.txt', 'a')
        file.write(item_name + ',' + str(price) + ',' + str(quantity) + '\n')
        file.close()
        repeat = input('Would you like to repeat again? >> ')
        print()

def change_quantity(file_name):
    file = open(file_name, 'r')
    inventory = file.readlines()
    file.close()
    
    item_name = input('Enter the name of the item >> ')
    for item in inventory:
        fields = item.split(',')
        if fields[0] == item_name:
            quantity = int(input('How many items are there now? >> '))
            inventory.remove(item)
            if quantity >= 0:
                inventory.append(fields[0] + ',' + fields[1] + ',' + str(quantity) + '\n')
            break
    else:
        print('That item is not in the inventory.')
    file = open(file_name, 'w')
    file.writelines(inventory)
    file.close()
    
    
def view_inventory():
    file_name = 'inventory.txt'
    file = open(file_name, 'r')
    inventory = file.readlines()
    file.close()
    for i in range(0, len(inventory)):
        fields = inventory[i].split(',')
        print(i + 1, '-', fields[2].strip(), fields[0].strip(), 'at ' + '$' + fields[1])

#main
main_menu()