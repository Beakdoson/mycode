#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add d, n, and s
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

proto2 = [22, 80, 443, 53] # list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

protoa.append(proto2) # pass proto2 as an argument to the append method

print(protoa)

proto3 = [22,80,53,443,3389, 3389]

proto3.count(3389)

