def main():
    x = 5   # x will be passed by value
    x = kitten(x)  # x is being passed by value
    print(x)  # the value of x will be return value from function
    
def kitten(n):
    print(f'{n} was passed')
    print('will pass back the number 10')
    return 10

main()