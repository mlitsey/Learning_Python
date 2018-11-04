'''
Python 3 Tutorial: Print Function and Strings
Video https://youtu.be/UsCQXe1OHZk
'''
print('This is an example of the print function')
print("We're going to the store")
print('He said "Hi."')
print('We\'re going to the store')
print('Hi'+'there')
print('Hi '+'there')
print('Hi','there')
print('Hi',5)
print('Hi',+5)
print(5+'Hi')
print('Hi',+str(5))
print(int('8'),+5)
print(int('8.5'),+5)
print(float('8.5'),+5)
'''
Python 3 Programming Tutorial: Math
Video https://youtu.be/BvgPM9-krOY
'''
# is for single line commenting

''' 
is 
for
multi line 
commenting
'''
print('Hi')

# can use + - * / for math
1+3
print(1+3) #addition
print(3-1) #subtraction
print(4*4) #multiplication
print(5/2) #division
print(5/34) #division with float
print(4**4) #exponent (power of)
print(4+=1) #error, might have worked in 2.7
'''
Python 3 Programming Tutorial: Variables
https://youtu.be/vKqVnr0BEJQ
'''
exampleVar=55
print(exampleVar)
exampleVar=55+32
print(exampleVar)
exampleVar=print('whoa')
print(exampleVar)
x,y = (3,5)
print(x)
print(y)
x,y = (3,5,8) # Error
'''
Python 3 programming tutorial: While Loop
https://youtu.be/jSs58VZVLw8
'''
condition = 1
while condition < 10:
    print(condition)
    condition += 1 # same as condition = condition + 1

while True: # this is an infinite loop, use 'ctrl + c' to break it
    print('doing stuff')

'''
Python 3 Programming Tutorial - For loop
https://youtu.be/xtXexPSfcZg
'''
exampleList = [1,5,6,1,6,7,8,9,345,53,5]

for eachNumber in exampleList:
    print(eachNumber)
print('continue program')

for eachNumber in exampleList:
    print(eachNumber)
    print('continue program')

for x in range(1,11):
    print(x)

'''
Python 3 Programming Tutorial: If Statement
https://youtu.be/4u2ClNCtcgY
'''
x = 5
y = 8
z = 5
a = 3
if x > y:
    print('x is greater than y')
if x < y:
    print('x is less than y')
if z < y > x:
    print('y is greater than z and greater than x')
if z < y > x > a:
    print('y is greater than z and greater than x')
if z <= x:
    print('z is less than or equal to x')
if z == x:
    print('z is equal to x')
if z != x:
    print('z is not equal to x')
if z != y:
    print('z is not equal to y')

'''
Python 3 Programming Tutorial: If Else
https://youtu.be/qf0sfRZ0hHc
'''
x = 5
y = 8

if x > y:
    print('x is greater than y')
if x > 55:
    print('x is greater than 55')
else:
    print('x is not greater than y')

'''
Python 3 Programming Tutorial: If Elif Else
https://youtu.be/42MBMSOZgD4
'''
x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
#elif x == z:
elif x < z:
    print('x is less than z')
#elif 5 == 2:
elif 5 > 2:
    print('5 is greater than 2')
else:
    print('if and elif(s) never ran')

'''
Python 3 Programming Tutorial - Functions
https://youtu.be/owglNL1KQf0
'''
def example():
    print('basic function')
    z = 3 + 9
    print(z)

example()

'''
Python 3 Programming Tutorial - Function Parameters
https://youtu.be/CGRKqnoQGgM
'''
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is',num1)
    print(answer)

simple_addition(5,3)
simple_addition(num2=5,num1=3)

'''
Python 3 Programming Tutorial - Function Parameter Defaults
https://youtu.be/KeRxe9rll2Q
'''
def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print(num1,num2)
simple(2)

def basic_window(width,height,font='TNR',
                 bgc='w',scrollbar=True):
    print(width,height,font,bgc)
basic_window(500,350)
basic_window(500,350,bgc='red')

'''
Python 3 Programming Tutorial - Global and Local Variables
https://youtu.be/r9LtArXOYjk
'''
x = 6

def example():
    z = 5
    #print(z)
    print(x)
    print(x+5)
    x+=6 #error "UnboundLocalError"
example()

def example2():
    Global x
    print(x)
    x+=5
    print(x)
example2()

def example3(): # use this method when not allowed to use Globals
    globx = x
    print(globx)
    globx+=5
    print(globx)
    return globx
x = example3()
print(x)

'''
Python 3 Programming Tutorial - Installing modules
https://youtu.be/UKXx4e9PotI
'''
 
PIP install
pip install matplotlib

# Linux
"sudo apt-get install python-<module name>"
sudo apt-get install python-matplotlib

# Windows
www.pyqtgraph.org
download tar.gz file
unzip and untar the file
hold shift and right click the folder -- select "open command window here" or "open powershell window here"
setup.py install or ".\setup.py install"


'''
How to download and install Python Packages and Modules with Pip
https://youtu.be/jnpC_Ib_lbc
'''
pip install matplotlib
or
"C:\<path to python> \scripts\pip install matplotlib"
or
"C:\Users\Michael\AppData\Local\Programs\Python\Python36\python.exe"

{
download wheel file 
open foler for the wheel file
"C:\<path to python> \scripts\pip install <wheel file>"
}


'''
Python 3 Programming Tutorial - Common errors
https://youtu.be/AWIgW_F_k50
'''
variable = 55 # misspelled
print(varaible) # misspelled
NameError: name 'varaible' is not defined

def task():
#didn't put anyting in this function
def task2():
    print('xxx')
Expected an indented block

print('hello there') #remove closing ) to see error
print('f')
Invalid syntax

x = 'test line' #remove the trailing ' to see error
print(x)
EOL while scanning string literal

'''
Python 3 Programming Tutorial - Writing to File
https://youtu.be/f6zeuk5UjuE
'''
text = 'Sample Text to Save\nNew line!'
saveFile = open('exampleFile.txt','w') # w = write file / overwrite file, <filePath>/<fileName> = exampleFile.txt
saveFile.write(text)
saveFile.close()

'''
Python 3 Programming Tutorial - Appending Files
https://youtu.be/O3KAyaDvM-k
'''
appendMe = '\nNew bit of information'
appendFile = open('exampleFile.txt','a') # a = append to file, <filePath>/<fileName> = exampleFile.txt
appendFile.write('\n') # used to add a new line to file if not adding it in the text like appendMe
appendFile.write(appendMe)
appendFile.close()

'''
Python 3 Programming Tutorial - Read from a file
https://youtu.be/0SyyGIFnVCA
'''
readMe = open('exampleFile.txt','r').read() # r = read
print(readMe)

readMe = open('exampleFile.txt','r').readlines() # r = read, read line by line like a spreadsheet and saves into a python list
print(readMe)

'''
Python 3 Programming Tutorial - Classes
https://youtu.be/Beu5_JZEWsI
'''
class calculator:
    def addition(x,y):
        added = x + y
        print(added)
    def subtraction(x,y):
        sub = x - y
        print(sub)
    def multiplication(x,y):
        mult = x * y
        print(mult)
    def division(x,y):
        div = x / y
        print(div)

calculator.multiplication(3,5)
calculator.division(9,3)
calculator.subtraction(10,9)

'''
Python 3 Programming Tutorial - Frequently asked questions
https://youtu.be/hlxCpeb9pbU
'''
"shbang line used in linux to tell script where to run python from"
#! /usr/bin/python
#! /usr/bin/python3

"found in some modules if name == main"
def epic():
    print('wow this is great!')
if _name_ == '_main_':
    print('such great module!!!!')
"this causes the import to print something different than running it from the script"

'''
#24
Python 3 Programming Tutorial - Statistics (Mean, Standard Deviation)
https://youtu.be/D2U6yg0i-oA
'''
import statistics
example_list = [4,6,2,6,7,8,2,5,6,78,4,6,7,2,2]
x = statistics.mean(example_list)
print('Mean',x)
x = statistics.median(example_list)
print('Median',x)
x = statistics.stdev(example_list)
print('Standard Deviation',x)
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = statistics.stdev(example_list)
print('Standard Deviation',x)
x = statistics.variance(example_list)
print('Variance',x)

'''
#25
Python 3 Programming Tutorial - Module Import Syntax
https://youtu.be/MZlKCdybZrA
'''
import statistics as s 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = s.variance(example_list)
print('Variance',x)

from statistics import variance 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = variance(example_list)
print('Variance',x)

from statistics import variance as v 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = v(example_list)
print('Variance',x)

from statistics import variance, mean 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = variance(example_list)
y = mean(example_list)
print('Variance',x)
print('Mean',y)

from statistics import variance as v, mean as m 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = v(example_list)
y = m(example_list)
print('Variance',x)
print('Mean',y)

from statistics import * 
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x = variance(example_list)
y = mean(example_list)
print('Variance',x)
print('Mean',y)

'''
#26
Python 3 Programming Tutorial - Making Modules
https://youtu.be/sKYiQLRe254
'''
    
def ex(data):
    print(data)
    #save in same directory as original script
    # as examplemod.py

import examplemod
examplemod.ex('test')
    #save examplemod.py to python directory\Lib\site-packages\ (C:\Python\Python37\Lib\site-packages\)
    # ("C:\Users\Michael\AppData\Local\Programs\Python\Python36\Lib\site-packages\")
    #run above in idle


'''
#26
Python 3 Programming Tutorial - Making Modules
https://youtu.be/sKYiQLRe254
'''
             
def ex(data):

                print(data)

                #save in same directory as original script

                # as examplemod.py

 

import examplemod

examplemod.ex('test')

                #save examplemod.py to python directory\Lib\site-packages\ (C:\Python\Python37\Lib\site-packages)

                #run above in idle

 

'''
#27
Python 3 Programming Tutorial - Lists and Tuples
https://youtu.be/RVXIBZvg-W8
'''

 

Tuples are immuttable - unchangeable

                x = 5,6,2,6

                x = (5,6,2,6)

 

                def exampleFunc():

                                return 15,6

 

                x,y = exampleFunc()

 

Lists are muttable - changeable

                y = [5,6,2,6]

 

print(x[1])

print(y[2])

print(y[2],y[3])

 

'''
#28
Python 3 Programming Tutorial - List Manipulation
https://youtu.be/LUoKlnK5wcc
'''

 

x = [5,6,2,1,6,7,2,2,6,7,2]

print(x)

x.append(2)

print(x)

x.insert(2,99) # inserts 99 at index 2

print(x)

x.remove(2) # removes first instance of 2 in the list

print(x)

x.remove(x[2]) # removes the item at index 2 in the list

print(x)

print(x[5]) # print index 5

print(x[5:7]) # print index 5 to 7 not including 7 (slice)

print(x[5:9]) # print index 5 to 9 not including 9 (slice)

print(x[-1]) # print last index in the list

print(x[-2]) # print next to last index in the list

print(x.index(1)) # get the index value for 1 in the list

print(x.count(6)) # get the number of 6's in the list

x.sort() # sort list intuitivly, in this case numerically

print(x)

y = ['Janet','Jessy','Kelly','Alice','Joe','Bob']

print(y)

y.sort() # sorts list alphabetically

print(y)

 

'''
#29
Python 3 Programming Tutorial - Multi-dimensional List
https://youtu.be/Go-FfGhxbSM
'''
x = [[5,6],[6,7],[7,2],[2,5]]
print(x)
print(x[1])
print(x[1][0])
x = [[[5,7],[6,6]],[[6,6],[7,8]],[7,2],[2,5]]
print(x)
print(x[1][0])
print(x[1][0][0])
x = [
[[5,7],[6,6]],
[[6,6],[7,8]],
 [7,2],[2,5]
    ]
print(x)
print(x[1][0])
print(x[1][0][0])

'''
#30
Python 3 Programming Tutorial - Reading from a CSV spreadsheet
https://youtu.be/K_oXb04izZM
'''
import csv
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #print(readCSV)

    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1])

import csv
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    whatColor = input('What color do you wish to know the date of?')
    coldex = colors.index(whatColor.lower()) #added the "lower()" so that it won't error on incorrect spelling
    theDate = dates[coldex]
    print('The date of',whatColor,'is',theDate)

'''
#31
Python 3 Programming Tutorial - Try and Except error Handling
https://youtu.be/nqGhjLUhyDc
'''

import csv
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('What color do you wish to know the date of?')
        if whatColor in colors:    
            coldex = colors.index(whatColor.lower()) #added the "lower()" so that it won't error on incorrect spelling
            theDate = dates[coldex]
            print('The date of',whatColor,'is',theDate)
        else:
            print('Color not found, or is not a color.')
    # except Exception, e: #in python 2.7
    except Exception as e:
    #except NameError as e:
        print(e)

    print('continuing')

'''
#32
Python 3 Programming Tutorial - Multi-line Print
https://youtu.be/gINlrLx2zNA
'''

print('''
So this is a simple
multi-line
print

++++++++++++++++++++++++++++++
|                            |
|                            |
|           BOX              |
|                            |
|                            |
++++++++++++++++++++++++++++++
    



    ''')

'''
#33
Python 3 Programming Tutorial - Dictionaries
https://youtu.be/YNRc6c0wUA8
'''

# dictionary is same as associative array, unordered assorment of data with keys and values
# use {} to tell python this is a dictionary
exDict = {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17} 
print(exDict)
print(exDict['Jack'])
print('Jack is',exDict['Jack'])
exDict['Tim'] = 14 # adding information to the dictionary
print(exDict)
exDict['Tim'] = 15 # updating information in the dictionary
print(exDict)
del exDict['Tim'] # removes key and value from dictionary
print(exDict)

exDict = {'Jack':[15,'blonde'], 'Bob':[22,'brown'], 'Alice':[12,'black'], 'Kevin':[17,'red']} 
print(exDict['Jack'])
print(exDict['Jack'][0])
print(exDict['Jack'][1])
print('Jack is',exDict['Jack'][0],'years old')
print('Jack has',exDict['Jack'][1],'hair')

'''
#34
Python 3 Programming Tutorial - Built-in Functions
https://youtu.be/7rjJrQy9gi4
'''
#Absolute value, distance from 0
exNum1 = -5
exNum2 = 5
print(abs(exNum1))
if abs(exNum1) == exNum2:
    print('these are the same')
# help function
help()
# urllib, time, 
# goes to help prompt, use ctrl+c to break out
import time
help(time)
# goes directly to help with time
