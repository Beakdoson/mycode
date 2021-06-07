#!/usr/bin/env python3

# creates a list with three items
my_list = [ "192.168.0.5", 5060, "UP" ]
# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# displays the 2nd item in the list
print("This is the 2nd item in the list (port): "+ str( my_list[1]) )

# displays the last item in the list
print("The last item in the list (state):" + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("This is only the IP addresses: " + iplist[3], ", and", iplist[4] )
