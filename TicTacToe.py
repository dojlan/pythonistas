# Milestone Project 1 - Tic Tac Toe
def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


board = ['#','X','O','X','O','X','O','X','O','X']
print(display_board(board))

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ")
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        return (player1, player2)


print(player_input())

#position = int(input('Please enter a number'))
#  a = ['#','X','O','X','O','X','O','X','O','X']
#    for i in board:
#        for j in range(10):
#            i == j
#    return(f"{i} is equal to {j}")
#a = ['#','X','|','X','|','X','|','X','|','X']
# b = a[1:4]
# c = a[4:7]
# d = a[7:]
# e = b + c + d
# nulist = [b, c, d]
# for n in nulist:
#    for m in n:
#        print(m, end=' ')
#    print()
