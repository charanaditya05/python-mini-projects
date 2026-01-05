board=[' ',' ',' ',
        ' ',' ',' ',
        ' ',' ',' ']

def printboard(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f" {board[6]} | {board[7]} | {board[8]}")

printboard(board)

def check_win(board, current_player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == current_player:
            print(f"Player {current_player} has won the game 🎉!")
            return True
    return False

current_player='X'
while True:
    user = int(input(f"Player {current_player}, enter a position (0-8): "))
    if user < 0 or user > 8:
        print("Invalid position. Choose between 0 and 8.")
        continue
    if(board[user]!=' '):
        print("Given index is already taken choose another index on the board")
        continue
    if(board[user]==' '):
        board[user] = current_player
        printboard(board)
        if(check_win(board,current_player)):
            break
        
    if(' ' not in board):
        print("GAME OVER!")
        break
    if(current_player == 'X'):
        current_player = 'O'
    else:
        current_player='X'