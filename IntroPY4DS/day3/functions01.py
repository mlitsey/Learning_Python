def main():    #definition of function called main
    x=kitten(7)  #called the kitten function with
                 #the parameter value of 3
    
    for thisname in x:
        print(thisname)
    
def kitten(n):          #definition of a function called kitten
                        #that allows parameter value to be passed in
    print(f'{n} Meow')  # displays the param value passed in
                        # before the 'meow' message
    
    return ('alex','tim','jane')

main() # calling the main function