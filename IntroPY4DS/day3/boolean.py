a = True
b = False
z = 6
p = 4

x = ('bear','bunny','tree','sky','rain','zoo')
y = 'bear'

print(x[1])
if y not in x[1]:
    if z==6:
      if 'zoo' in x:
        print('it is true')
      else: # this is the 'zoo' in x test
        print ('zoo not in x')
    else:   # this is for the 'z' test
        print('z not 6')
else:  # this is for the 'y' test
    print('it is false')