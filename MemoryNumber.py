import random
import time
import os

print("Welcome to my memory trainer, let's start. You will see a number, try to remember it.\nIf you will write the number correctly, you can go to next level.\nIf you won't, you will have to try again from start.")
time.sleep(10)
AreYouReady = input("Are you ready to play? Press 'y' to continue.")
TryAgain = 'y'
level = 0
number = 1
while TryAgain == 'y' or 'Y':
    RandomNumber = (random.randint(10**level, 10**(level+1)-1))
    print (RandomNumber)
    time.sleep(number)
    os.system("clear")
    InputNumber = int(input("Now write here the number you saw. \n"))
    if InputNumber == RandomNumber and level < 8:
        print("Good job, your answer is correct, let's try something harder.")
        if level < 8:
            level = level + 1
            number = number + 0.5
            time.sleep(2)
            continue
    elif level == 8:
        print("Good job, that's it for today, we don't have more levels for you right now.")
        break
    else:
        print("Sorry, that is not right, you can try it again if you want.")
        TryAgain = input("If you want to try it again, type 'y', if you want to go to easier level, type 'n'\n")
        if TryAgain == 'y' or 'Y':
            print("Alright, let's try it again.")
            continue
        elif level > 0 and TryAgain == 'n' or 'N':
            level-1
            continue
        else:
            print("Neither of the conditions were matched, try it again with the same level.")
            continue