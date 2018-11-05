#!/usr/bin/python3

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local
    print("bacon Function =",eggs) # this is the local
    
def ham():
    print("ham Function =",eggs) # this is the global

eggs = 42 # this is the global
ham()
spam()
print(eggs)
bacon()
