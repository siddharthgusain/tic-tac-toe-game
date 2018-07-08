
# coding: utf-8

# In[1]:


from __future__ import print_function
import time


# In[2]:


from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[3]:


def player_input(player1):
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input(player1+": Do you want to be X or O?").upper()

    if marker == 'X':
        return ('X', 'O')
    elif marker=="O":
        return ('O', 'X')
    else:
        print("Invalid Choice!Enter again")


# In[4]:


def place_marker(board, marker, position):
    board[position] = marker


# In[5]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) 


# In[6]:


import random
def choose_first(player1,player2):
    if random.randint(0, 1) == 0:
        return player1
    else:
        return player2


# In[7]:


def space_check(board, position):
    
    return board[position] == ' '
    


# In[8]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[9]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[10]:


def replay():
    
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[11]:


def player_choice(player,board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = raw_input("Choose your next position "+player+":(1-9)")
    return int(position)


# In[13]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1=raw_input("Enter Name Of Player 1:").upper()
    player2=raw_input("Enter Name Of Player 2:").upper()
    player1_marker, player2_marker = player_input(player1)
    
    turn = choose_first(player1,player2)
    
    print(turn + ' will go first.')
    print("WAIT FOR FEW MINUTES YOUR BOARD IS LOADING.......")
    time.sleep(5)
    game_on = True

    while game_on:
        if turn == player1:
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(player1,theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations!"+player1+ " has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player2

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(player2,theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(player2+" has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = player1

    if not replay():
        print("Exiting please wait.....")
        time.sleep(5)
        clear_output()
        break

