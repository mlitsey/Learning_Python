#!/usr/bin/python3

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    #count[character] = count[character] + 1
    count[character] += 1 # condensed version of above line

pprint.pprint(count)
#print(pprint.pformat(count)) #same as above, as a string value?
