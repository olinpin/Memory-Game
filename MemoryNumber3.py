import random
import time
import os
import sys

print("Welcome to my memory trainer, let's start. You will see a number, try to remember it.\nIf you will write the number correctly, you can go to next level.\nIf you won't, you will have to try again from start.")
time.sleep(1)
Restart = 'y'
level = 0
max_level = 8
showsec = 1
waitsec = 1
SkipTime = input("Do You want to skip waiting time for remembering numbers with Enter? Yes/No\n")

    
while Restart == 'y' or 'Y':
    RandomNumber = (random.randint(10**level, 10**(level+1)-1))
    print(RandomNumber)
    if SkipTime == ("Yes" or "yes"):
        input("Press Enter to continue and then wait for next command")
    elif  SkipTime == "No" or "no":
        time.sleep(showsec)
    os.system("clear")
    time.sleep(waitsec)
    InputNumber = int(input("Now write here the number you saw. \n"))
    if InputNumber == RandomNumber and level < max_level:
        print("Good job, your answer is correct, let's try something harder.\n")
        level = level + 1
        showsec = showsec + 0.5
        waitsec = waitsec + 0.
        time.sleep(1)
        continue
    elif level == max_level:
        print("Good job, that's it for today, we don't have more levels for you right now.")
        break
    else:
        print("Sorry, that is not right, you can try it again from the beginnng.")
        level = 0
        showsec = 1
        waitsec = 1