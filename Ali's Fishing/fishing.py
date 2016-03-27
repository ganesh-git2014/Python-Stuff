import time, os
import random
clear = lambda: os.system('cls')
inventory = []
gold = 0
rawfish = ["Mackarel", "Cod", "Salmon", "Herring", "Tuna"]
trash = ["Old Shoe", "Thin Bone", "Rusted Empty Box", "Plank Fragment"]
special = ["Copper Ring"]

print"                   _   _"
print"    ______ __     (_) ( )"          
print"    |  __ || |     _  |/"
print"    | |_| || |    | |   ___"
print"    | __  || |    | |  / __|"   
print"    | | | || |___ | |  \__ \ "
print"    |_| |_||_____||_|  |___/"   
print"    ______  _     _     _"            
print"    |  ___|(_)   | |   (_)"            
print"    | |__   _ ___| |__  _ _ __   __ _" 
print"    |  __| | / __| '_ \| | '_ \ / _` |"
print"    | |    | \__ \ | | | | | | | (_| |"
print"    |_|    |_|___/_| |_|_|_| |_|\__, |"
print"                                 __/ |"
print"                                |___/ "
time.sleep(2)
print".       .                                     /|    /|     "
print" \     /                o                      |     |     "
print"  \   /   .-. .--..--.  .   .-. .--.       o   |     |     "
print"   \ /   (.-' |   `--.  |  (   )|  |           |     |     "
print"    '     `--''   `--'-' `- `-' '  `-      o   |  o  |     " 
time.sleep(2)
print "\nIn this current version the first item in your inventory is sold.\n"
print "There will be an update, selecting what item to sell."

def sell_function():
    global gold
    if inventory[0] in rawfish:
        sold = inventory.pop(0)
        gold = gold+5
        print "You have sold a", sold, "for 5 gold coins!"
    elif inventory[0] in trash:
        sold = inventory.pop(0)
        gold = gold+1
        print "You have recycled a", sold, "for 1 gold coin!"
    elif inventory[0] in special:
        sold = inventory.pop(0)
        gold = gold+1000
        print "You have sold a", sold, "for 10 gold coins!"
    else:
        print "Shopkeeper:'You can't sell that.'"

def fish_function():
    random_fishingchance = random.randrange(1,32)
    if 1 <= random_fishingchance < 3:
        inventory.append("Mackarel")
        print "You have reeled in a Mackarel!"
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 3 <= random_fishingchance < 5:
        inventory.append("Cod")
        print "You have reeled in a Cod!"
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 5 <= random_fishingchance < 7:
        inventory.append("Salmon")
        print "You have reeled in a Salmon!"
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 7 <= random_fishingchance < 9:
        inventory.append("Herring")
        print "You have reeled in a Herring!"
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 9 <= random_fishingchance < 11:
        inventory.append("Tuna")
        print "You have reeled in a Tuna!"
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 11 <= random_fishingchance < 16:
        inventory.append("Old Shoe")
        print "You have reeled in an Old Shoe..."
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 16 <= random_fishingchance < 21:
        inventory.append("Thin Bone")
        print "You have reeled in a Thin Bone..."
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 21 <= random_fishingchance < 26:
        inventory.append("Rusted Empty Box")
        print "You have reeled in a Rusted Empty Box..."
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 26 <= random_fishingchance < 31:
        inventory.append("Plank Fragment")
        print "You have reeled in a Plank Fragment..."
        time.sleep(0.5)
        print "You place it into your inventory"
    elif 31 <= random_fishingchance < 32:
        inventory.append("Copper Ring")
        print "You have reeled in a ring shaped object covered in mud."
        print "After cleaning it you notice it is a Copper Ring!"
        time.sleep(0.5)
        print "You place it into your inventory"
    else:
        print "It seems your fishing line has snapped!"

#This is the definition which loops asking for inputs within the game.
def action_function():
    global clear
    while True: #This while loop, loops the action menu untill the user decides to QUIT.
        action = raw_input("Do you want to 'sell'  'fish'  'inventory' 'money' or 'quit'? ") #This is where the user inputs his action choice which is then handeld by the code below.
        if action == "quit": #If the user inputs 'quit' this if statement breaks the loop and ends the game.
            clear()
            print"    _______ _                 _           __           "
            print"   |__   __| |               | |         / _|          "
            print"      | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __  " 
            print"      | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| "
            print"      | |  | | | | (_| | | | |   <\__ \ | || (_) | |    "
            print"      |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    "
            print"          _             _             "
            print"         | |           (_)            "
            print"    _ __ | | __ _ _   _ _ _ __   __ _ "
            print"   | '_ \| |/ _` | | | | | '_ \ / _` |"
            print"   | |_) | | (_| | |_| | | | | | (_| |"
            print"   | .__/|_|\__,_|\__, |_|_| |_|\__, |"
            print"   | |             __/ |         __/ |"
            print"   |_|            |___/         |___/ "                                                       
            time.sleep(1)
            print"             _ _ _       ______ _     _     _             "
            print"       /\   | (_| )     |  ____(_)   | |   (_)            "
            print"      /  \  | |_|/ ___  | |__   _ ___| |__  _ _ __   __ _ "
            print"     / /\ \ | | | / __| |  __| | / __| '_ \| | '_ \ / _` |"
            print"    / ____ \| | | \__ \ | |    | \__ \ | | | | | | | (_| |"
            print"   /_/    \_\_|_| |___/ |_|    |_|___/_| |_|_|_| |_|\__, |"
            print"                                                     __/ |"
            print"                                                    |___/ "
            print"              __                      "
            print"             /o \/        __         "
            print"    <><      \__/\ __    /o \/        "   
            print"     <><          /o \/  \__/\         "    
            print"       <><     __ \__/\_                "
            print"      <><      /o \/  /o \/              "                     
            print"     <><       \__/\  \__/\               "                           
            print"     <><        __     __                  "  
            print"     <>< <><   /o \/  /o \/     __          "     
            print"     <><  <><  \__/\  \__/\    /o \/         "     
            print"       <><                     \__/\     "
            print"     <><                __              "
            print"                       /o \/             "                    
            print"                __     \__/\    "
            print"               /o \/           "
            print"               \__/\          "  
            time.sleep(5)
            break            
            end              
        if action == "sell": #If the user inputs 'sell' this if statement will bring up the 'sell_function()' definition.
            clear()
            sell_function()
        if action == "fish": #if the user inputs 'fish' this if statement will print 'text' then wait 5 seconds using the 'time.sleep()' function then bring up the 'fish_function()' function.
            clear()
            print "\nYou throw your reel...\n"
            time.sleep(5)
            fish_function()
        if action == "inventory":  
            clear()
            print "\nYou begin to open your inventory\n"
            time.sleep(0.5)
            print inventory
        if action == "money":
            clear() 
            print gold
        if action == "gold":
            clear()
            print gold
action_function()
