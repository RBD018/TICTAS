from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('Note : The position on the board')    
    print('-------------------------------------------------------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    marker = ''
    name_p1 = input('Enter P1 Name ')
    name_p2 = input('Enter P2 Name ')
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 please enter the marker (X / O) ----> ').upper()
        if marker == 'X':
            return ('X','O')
        elif marker == 'O':
            return ('O','X')
        else:
            print('Please choose correct marker from (X / O) ')
    print('Lets start the game')
	

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return((board[1] ==  mark and board[2] == mark and board[3] == mark) or
    (board[4] ==  mark and board[5] == mark and board[6] == mark) or
    (board[7] ==  mark and board[8] == mark and board[9] == mark) or
    (board[1] ==  mark and board[4] == mark and board[7] == mark) or
    (board[2] ==  mark and board[5] == mark and board[8] == mark) or
    (board[3] ==  mark and board[6] == mark and board[9] == mark) or
    (board[1] ==  mark and board[5] == mark and board[9] == mark) or
    (board[3] ==  mark and board[5] == mark and board[7] == mark))

import random

def choose_first():
    if random.randint(1,2) == 1:
        return ('1')
    else:
        return ('2')
		

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
         position = int(input('Choose your next position: (1-9) '))

    return position

def replay():
    play_again = ''
    while not (play_again == 'Y' or play_again =='N'):
        play_again = input('Do you want to play again (Y / N ): ').upper()
        if play_again == 'Y':
            return True
        elif play_again == 'N':
            return False
        else:
            print('Please enter valid input : (Y - Yes / N - No ) ')

print('Welcome to Tic Tac Toe!')


while True:
    
    p1_M,p2_M = player_input()
    turn = choose_first()
    print('Player {} will go first '.format(turn))
    game = input('Do you want to start the game. Yes(Y) / No(N) : ').upper()
    board = [' ']*10
    if game == 'Y':
        game_on = True
    elif game == 'N':
        game_on = False
    else:
        print('Please enter valid Input Y or N ,to continue the game')
    
    while game_on:
        if turn == '1':
            display_board(board)
            pos = int(player_choice(board))
            place_marker(board,p1_M,pos)
            if win_check(board, p1_M):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw')
                    game_on = False
                else:
                    turn = '2'
        else:
            #player 2
            display_board(board)
            pos = int(player_choice(board))
            place_marker(board,p2_M,pos)
            if win_check(board, p2_M):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw')
                    game_on = False
                else:
                    turn = '1'
                    
    if not replay():
            break

