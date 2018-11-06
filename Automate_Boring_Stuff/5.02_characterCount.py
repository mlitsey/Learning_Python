#!/usr/bin/python3

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    #count[character] = count[character] + 1
    count[character] += 1 # shorter version of above line

print(count)
