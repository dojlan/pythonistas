# Milestone Project 1 - Tic Tac Toe

#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9
# corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


#board = ['#','X','O','X','O','X','O','X','O','X']
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#print(display_board(board))


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
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

#print(player_input())


#

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    display_board(board)
    marker == board[position]

#print(place_marker(board,'X',8))


# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, marker):
    display_board(board)
    return (marker == board[7] == board[8] == board[9] or
            marker == board[4] == board[5] == board[6] or
            marker == board[1] == board[2] == board[3] or
            marker == board[1] == board[4] == board[7] or
            marker == board[2] == board[5] == board[8] or
            marker == board[3] == board[6] == board[9])

#print(win_check(board,'X'))


# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
import random

def choose_first():
    your_select = ['X', 'O']
    my_choice = random.choice(your_select)
    return (f"It is player {my_choice}'s turn to play")

#print(choose_first())

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    #position = int(input('Please enter a number: '))
    return board[position] == 'X' or board[position] == 'O'

#print(space_check(board, 8))


# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full,
# False otherwise.
def full_board_check(board):
    my_count = 0
    for space in board:
        if space == 'X' or space == 'O':
            my_count += 1
    if my_count == 9:
        print("Board is Full")
    else:
        print("Board is not full yet")


def full_board_check2(board):
    for space in board:
        if space == ' ':
            return "Board is not full yet"
    else:
        return "Board is Full"

#print(full_board_check2(board))


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses
# the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = int(input('Please enter your next number: '))
    if position > 1 and position <= 9:
        return space_check(board, position)
    else:
        return "Please enter a number between 1 and 9"

#print(player_choice(board))

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True
# if they do want to play again.
def replay():
    player = input("Do you want to play again? Yes or No: ")
    if player == 'Yes':
        return True
    else:
        return False

#print(replay())

#

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
print('Welcome to Tic Tac Toe!')

while True:
    print(display_board(board))

# Set the game up here
    game_on = True
    while game_on:
        # Player 1 Turn
        print(player_input())


        # Player2's turn.


    if not replay():
        break
