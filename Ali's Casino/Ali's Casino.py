import time, random, sys, traceback
gold1 = 10000
gold2 = 10000
bet1 = ""
bet2 = ""
player1 = ""
player2 = ""

#major bug found when playing the game, when saying no to place a bet after placing a higher bet than the computer it asks.


print "   __          __  _                            _        " 
print "   \ \        / / | |                          | |        "
print "    \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   "
print "     \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  "
print "      \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | "
print "       \/  \/_\___|_|\___\___/|_| |_| |_|\___|  \__\___/  "

print "             _ _ _        _____          _                "
print "       /\   | (_| )      / ____|        (_)               "
print "      /  \  | |_|/ ___  | |     __ _ ___ _ _ __   ___     "
print "     / /\ \ | | | / __| | |    / _` / __| | '_ \ / _ \    "
print "    / ____ \| | | \__ \ | |___| (_| \__ \ | | | | (_) |  " 
print "   /_/    \_\_|_| |___/  \_____\__,_|___/_|_| |_|\___/    "
print "                                                          "
print "                                                          "
time.sleep(2)
print".       .                                     /|    /|     "
print" \     /                o                      |     |     "
print"  \   /   .-. .--..--.  .   .-. .--.       o   |     |     "
print"   \ /   (.-' |   `--.  |  (   )|  |           |     |     "
print"    '     `--''   `--'-' `- `-' '  `-      o   |  o  |     " 
time.sleep(2)

def end():
    sys.exit()

def gameplay():
    time.sleep(0.5)
    choosing = raw_input("\nPlay against a friend or a computer? 'friend, computer' or 'quit'?\n")
    print "\nYou can type 'quit' anytime to return to the Menu\n"
    if choosing == "friend":
        friend()
    elif choosing == "computer":
        computer()
    elif choosing == "quit":
        end()
    else:
        gameplay()



def friend():
    global player1
    global player2

    player1 = raw_input("\nPlayer 1 please enter your name\n")

    player2 = raw_input("\nPlayer 2 please enter your name\n")

    print "Welcome %s and %s to Ali's Casino!" % (player1, player2)
    time.sleep(1)
    print "\nBoth players will start with 10,000 coins\n"
    time.sleep(1)
    print "\nTo win a game your dice roll must be larger than the opponents.\n"
    time.sleep(1)
    print "\nHave fun and enjoy responsibly.\n"


def starting():
    start = raw_input("\nStart game? 'yes, no or quit?'\n")
    if start == "yes":
        firstbet()
    elif start == "no":
        end()
    elif start == "quit":
        menu()
    else:
        print "Invalid Command"
        starting()



def firstbet(): 
    global gold1
    global bet1
    bet1 = int(raw_input(player1+ " please place your bet "))
    if bet1 > gold2:
        print ""
        print "You can not place a higher bid than the opponents avalible coins"
        print ""
        firstbet()
    if bet1 <= gold1:
        print("")
        print(player1+ " has placed" , bet1,"coins!")
        secondbet()
    elif bet1 > gold1:
        print("")
        print(player1+ "has an insufficient amount of coins")
        firstbet()



def secondbet():
    global gold2
    global bet2
    print("")
    bet2 = int (raw_input(player2+ " please place your bet "))
    if bet2 < bet1:
        print("\nPlease place the same or a larger amount than the first bet\n")
        secondbet()
    elif bet2 > bet1:
        proceed = raw_input("\nYou have placed a larger amount of coins than the computer, proceed?\n")
        if proceed == "yes":
            secondbet2()
        else:
            secondbet()
    elif bet2 <= gold2:
        print("")
        print(player2+ " has placed", bet2, "coins!")
        print("")
        total()
    elif bet2 > gold2:
        print("")
        print(player2+ " has an insufficient amount of coins")
        secondbet()


def secondbet2():
    if bet2 <= gold2:
        print("")
        print(player2+ " has placed", bet2, "coins!")
        print("")
        total()
    elif bet2 > gold2:
        print("")
        print(player2+ " has an insufficient amount of coins")
        secondbet()



def total():
    time.sleep(0.5)
    print "The pot is", (bet1 + bet2), "Coins Goodluck!"
    time.sleep(0.5)
    roll()


def roll():
    global gold1
    global gold2
    global bet1
    global bet2
    rollnum = random.randint(1,6)
    print "\nRolling %s's dice.....\n" % (player1)
    time.sleep(1)
    print""
    print "       ____"
    print "      /\' .\    _____"
    print "     /: \___\  / .  /\ "
    print "     \. / . / /____/..\ "
    print "      \/___/  \'  '\  / "
    print "               \'__'\/ "
    time.sleep(3)
    print player1 +"'s dice has landed on the number", rollnum,"!" 
    time.sleep(1)
    rollnum2 = random.randint(1,6)
    print "\nRolling %s's dice.....\n" % (player2)
    time.sleep(1)
    print ""
    print "       ____"
    print "      /\' .\    _____"
    print "     /: \___\  / .  /\ "
    print "     \' / . / /____/..\ "
    print "      \/___/  \'  '\  / "
    print "               \'__'\/ "
    time.sleep(3)
    print player2 +"'s dice has landed on the number", rollnum2,"!" 

    if rollnum > rollnum2:
        time.sleep(1)
        print "\n%s Wins!\n" % (player1)
        gold1 = gold1 + bet2
        gold2 = gold2 - bet2
        showgold()
    elif rollnum < rollnum2:
        time.sleep(1)
        print "\n%s Wins!\n" % (player2)
        gold2 = gold2 + bet1
        gold1 = gold1 - bet1
        showgold()
    elif rollnum == rollnum2:
        time.sleep(1)
        print "\nIts a draw!\n"
    if gold1 <= 0:
        print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player1)
        end()
    if gold2 <= 0:
        print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player2)
        end()
    '''else:
        print "\nInvalid roll\n"'''''

def showgold():
    print player1 + " now has", gold1,"Gold coins!"
    print "                                         "
    time.sleep(1)
    print player2 + " now has", gold2,"Gold coins!"



def end():
    sys.exit()



def computer():
    global gold3
    global compgold
    compgold = 10000
    randchoice = random.randint(1, 10)
    player1 = ""
    gold3 = 10000
    bet1 = 0


  
        
   
    def rollplay1():
        global player1
        global rollnum
        rollnum = random.randint(1, 6)
        print "\nRolling %s's dice.....\n" % (player1)
        time.sleep(1)
        print  ""
        print "       ____"
        print "      /\' .\    _____"
        print "     /: \___\  / .  /\ "
        print "     \' / . / /____/..\ "
        print "      \/___/  \'  '\  / "
        print "               \'__'\/ "
        time.sleep(3)
        print player1 +"'s dice has landed on the number", rollnum,"!" 
        rollalgo()
 


    def rollcomp():
        global rollnum2
        rollnum2 = random.randint(1, 6)
        print "\nRolling The Computers dice.....\n"
        time.sleep(1)
        print ""
        print "       ____ "
        print "      /\' .\    _____"
        print "     /: \___\  / .  /\ "
        print "     \' / . / /____/..\ "
        print "      \/___/  \'  '\  / "
        print "               \'__'\/ "
        time.sleep(3)
        print "The computers dice has landed on the number", rollnum2,"!"
        time.sleep(1)
        rollplay1()


    def rollalgo():
        global player1
        global rollnum
        global rollnum2
        global gold3
        global compgold
        global bet1
        global compbet
        if gold3 <= 0:
            print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player1)
            end()
        elif compbet <= 0:
            print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player2)
            end()

        if rollnum > rollnum2:
            time.sleep(1)
            print "\n%s Wins!\n" % (player1)
            gold3 = gold3 + compbet
            compgold = compgold - compbet
            showgold()
        elif rollnum < rollnum2:
            time.sleep(1)
            print "\nThe Computer Wins!\n" 
            compgold = compgold + bet1
            gold3 = gold3 - bet1
            showgold()
        elif rollnum == rollnum2:
            time.sleep(1)
            print "\nIts a draw!\n"
            startroll()
       
                  

    def showgold():
        global gold3
        global player1
        global compgold
        print player1 + " now has", gold3,"Gold coins!"
        print "                                      "
        time.sleep(1)
        print "The Computer now has", compgold,"Gold coins!"
        if gold3 <= 0:
            print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player1)
            end()
        elif compbet <= 0:
            print "\n%s is out of money! Thats what happens when you gamble, i hope this game teaches you a lesson. Have fun on the streets.\n" % (player2)
            end()
        startroll()


    def total():
        global bet1
        global compbet
        time.sleep(0.5)
        print ("")
        print "The pot is", (bet1 + compbet), "Coins Goodluck!"
        time.sleep(0.5)
        rollcomp()



    def player1bet2():
        global bet1
        global gold3
        global player1
        if bet1 <= gold3:
            print("")
            print(player1+ " has placed" , bet1,"coins!")
            total()
        elif bet1 > gold3:
            print("")
            print(player1+ " has an insufficient amount of coins")
            player1bet()




    def player1bet():
        global player1
        global bet1
        global gold3
        print("")
        bet1 = int(raw_input(player1+ " please place your bet "))
        if bet1 == compbet:
            player1bet2()
        elif bet1 < compbet:
            print "\nYou have placed a smaller amount of coins than your opponent, place again.\n"
            player1bet()
        elif bet1 > compbet:
            proceed = raw_input("\nYou have placed a larger amount of coins than the computer, proceed?\n")
            if proceed == "yes":
                player1bet2()
        else:
            player1bet()

        '''if type(bet1) != int:
            print "That is not a number!"
            player1bet()
        elif bet1 > compgold:
            print "You have placed a higher bet than the computer "
            player1bet()'''




    def computerbet():
        global gold3
        global compbet
        global compgold
        if compgold > gold3:
            compbet = random.randint(1, gold3)
        else:
            compbet = random.randint(1, compgold)
        print ("")
        print ("The computer has placed", compbet,"Coins!")
        player1bet()

            



    def startroll():
        start = raw_input("\nStart Roll? 'yes, no or quit'\n")
        if start == "yes":
            computerbet()
        elif start == "no":
            end()
        elif start == "quit":
            menu()
        else:
            print "invalid command"
            startroll()



    def choosename():
        global player1
        player1 = raw_input("Whats your name?")
        startroll()

    choosename()



gameplay()
while True:
   time.sleep(1)
   starting()

