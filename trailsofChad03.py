#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

## dictionary for char_name and char_stat to pull key values

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

print("Hero, " + char_name["wolverine"] + " and their powers, " + char_stat)

