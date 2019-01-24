def f(i): #Investigate ID stuff
    print(id(i))
    if type(i) ==int:
        i+=1
        print(id(i))
    elif type(i) == list:
        i.append(4)
        print(id(i))
    
x = 5       #small int: IDs are shared
y = 5005    #big int: id individually assigned
z = [1,2,3] #list: object ID behaviors

print('x')
print(id(x)) #original ID
f(x)         #display ID received, ID of increment, and result ID
print("{} = {}".format(id(x), x))

print('\ny')
print(id(y)) #original ID
f(y)         #display ID received, ID of increment, and result ID
print("{} = {}".format(id(y), y))

print('\nz')
print(id(z)) #original ID
f(z)         #f appends, but the list is the same object before and after
print("{} = {}".format(id(z), z)) #verify ID remained the same