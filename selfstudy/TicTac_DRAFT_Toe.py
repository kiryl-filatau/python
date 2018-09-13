#from IPython.display import clear_output
#### FUNCTIONS ####


# fix that board is shown after each step
def display_board(board):
    print(' ' + board[6]+ ' | ' +board[7]+ ' | ' +board[8] + ' ')
    print('-----------')
    print(' ' + board[3]+ ' | ' +board[4]+ ' | ' +board[5] + ' ')
    print('-----------')
    print(' ' + board[0]+ ' | ' +board[1]+ ' | ' +board[2] + ' ')


def player_choice():
    choice = input('select X or O: ')
    if choice.lower() == 'x':
        print(f'you choice is {choice.upper()} you will play as Player 1')
    elif choice.lower() == 'o':
        print(f'you choice is {choice.upper()} you will play as Player 2')
    else:
        print("you should choose only between X and O")
    return choice


def player_number(order):
    while True:
        try:
            step = int(input(f'Player {order} could you please enter number from 1 to 9: '))
            if step in range(1,10):
                return step
            else:
                return ValueError
        except ValueError:
            print('The value you entered is not a number')
            continue
        else:
            break
    
def player_1(start_board):
    step = player_number('1')
    if step in range(1,10):
        if start_board[step-1] == ' ':
            start_board[step-1] = 'X'
        else:
            print('This cell was already used')
            return False
    else:
        print('Value is out of range 1 to 9')
        return False
    return start_board

def player_2(start_board):
    step = player_number('2')
    if step in range(1,10):
        if start_board[step-1] == ' ':
            start_board[step-1] = 'O'
        else:
            print('This cell was already used')
            return False
    else:
        print('Value is out of range 1 to 9')
        return False
    return start_board

# fix draw and skip if no winner is possible

def win(start_board,winner):
    check_board = [
        [start_board[0],start_board[1],start_board[2]],
        [start_board[3],start_board[4],start_board[5]],
        [start_board[6],start_board[7],start_board[8]]
    ]
    for sets in winner_board:
        win_lines = [check_board[x][y] for (x,y) in sets]
        print(win_lines)
        if len(set(win_lines)) == 1 and win_lines[0] == 'X':
            print('The winner is Player 1')
            winner = False
            exit()
        elif len(set(win_lines)) == 1 and win_lines[0] == 'O':
            print('The winner is Player 2')
            winner = False
            exit()

#### VARIABLES ####

check_choise = True
first_player_step = True
winner = True
start_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
winner_board = (
    [[(x,y)for y in range(3)] for x in range(3)] +
    [[(x,y)for x in range(3)] for y in range(3)] + 
    [[(d,d)for d in range(3)]] +
    [[(2-d,d)for d in range(3)]]
)
#### LOGIC ####

while check_choise:
    player_input = player_choice()
    if player_input.lower() == 'x' or player_input.lower() == 'o':
        check_choise = False
        break

while winner:
    while first_player_step:
        if player_1(start_board):
            display_board(start_board)
            first_player_step = False
            win(start_board,winner)
        break
    while not first_player_step:
        if player_2(start_board):
            display_board(start_board)
            first_player_step = True
            win(start_board,winner)
        break
    
