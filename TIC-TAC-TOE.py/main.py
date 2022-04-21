from IPython.display import clear_output

def user_input():
    clear_output()
    marker=input("Please pick a marker to play the game. Choose 'X' or 'O': ").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')

def display_board(board):
    print('     |    |     ')
    print(f'  {board[0]}  |  {board[1]} |  {board[2]} ')
    print('     |    |     ')
    print('----------------')
    print('     |    |     ')
    print(f'  {board[3]}  |  {board[4]} |  {board[5]}')
    print('     |    |     ')
    print('----------------')
    print('     |    |     ')
    print(f'  {board[6]}  |  {board[7]} |  {board[8]}')
    print('     |    |     ')

def marker_position(board,marker,position):
    board[position]=marker

def win_check(board, marker):
    return ((board[0]==marker and board[1]==marker and board[2]==marker) or
    (board[3]==marker and board[4]==marker and board[5]==marker) or
    (board[6]==marker and board[7]==marker and board[8]==marker) or
    (board[0]==marker and board[3]==marker and board[6]==marker) or
    (board[1]==marker and board[4]==marker and board[7]==marker) or
    (board[6]==marker and board[7]==marker and board[8]==marker) or
    (board[0]==marker and board[4]==marker and board[8]==marker) or
    (board[2]==marker and board[4]==marker and board[6]==marker))

import random
from typing import ForwardRef
def first_player():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_checK(board,position):
    if board[position]==' ':
        return True

def full_board_check(board):
    for i in range(0,10):
        if space_checK(board,i):
            return False
    return True

def palyers_choice(board):
    position=0
    position=int(input("Enter the postion you want to set your marker on. (1-9): "))
    if position in [1,2,3,4,5,6,7,8,9] and space_checK(board,position):
        return position

def replay():
    rep=input("Do you want to play again? If yes press y or to exit press n: ").lower()
    return rep=='y'

print("Welcome to TIC TAC TOE developed by THEBOSS")
while True:

    player1_marker,player2_marker=user_input()
    turn=first_player()
    print(f"{turn} will go first.")

    start_game=input("Are you ready to play? Enter y to start or no to exit: ").lower()
    if start_game=='y':
        rungame=True
    else:
        rungame=False

    while rungame:
        if turn=='Player 1':
            board=[' ']*10
            display_board(board)
            position=palyers_choice(board)
            marker_position(board,player1_marker,position)
            display_board(board)
            if win_check(board,player1_marker):
                display_board(board)
                print("\nCongratulations! You have won the game!")
                rungame=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nThe game is drawn.")
                    break
                else:
                    turn='Player 2'

        elif turn=='Player 2':
            board=[' ']*10
            display_board(board)
            position=palyers_choice(board)
            marker_position(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("\nPlayer 2 has won the game!")
                rungame=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("\nThe game is drawn.")
                    break
                else:
                    turn='Player 1'
    if not replay():
        break
   
