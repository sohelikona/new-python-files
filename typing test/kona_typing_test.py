from time import *
import random as r
from text import text

print(time())

def mistake(paragraphText, userText):
    error = 0
    for i in range(len(paragraphText)):
        try:
            if paragraphText[i] != userText[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(time_speed, time_enter, userinput):
    time_delay = time_enter - time_speed
    time_round = round(time_delay, 2)
    speed = len(userinput) / time_round
    return round(speed)
    

while True:
    check = input("Press s to start the test and q to quit! :  ")
    if check == 's' or check == 'S':
        text1 = r.choice(text)
        print("Welcome to my typing test program!👋")
        print(text1)
        print()
        print()

        time_1 = time()
        userInput = input(" Input:   ")
        time_2 = time()

        print('Speed: ', speed_time(time_1, time_2, userInput), "w/sec")
        print("Error: ", mistake(text1, userInput))
    elif check == 'q' or check =="Q":
        print("program ended successfully")
        quit()
    else:
        print("Unknown input,😒 you can only press s or q.")