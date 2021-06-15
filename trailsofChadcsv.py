#!/usr/bin/env python3
  
# standard library
import csv
import os
import time

# reading from csv file and storing in variable comicfile 
# function to take input of user, read the csv file and display only elements from that input

def comicReader(name):
    comicInput = input("""
            
                       What kind of comics would you like to view in my collection? 
                       1. Spider-man
                       2. Batman
                       3. Superman
                       4. X-men
                       5. Dont want to view anything
                       """)
    # while loop to display ASCII and list comics by title 
    # loop will exit when user pick's option 5
    while comicInput != "5":
        if comicInput == "1":
            os.system("clear")
            with open("/home/student/mycode/spiderman.txt") as spidey:
                print(spidey.read())
            time.sleep(3)
            print("This is what I have for Spider-Man in my collection")
            with open("brett_comics.txt", "r") as comicfile:
                reader = csv.reader(comicfile, delimiter=';') 
                for row in reader:
                    if "Spider-Man" in row[0]:
                        print(row[0])
                        comicInput = "5"
        if comicInput == "2":
            os.system("clear")
            with open("/home/student/mycode/batmanimg.txt") as batman:
                print(batman.read())
            time.sleep(3)
            print("This is what I have for Batman in my collection")
            with open("brett_comics.txt", "r") as comicfile:
                reader = csv.reader(comicfile, delimiter=';')
                for row in reader:
                    if "Batman" in row[0]:
                        print(row[0])
                        comicInput = "5"
        if comicInput == "3":
            os.system("clear")
            with open("/home/student/mycode/superman.txt") as supes:
                print(supes.read())
                time.sleep(3)
                print("This is what I have for Superman in my collections")
                with open("brett_comics.txt", "r") as comicfile:
                    reader = csv.reader(comicfile, delimiter=";")
                    for row in reader:
                        if "Superman" in row[0]:
                            print(row[0])
                            comicInput = "5"
        if comicInput == "4":
            os.system("clear")
            with open("/home/student/mycode/xmenimg.txt") as mutants:
                print(mutants.read())
                time.sleep(3)
                print("This is what I have for X-men in my collection")
                with open("brett_comics.txt", "r") as comicfile:
                    reader = csv.reader(comicfile, delimiter=";")
                    for row in reader:
                        if "X-Men" in row[0]:
                            print(row[0])
                            comicInput = "5"
comicReader("jelani")
