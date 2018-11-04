#Lesson 5
#making tic-tac-toe

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game[0][1] = 1

print('   a  b  c')

for count2, row in enumerate(game):
    print(count2, row)
    
# refrence index
"""
l = [1,2,3,4,5]
print(l[1])
print(l[4])
print(l[-1])
print(l[1:4]) #slice
print(l[2:]) #slice to end of line
print(l)
l[1] = 99
print(l)
"""