#!/usr/bin/env python3

# import module to add user experience
import time

# counter for while loop
round = 0

archtype_answer = " "

# greeting to user
print("Welcome to the King of Iron Fist Tournament!")
time.sleep(4)
print("There is many characters to choose from so the first question would be....")
time.sleep(2)

# rounds and as long as answer is not null
while True:

    round = round + 1

    # questions to be added to solutions
    print("Do you prefer to battle upclose or from a distance?")
    time.sleep(2)
    print("1. Upclose")
    print("2. From a distance")
    distance_question = int(input(""))
    time.sleep(3)
    if distance_question == 1:
        print("You like to get upclose? You might like Rushdown characters")
        time.sleep(1)
        print("You should try out the following characters, Lars, Lee, Miguel, Kazumi")
    elif distance_question == 2:
        print("You like to keep your opponent at a distance")
        time.sleep(1)
        print("You should try out the following characters, Steve, Dragunov, Leroy")
    else:
        print("Pick a valid choice please")
        continue

    print("Do you like to pressure opponents with attacks?")
    print("1. Yes")
    print("2. No")
    speed_question = int(input(""))
    time.sleep(3)
    if speed_question == 1:
        print("You like to blitz opponents")
        time.sleep(1)
        print("You should try out the following characters, Lars, Lee, Miguel, Kazumi")
    elif speed_question == 2:
        print("It sounds like you are more of a defensive play style")
        time.sleep(1)
        print("You should try out the following characters, Steve, Dragunov, Leroy")
    else:
        print("Pick a valid choice please")
        continue

    print("Do you add throws to mix up the flow of the match?")
    time.sleep(2)
    print("1. I love to add throws!")
    print("2. I hate grapplers! throw breaks are hard to perform1")
    throw_question = int(input(""))
    if throw_question == 1:
        print("You are a true grappler by heart!")
        time.sleep(2)
        print("You should try out the following characters, King, Armor King, Craig Marduk")
    elif throw_question == 2:
        print("It sounds like you need to practice your throw breaks!")
        time.sleep(2)
        print("Pick characters who dictact the flow of the match to counter grapplers")
        break
#print("1. Yes")
#print("2. No")
#throw_question = int(input(""))

