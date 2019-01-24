def main():
    y=[5]
    print(id(y))
    kitten(y)   # passes a reference
    print(id(y))
    print(y)


def kitten(a):
    print(f'{a} was passed in')
    print(id(a))
    a[0]=3
    print(id(a))
    print('meow')
    
main()