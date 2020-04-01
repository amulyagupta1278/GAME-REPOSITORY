import time
name = input("  Enter your name in (Mr/Mrs ): ")

print("*************************************************************************************************************************************************************")
print()
print("                                                         HELLO ", name ," ")
print()
print("***********************************************    A WARM WELCOME IN THE GAME  ******************************************************************************")
print()
print("                                                          OF WORD GUESSING   ")
print()
print("*************************************************************************************************************************************************************")
print("")
time.sleep(1)
time.sleep(0.5)



def sportsguess():
    print("  Guess a name of sport having 7 letters")
    print("  Start guessing......")
    word = "cricket"
    guesses = " "
    turns = 5
    while turns > 0 :
        failed = 0
        for char in word :
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1


        if failed == 0:
            print(" ************** HURRY  YOU WON THE GAME *************** ")
            break
        print
        guess = input("   guess a character: ")
        guesses += guess


        if guess not in word:
            turns -= 1
            print("   Wrong")
            print()
            print(" ------------------ you have ", + turns ," more guesses ------------------------- ")
            print()
            if(turns == 0):
                print("****** BAD LUCK TRY ONCE AGAIN *****")
                print()
                
def movieguess():
    print("  Guess a movie cointaining 8 letters ")
    print("  Start guessing......")
    word ="bahubali"
    guesses = " "
    turns = 5
    while turns > 0 :
        failed = 0
        for char in word :
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1


        if failed == 0:
            print(" ***** HURRY  YOU WON THE GAME ******** ")
            break
        print
        guess = input("   guess a character: ")
        print()
        guesses += guess


        if guess not in word:
            turns -= 1
            print("   Wrong")
            print()
            print(" ------------ you have ", + turns ," more guesses ---------------------")
            print()

            if(turns == 0):
                print("****** BAD LUCK TRY ONCE AGAIN *****")
                print()
                
def holybookguess():
    print("  Guess a word cointaining five letters ")
    print("  Start guessing......")
    word = "bible"
    guesses = " "
    turns = 5
    while turns > 0 :
        failed = 0
        for char in word :
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1


        if failed == 0:
            print(" ***** HURRY  YOU WON THE GAME ******** ")
            break
        print
        guess = input("   guess a character: ")
        print()
        guesses += guess


        if guess not in word:
            turns -= 1
            print("  Wrong")
            print()
            print(" ---------------you have", + turns ," more guesses----------------------- ")
            print()
            if(turns == 0):
                print("****** BAD LUCK TRY ONCE AGAIN *****")
                print()
                
def singerguess():
    print("  Guess a singer name cointaining 12 letters ")
    print("  Start guessing......")
    word = "kishorekumar"
    guesses = " "
    turns = 10
    while turns > 0 :
        failed = 0
        for char in word :
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1


        if failed == 0:
            print(" ***** HURRY  YOU WON THE GAME ******** ")
            break
        print
        guess = input("   guess a character: ")
        print()
        guesses += guess


        if guess not in word:
            turns -= 1
            print("   Wrong")
            print()
            print(" ----------- you have ", + turns ," more guesses ------------------------  ")
            print()
            if(turns == 0):
                print("****** BAD LUCK TRY ONCE AGAIN *****")
                print()
                
def actorguess():
    print("  Guess an actor name having 8 words starting with j ")
    print("  Start guessing......")
    print("  BEST OF LUCK !")
    word = " jitendra "
    guesses = " "
    turns = 10
    while turns > 0 :
        failed = 0
        for char in word :
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1


        if failed == 0:
            print(" ***** HURRY  YOU WON THE GAME ******** ")
            break
        print
        guess = input("   guess a character: ")
        print()
        guesses += guess


        if guess not in word:
            turns -= 1
            print("   Wrong")
            print()
            print(" ------------------- you have ", + turns ," more guesses ------------------")
            proint()
            if(turns == 0):
                print("****** BAD LUCK TRY ONCE AGAIN *****")
                print()


def menudata():
    print()
    print()
    print(" *****<  CHOICE 1 : for  sports name guess   >***** ")
    print(" *****<  CHOICE 2 : for movie name guess     >***** ")
    print(" *****<  CHOICE 3 : for holybook  name guess >***** ")
    print(" *****<  CHOICE 4 : for singer name guess    >***** ")
    print(" *****<  CHOICE 5 : for actor name guess     >***** ")
    print()
    print()
    userinput = int(input("  PLEASE enter your choice : "))
    
    if(userinput == 1):
        sportsguess()
        runagain()
    elif(userinput == 2):
        movieguess()
        runagain()
    elif(userinput == 3):
        holybookguess()
        runagain()
    elif(userinput == 4):
        singerguess()
        runagain()
    elif(userinput == 5):
        actorguess()
        runagain()



def runagain():
    ch1 = input(" Do you want to continue playing(y/n) ???? : ")
    if(ch1=='y'):
        menudata()
    elif(ch1=="n"):
        print(" *********************YOU HAVE WELL TRIED ! ****************")
    else:
        print("  ")
        print("**********************************************************            *******************************************************************************")
        print("*****************************************************         THANK YOU      ************************************************************************")
        print("**********************************************************            *******************************************************************************")
        print("  ")

menudata()


