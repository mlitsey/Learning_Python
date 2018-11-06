#!/usr/bin/python3

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-')) # prints centered title between "-" characters
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth)) # prints 2 columns key left justified followed by "." and value right justified
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 12, 5) # prints list formated with left column 12 and right column 5 charactes long
printPicnic(picnicItems, 20, 6) # prints list formated with left column 20 and right column 6 charactes long
