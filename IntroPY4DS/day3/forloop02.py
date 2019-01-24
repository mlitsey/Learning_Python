animals = ('bear','bunny','dog','cat','velociraptor')
broken=True
for pet in animals:
    if pet == 'dog': continue
    #if pet == 'velociraptor': break
    print(pet)
else:
    broken=False
    print('that is all of the animals')

print('broken' if broken else 'not broken')    
# display a message that shows if the 'for loop' was
# 'broken' or 'completed'

