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

# 6 rounds and as long as answer is not null
while round <= 6:
    round += 1
    archtype_answer = input('What is your preferred Tekken 7 play style? Rushdown, Grappler, Mixup, Poking, or Counter hitter? ')
    if archtype_answer == "Rushdown":
        print("You should try out the following characters, Lars, Lee, Miguel, Kazumi")
        break
    elif archtype_answer == "Grappler":
        print("You should try out the following characters, King, Armor King, Craig Marduk")
        break
    elif archtype_answer == "Mixup":
        print("You should try out the following characters, Kazuya, Jin, Heihaichi")
        break
    elif archtype_answer == "Poking":
        print("You should try out the following characters, Nina, Feng, Anna")
        break
    elif archtype_answer == "Counter hitter":
        print("You should try out the following characters, Steve, Dragunov, Leroy")
        break
    else:
        print('Ill give you some time to think of of your play style!')
