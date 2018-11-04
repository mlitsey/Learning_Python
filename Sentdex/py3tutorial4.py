#Lesson 4
#making tic-tac-toe

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
print('   0  1  2')
count = 0

for row in game:
    print(count, row)
    count += 1 # or count = count + 1

print('   a  b  c')
for count2, row in enumerate(game):
    print(count2, row)
    
