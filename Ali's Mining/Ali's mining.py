__author__ = 'AliHamdan'

#Aliscape mining game beta
#V0.2 ALPHA
import random, time
money = 10000
inventory = ["bronze pickaxe"]



#-------------Levels-------------

Mining = 0
MningXP = 0

Strength = 0
StrengthXP = 0

Vision = 0
VisionXP = 0



#--------------------------------



Pickaxes = {
 'adamant pickaxe': {'name': 'adamant pickaxe', 'cost': 150, 'sell': 100, 'level': 5},
 'bronze pickaxe': {'name': 'bronze pickaxe', 'cost': 10, 'sell': 1, 'level': 5},
 'dragon pickaxe': {'name': 'dragon pickaxe', 'cost': 666, 'sell': 333, 'level': 5},
 'inferno adze': {'name': 'inferno adze', 'cost': 1000, 'sell': 500, 'level': 5},
 'iron pickaxe': {'name': 'iron pickaxe', 'cost': 50, 'sell': 25, 'level': 5},
 'mithril pickaxe': {'name': 'mithril pickaxe', 'cost': 100, 'sell': 50, 'level': 5},
 'rune pickaxe': {'name': 'rune pickaxe', 'cost': 200, 'sell': 100, 'level': 5},
 'steel pickaxe': {'name': 'steel pickaxe', 'cost': 75, 'sell': 325, 'level': 5}}

Ores = {
 'clay':{'name':'Clay ore', 'cost': 100, 'sell': 5, 'level': 5},
 'copper':{'name':'Copper ore', 'cost': 100, 'sell': 5, 'level': 5},
 'tin':{'name':'Tin ore', 'cost': 100, 'sell': 5, 'level': 5},
 'iron':{'name':'Iron ore', 'cost': 100, 'sell': 5, 'level': 5},
 'silver':{'name':'Silver ore', 'cost': 100, 'sell': 5, 'level': 5},
 'coal':{'name':'Coal ore', 'cost': 100, 'sell': 5, 'level': 5},
 'gold':{'name':'Gold ore', 'cost': 100, 'sell': 5, 'level': 5},
 'mithril':{'name':'Mithril ore', 'cost': 100, 'sell': 5, 'level': 5},
 'adamantite':{'name':'Adamantite ore', 'cost': 100, 'sell': 5, 'level': 5},
 'runite':{'name':'Runite ore', 'cost': 100, 'sell': 5, 'level': 5},
 'diamond':{'name':'Diamond ', 'cost': 100, 'sell': 5, 'level': 5},
 'ruby':{'name':'Ruby', 'cost': 100, 'sell': 5, 'level': 5},
 'emerald':{'name':'Emerald', 'cost': 100, 'sell': 5, 'level': 5},
 'sapphire':{'name':'Sapphire', 'cost': 100, 'sell': 5, 'level': 5}}



def start():
    print "Hello and welcome to Aliscapes mining"
    time.sleep(2)
    print "\n*You are handed a Bronze Pickaxe* This is your first axe, use it wisely.\n"
    time.sleep(2)
    print "\nTo check your inventory type *inv*.\n"
    print "\nTo check your levels enter *lev*\n"
    print "\nTo mine enter *mine*.\n"
    print "\nTo shop for Pickaxes enter *Shop*.\n"
    print "\nTo shop for Ores enter *Shop2*.\n"
    home()


def levels():
    print "Your Mining level:", Mining
    print "Your Mining Exp:",MningXP

    print "Your Strength level:",Strength
    print "Your Strength Exp:",StrengthXP

    print "Your Vision level:",Vision
    print "Your Vision Exp:",VisionXP
    time.sleep(2)
    raw_input("\nHit Enter to return to the menu\n")
    home()



def shop2():
    global money
    global cost
    print "Welcome to Alister's Ores!"
    time.sleep(2)
    sellbuy = raw_input("\nWould you like to sell or buy Ores?:\n")
    if sellbuy == "sell":
        sell()
    elif sellbuy.lower() == "buy":
        print "\nYou have\n", money, "\nCoins\n"
        print "\nHere is a list of our goods....\n"
        for i in Ores.values():
            print '{name} - costs: {cost}'.format(**i)

    while True:
        what_item = raw_input("\nWhich item would you like to purchase? (Leave blank to quit)\n")
        if not what_item:
            print "\nYou are now returning to Home\n"
            home()
        if what_item in Ores:
            if money >= Ores[what_item]["cost"]:
                inventory.append(what_item)
                money = money - Ores[what_item]["cost"]
                print "You have successfully purchased a", what_item
                time.sleep(1)
                print "\nYou now have\n", money, "Coins"
                time.sleep(1)
                print "\nReturning Home\n"
                home()
            else:
                print "Insufficiant funds to complete the purchase"
                print "\nReturning Home\n"
                home()
        else:
            print "No such item"
            print "\nReturning Home\n"
            home()


def shop():
    global money
    global cost
    print "Welcome to Alister's goods!"
    time.sleep(2)
    sellbuy = raw_input("\nWould you like to sell or buy Goods or Exit?:\n")
    if sellbuy.lower() == "sell":
        sell()
    elif sellbuy.lower() == "buy":
        print "\nYou have\n", money, "\nCoins\n"
        print "\nHere is a list of our goods....\n"
        for axe in Pickaxes.values():
            print '{name} - costs: {cost}'.format(**axe)
    elif sellbuy.lower() == "exit":
        print "returning home..."
        time.sleep(1)
        home()
    else:
        print "\nPlease enter a valid command!\n"
        shop()

    while True:
        what_item = raw_input("\nWhich item would you like to purchase? (Leave blank to quit)\n")
        if not what_item:
            print "\nYou are now returning to Home\n"
            home()
        if what_item in Pickaxes:
            if money >= Pickaxes[what_item]["cost"]:
                inventory.append(what_item)
                money = money - Pickaxes[what_item]["cost"]
                print "You have successfully purchased a", what_item
                time.sleep(1)
                print "You now have", money, "Coins"
                time.sleep(1)
                print "\nReturning Home\n"
                home()
            else:
                print "Insufficiant funds to complete the purchase"
                print "\nReturning Home\n"
                home()
        else:
            print "No such item"
            print "\nReturning Home\n"
            home()






def home():
    Action = raw_input("\nWhat would you like to do?: \n")
    if Action == "inv":
        showinv()
    elif Action == "shop":
        shop()
    elif Action == "mine":
        mining()
    elif Action == "lev":
        levels()
    elif Action == "shop2":
        shop2()
    else:
        print "Invalid command"
        home()



def sell():
    global sell
    global money
    print "Your inventory", inventory
    selling = raw_input("\nWhich item in your inventory would you like to sell?: \n")
    if selling in inventory:
        if selling in Pickaxes:
            confirm = raw_input ("Are you sure you wish to sell the item {} "
                 "for {} Coins? (y/n)\n>>".format(
                     selling,Pickaxes[selling]["sell"]))
            if confirm.lower() in ["yes","y"]:
                i = inventory.index(selling)
                del inventory[i]
                money = money + Pickaxes[selling]["sell"]
                print "You now have", money, "Coins"
                time.sleep(2)
                raw_input("\nHit Enter to return to the menu\n")
                home()
        if selling in Ores:
            confirm = raw_input ("Are you sure you wish to sell the item {} "
                 "for {} Coins? (y/n)\n>>".format(
                     selling,Ores[selling]["sell"]))
            if confirm.lower() in ["yes","y"]:
                i = inventory.index(selling)
                del inventory[i]
                money = money + Ores[selling]["sell"]
                print "You now have", money, "Coins"
                time.sleep(2)
                raw_input("\nHit Enter to return to the menu\n")
                home()

        else:
            print "\nItem not sold\n"
            time.sleep(2)
            raw_input("\nHit Enter to return to the menu\n")
            home()
    else:
        print "Item not in inventory... returning home."
        time.sleep(2)
        home()









def mining():
    for i in Ores:
        if Ores['level'] > Mining:
            continue
            print i
            raw_input("Which ore would you like to mine?: ")




def showinv():
    print money, "Gold"
    for i in inventory:
        print i
    time.sleep(2)
    raw_input("\nHit Enter to return to the menu\n")
    home()











start()












