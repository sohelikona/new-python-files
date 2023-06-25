name = input("Type Your name:  ")

print("Welcome", name, " to this adventure!👋")

answer = input("You're on a dirt road, it has come to an end and you can go left or right. So, which way would you like to go?🤔:  ").lower()





if answer == "left":
    answer = input("You come to a river, you can walk aoround it or swim in the river, Type walk to walk around and swim to swim accross: ")


    if answer == "swim":
         print("You swam across and were eaten by an crocodile.")
    elif answer == "walk":
         print("You walked for many miles, ran out of water and you lost the game.")
    else: print("Not a valid option. You lose.")







if answer == "right":
    answer = input("You've come to a Jungle. This Jungle is full of wild beasts. Do you want to enter in this jungle. Type yes to go into the jungle. Type no to quit:   ")


    if answer == "yes":
         answer = input("You've entered into the jungle and now you're sourrend by some hyena. You have to options, either you can run to save your life or you can fight back. To fight type fight, to run type run:   ")


    elif answer == "no":
         print("You quit the game and you LOSE!")



    if answer == "fight":
         answer = input("Yay! You won against the hyena. What do you want to do?  Do you want to hunt to feed yourself or just wanna walk to reach to the peaple. Type hunt to hunt and type walk to walk:  ")
    elif answer == "run":
         print("Opps, You're torn apart by hyena. You lose")


    else: print("Not a valid option. You lose.")

    if answer == "hunt":
         answer = input("You've successfully hunted a deer. So, now that you're full, which way do you wanna go? Type left to go to left and type right to go to right:  ")

    elif answer == "walk":
         print("Sorry, You walked for miles and ran out of water and you lost the game")

    else: print("Not a valid option. You lose.")

    if answer == "right":
         print("You lost your way and eaten by a Lion")

    elif answer == "left":
         answer = print("Wohoooooo, congratulations. You found a village full of people. You won the game.")

    else: print("Not a valid option. You lose.")
         




    # elif answer == "no":
    #      print("You lose!")
    # else: print("Not a valid option. You lose.")




else:print("Not a valid option. You lose.") 









