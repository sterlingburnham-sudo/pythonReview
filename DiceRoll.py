import random

def diceroll():
    diceValue = random.randint(1,6)
    return diceValue

def startGame():
    print("Welcome to Dice Game! Its your roll against their roll")
    print("This program is now live on gitHub!")
    ourRoll = diceroll()
    theirRoll = diceroll()

    print("You rolled a " + str(ourRoll))
    print("You rolled a " + str(theirRoll))

    if ourRoll == theirRoll:
        print("tie")

    elif ourRoll > theirRoll:
        print("You win!")
    else:
        print("You lose!")



startGame()

