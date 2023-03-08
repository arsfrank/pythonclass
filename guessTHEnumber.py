# Game to guess the random number
import random
num = random.randint(1,9)
computer = int(input("Enter a number between 1 and 9: "))
guess = False
counter=0
while not guess:
    usernum = int(input("Enter a number between 1 and 9: "))
    if usernum == computer:
        guess = True
    elif usernum < computer:
        print("too low")
    else:
        print(" too high!")
    if guess:
        print(" You guessed it right!")
    else:
        print("You lost! Mwahahahahaha")

    if counter > 2:
            print("Too many guesses!")
            break
    if guess:
        print(" You guesses it right!")
    else:
        print("you lost!")
        break
