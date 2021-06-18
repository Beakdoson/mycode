#!/usr/bin/env python3

import random
import time


def tour_intro():
    print("Welcome! I will give you a simple tour of my house and all it's wonders!\n")
    print("I live in a average family home in a quiet neiborhood\n")
    print("However lately...there has been wierd noises comming from my backyard\n")
    print("So becareful and stay on the tour path!\n")
    print("Where would you like to tour first? Inside the house? Or take a look outside? What is the worse that can happen?")

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Where do you want to look? (1st or 2nd choice): ")

    return path

def checkPath(tour_choice):
    print("You head down to the hallway to the living area")
    time.sleep(2)
    print("You see a flat screen TV, and a sectional sofa")
    time.sleep(2)
    print("You notice the artwork on the walls are really stylish and brings out the feng sui of the room")
    time.sleep(2)
    print("The owner clearly has great taste...")

    tour_space = random.randint(1, 2)

    if tour_choice == str(tour_space):
        print("You look around and wonder how touring a friends home can make you feel so at home youself!")
        time.sleep(2)
        print("With your energy balanced from the decorum, you feel it is going to be a great day!")
    else:
        print("taking in the style and placement of all the furniture and art work.. your mind cant help but wonder, what did the owner mean?")
        time.sleep(2)
        print("Stay on the tour they said? pfft this is just a quiet area after all")
        time.sleep(2)
        print("You take a step toward the back of the house where the door leads to a big sprawling backyard full of flowers")
        time.sleep(2)
        print("You see a small path leading to a well beyond the owners land and wonder...")
        time.sleep(2)
        path_choicetwo = input("Should I take this path to and look into the well? Yes or no\n")
        if path_choicetwo == "Yes" or path_choicetwo == "y" or path_choicetwo == "Y":
            print("You walk down the narrow path to a huge well")
            time.sleep(2)
            print("You can quickly tell that very few people visit this area, if at all")
            time.sleep(2)
            print("With a sudden chill in the air, you can feel that something large has stalked it's way to you silently")
            time.sleep(2)
            print("All you can see from the creature is a massive blanket of thick yellow fur and souless eyes... you wonder to yourself as it closes its jaws over your head")
            time.sleep(4)
            print("Why didnt I just stay on the tour....")
        else:
            print("Well my friend said stay on the tour for a reason, let me just continue looking at the home and go home myself!")
            time.sleep(2)
            print("Maybe he will tell me later on why he gave such a warning...")

play_again = "yes"
while play_again == "yes" or play_again == "y" or play_again == "Y":
    tour_intro()
    user_choice = choosePath()
    checkPath(user_choice)
    play_again = input("Do you want to play again and take the tour? Yes or no..")
