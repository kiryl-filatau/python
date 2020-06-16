from IPython.display import clear_output
import os, random
#### FUNCTIONS ####
#just for printing rules when game starts
def rules_func():
    print('Here is TicTacToe game\n' 
          'You can choose "X" or "O" to fil the table.\n'
          'The winner is the player who will fill\n'
          'the vertical or horisontal lines in the table\n'
          'please enter numbers 1-9 according the positions\n'
          'in the board:')
#printing board with numbers
def info_board_func(info_board):
    display_board(info_board)
#for displaying board
def display_board(board):
    print('          ' + board[6]+ ' | ' +board[7]+ ' | ' +board[8] + ' ')
    print('         -----------')
    print('          ' + board[3]+ ' | ' +board[4]+ ' | ' +board[5] + ' ')
    print('         -----------')
    print('          ' + board[0]+ ' | ' +board[1]+ ' | ' +board[2] + ' ')
#random choice who will start
def who_is_first(player1,player2):
    os.system('clear')
    order = [player1,player2]
    player1 = random.choice(order)
    order.remove(player1)
    player2 = order[0]
    print(f'{player1} will play first and use "X" and {player2} will play second and use "O"')
    info_board_func(info_board)
    return[player1,player2]

#to chose number for proper cell
def player_number(player):
    while True:
        try:
            step = int(input(f'{player} could you please enter number from 1 to 9: '))
            if step in range(1,10):
                os.system('clear')
                return step
            else:
                return ValueError
        except ValueError:
            os.system('clear')
            print('The value you entered is not a number')
            display_board(start_board)
            continue
        else:
            break
#player 1 step 
def player_1(start_board,player1):
    step = player_number(player1)
    if step in range(1,10):
        if start_board[step-1] == ' ':
            start_board[step-1] = 'X'
            display_board(start_board)
        else:
            os.system('clear')
            print('This cell was already used')
            display_board(start_board)
            return False
    else:
        print('Value is out of range 1 to 9')
        return False
    return start_board
#player 2 step
def player_2(start_board,player2):
    step = player_number(player2)
    if step in range(1,10):
        if start_board[step-1] == ' ':
            start_board[step-1] = 'O'
            display_board(start_board)
        else:
            os.system('clear')
            print('This cell was already used')
            display_board(start_board)
            return False
    else:
        print('Value is out of range 1 to 9')
        return False
    return start_board
#### skip if no winner is possible ####
#define that someone wins
def win(start_board,winner,player1,player2,play):
    check_board = [
        [start_board[0],start_board[1],start_board[2]],
        [start_board[3],start_board[4],start_board[5]],
        [start_board[6],start_board[7],start_board[8]]
    ]
    for sets in winner_board:
        win_lines = [check_board[x][y] for (x,y) in sets]
        # print(win_lines)
        if len(set(win_lines)) == 1 and win_lines[0] == 'X':
            print(f'The winner is {player1}')
            winner = False
            ask_to_continue(play,winner)
            exit()
        elif len(set(win_lines)) == 1 and win_lines[0] == 'O':
            print(f'The winner is {player2}')
            winner = False
            ask_to_continue(play,winner)
            exit()
    for sets in winner_board:
        if ' ' not in start_board:
            print('The winner is friendship')
            winner = False
            ask_to_continue(play,winner)
            exit()

def ask_to_continue (play,winner):
    while True:
        try:
            continue_answer = input('Would you like to play one more time?')
            print (continue_answer)
            if continue_answer.lower() == "yes":
                print('huj')
                play = True
                winner = True
            elif continue_answer.lower() == "no":
                print('piuzda')
                play = False
                exit()
            else:
                print('jopa')
                return ValueError
        except ValueError:
            print('Please enter "yes" or "no"')
            continue
        else:
            break

def tik_tok(winner,play,start_board,players,first_player_step,player_1,player2,check_choise):
    while check_choise:
        players = who_is_first(player1,player2)
        if True:
            check_choise = False
            break

    while winner or play:
        try:
            if first_player_step:
                if player_1(start_board,players[0]):
                    first_player_step = False
                    win(start_board,winner,players[0],players[1],play)
                    continue
            elif not first_player_step:
                if player_2(start_board,players[1]):
                    first_player_step = True
                    win(start_board,winner,players[0],players[1],play)
                    continue
            else:
                return ValueError
        except ValueError:
            continue
        else:
            break

#### VARIABLES ####
check_choise = True
first_player_step = True
winner = True
start_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
info_board = ['1','2','3','4','5','6','7','8','9']
winner_board = (
    [[(x,y)for y in range(3)] for x in range(3)] +
    [[(x,y)for x in range(3)] for y in range(3)] + 
    [[(d,d)for d in range(3)]] +
    [[(2-d,d)for d in range(3)]]
)
play = True
players = ''

#### LOGIC ####
rules_func()
info_board_func(info_board)
player1 = input('could you please enter your name, one of you:  ')
player2 = input('another one: ')

tik_tok(winner,play,start_board,players,first_player_step,player1,player2,check_choise)
