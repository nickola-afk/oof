import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)#0.02
    print()

def updates():
    print_slow("1.0 release \n update 1.3 -- i added mickel + door")

def show_instructions():
    print_slow("\nWelcome to the Haunted House!")
    print_slow("Move commands: go North, go South, go East, go West")
    print_slow("Add to Inventory: get 'item name'\n")

def show_status():
    print_slow("\n---------------------------")
    print_slow(f"You are in the {current_room}.")
    print_slow(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print_slow(f"You see a {rooms[current_room]['item']}.")
    print_slow("---------------------------\n")

rooms = {
    'Hall': {'North': 'Door', 'South': 'Kitchen', 'East': 'Dining Room', 'West': 'Room Hall', 'item': None},
    'Door': {'South': 'Hall', 'item': 'door'},
    'Kitchen': {'North': 'Hall', 'item': 'monster'},
    'Room Hall': {'East': 'Hall', 'South': 'Bed Room', 'West': 'Mikeals Room', 'item': None},
    'Mikeals Room': {'East': 'Room Hall', 'item': 'mikeal'},
    'Bed Room': {'North': 'Room Hall', 'item': 'key'},
    'Dining Room': {'West': 'Hall', 'South': 'Garden', 'item': 'bb_blaster'},
    'Garden': {'North': 'Dining Room', 'item': 'treasure'},
}

inventory = []
current_room = 'Hall'
i = 0
health = 100

updates()
show_instructions()

while True:
    show_status()

    move = input("> ").title().split()

    if len(move) == 2:
        command, direction = move[0], move[1]

        if command == 'Go':
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                item = rooms[current_room].get('item')
                if item == 'monster':
                    if 'bb_blaster' in inventory:
                        print_slow("how could you kill him, he just wanted a hug... Ending 2/5")
                        break
                    else:
                        print_slow("The monster has caught you dummy. Ending 1/5")
                        break
                if item == 'mikeal':
                    if 'bb_blaster' in inventory:
                        print_slow("dude that was a inocent man that i coded to die as soon as you walked in with the bb, maybe he died of shock... the cops came btw. Ending 5/5")
                        break
                    else:
                        print_slow("\nmikeal: hey")
                        ishouse = input("\nAsk him if this is his house \n-Is This Your House?- \n-ill find a way to kill you- \n-dude your purple\n-wheres the key to the treasure-\n")
                        while i != 1:
                            i = 0
                            if ishouse == "wheres the key to the treasure":
                                print_slow("\nmikeal: dwag its mine")
                            if ishouse == "dude your purple":
                                print_slow("\nmikeal: im litterally the perple guy from the one game i kill you now \nSeceret Ending")
                                health = 0
                                break
                            if ishouse == "Is This Your House?":
                                print_slow("mikeal: yeah could you leave, monster doesnt like you here")
                                break
                            if ishouse == "ill find a way to kill you":
                                print_slow("i get that alot")
                                time.sleep(10)
                                print_slow("kys")
                                break
                            else:
                                print_slow("could you repeat that?")
                                ishouse = input("\nAsk him if this is his house \n-Is This Your House?- \n-ill find a way to kill you- \n-dude your purple-\n")
            else:
                print_slow("You can't go that way dumbo")
        
        elif command == 'Get':
            item = rooms[current_room].get('item')
            if item and item.lower() == direction.lower():
                if item == 'treasure':
                    if 'key' in inventory:
                        inventory.append(item)
                        print_slow(f"{item.capitalize()} added to your inventory!")
                    else:
                        print_slow("Sorry, you need a key to get the treasure!")
                elif item == 'door':
                    if 'key' in inventory:
                        inventory.append(item)
                        pprint_slow(f"{item.capitalize()} added to your inventory!")
                    else:
                        print_slow("Sorry but you need the key")
                else:
                    inventory.append(item)
                    print_slow(f"{item.capitalize()} added to your inventory!")
                rooms[current_room]['item'] = None
            else:
                print_slow(f"Can't find a {direction} here.")

    if 'treasure' in inventory:
        print_slow("You got teh treasure1!!1!!!1!!!11!!!1! you winz1@!!21!!!1 Ending 3/5")
        break
    if 'door' in inventory:
        print_slow("You ran away, coward, same thing i would have done to lol. Ending 4/5")
        break
    if health == 0:
        print_slow("You ded from low heath")
        break
# Wait for the user to close the game manually
input("\nEnter to Quit the game dummy")
