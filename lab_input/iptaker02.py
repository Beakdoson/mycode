#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)


## object to store user input

user_answer = input("What is the name of your laptop?")

print("So the vendor of your laptop is " + user_answer)
