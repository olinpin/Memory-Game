import random
import time
import os
import sys
import timeit
import json

with open("stats.json") as statistics_file:
    statistics = json.load(statistics_file)['game_review']
    for p in statistics:
        print(p['name'], "|", p['time'], "|", p['level'], "\n")

print("Welcome to my memory trainer, let's start. You will see a number, try to remember it.\nIf you will write the number correctly, you can go to next level.\nIf you won't, you will have to try again from start.")
time.sleep(1)
level = 0
max_level = 0
show_sec = 1
wait_sec = 1
stopwatch = 0
end_stopwatch = 0
skip_time = input("Do You want to skip waiting time for remembering numbers with Enter? Yes/No\n")
your_name = input("What's your name? Please use the same name that you've used before if you're using the program again.\n")
while True:
    random_number = (random.randint(10**level, 10**(level+1)-1))
    print(random_number)
    stopwatch += time.time()
    if skip_time == ("Yes" or "yes"):
        input("Press Enter to continue and then wait for next command")
    elif  skip_time == "No" or "no":
        time.sleep(show_sec)
    end_stopwatch += time.time()
    os.system("clear")
    time.sleep(wait_sec)
    input_number = int(input("Now write here the number you saw. \n"))
    time_result = end_stopwatch-stopwatch
    if input_number == random_number and level < max_level:
        print("Good job, your answer is correct, let's try something harder.\n")
        level = level + 1
        show_sec = show_sec + 0.5
        wait_sec = wait_sec + 0.3
        time.sleep(1)
        continue
    elif level == max_level:
        print("Good job, that's it for today, we don't have more levels for you right now.\nIt took you", time_result, "seconds to beat the game")
        with open("stats.json", "r") as stat_read:
            reading = json.loads(stat_read.read())

            reading["game_review"].append({
                "name" : your_name,
                "time" : round(time_result, 2),
                "level" : level+1
            })

        with open("stats.json", "w") as stats:
            json.dump(reading, stats)
                
        break
    else:
        print("Sorry, that is not right, you can try it again from the beginnng.")
        level = 0
        show_sec = 1
        wait_sec = 1