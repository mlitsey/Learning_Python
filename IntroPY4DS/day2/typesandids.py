x = (1,'two',3.0,[4,'four'],5)
y = range(100)

print('x is {}'.format(x))

if isinstance(y,tuple):
    print('is tuple')
elif isinstance(y,list):
    print('is list')
else:
    print('ufo')

print(id(x))
print(id(y))