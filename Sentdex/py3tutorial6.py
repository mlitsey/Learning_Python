#Lesson 6
#making tic-tac-toe

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board():
    print('   a  b  c')
    for count2, row in enumerate(game):
        print(count2, row)


game_board()

game[0][1] = 1

game_board()
