x = [1,2,3,4,5,6]
y=(5,6,7,8,9,88)
z = range(5,27,5)

p = { 'one':1,'two':2, 'three': 3, 'four':4,'five':5 }
p['three']=66

x[3]=42
for k,v in p.items():
    print('key is {} and val is {}'.format(k,v))

#print(type(x))

#print(type(y))

print(type(p))
