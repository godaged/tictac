import os

# initialize the board, pc, player and left spacing.
board = ["", "", "", "", "", "", "", "", "", ]
pc = ""
player = ""
leftPadding = " " * 5

def isBoadEmpty(board, index):
    # return " " if cell is empty else return cell value.
    cellValue = ""
    if len(board[index]) > 0:
        cellValue = board[index]
    else:
        cellValue = " "
    return cellValue

def printBoard():
    # prints the tic tac toe board.
    #os.system('cls ||clear')
    row = ''
    print(leftPadding, "Tic Tac Toe")
    print(leftPadding, "===========")

    for index in range(len(board)):
        # start index with 1 => 0 + 1.
        index += 1
        if index%3 == 0:
            # print row if reached to thirs cell of the row.
            row += str(isBoadEmpty(board, index - 1))
            devider = '\n {}---|----|---'.format(leftPadding)
            if index == 9:
                # do not print devider if reached to 9th cell
                devider = ''
            print(leftPadding, row, devider)
            row = ''
        if index%3 != 0:
            # set first and second sell value content of the row.
            row += str(isBoadEmpty(board, index-1)) + '  | '

def selectMarker():
    # set the marker of your choice
    markers = ['X', 'O']
    marker = ''
    while marker not in markers:
        marker = input(" Enter your marker ('X'/'O') : ").upper()
        if marker not in ('X', 'O'):
            marker = ""  
    return marker

def makeMove(board, player):
    # make your move 1 to 9 otherwise out of range
    # if already filled, select empty cell
    move = 1
    moves = range(1,10)
    while move in moves:
        move = int(input(" Select what place you want to mark?"))
        if move not in moves:
            print(" {} is out of range".format(move))
            move = 1
        elif isBoadEmpty(board, move-1) == " ":
            board[move-1] = player
            break
        else:
            print(" {} th place is already taken".format(move))

def playGame():
    # plays the game.
    player = selectMarker()
    pc = 'O' if player == 'X' else 'X'
    printBoard()
    print()
    print(leftPadding, " Player = {}\n".format(player), leftPadding, "PC = {}".format(pc))
    makeMove(board, player)
    printBoard()
    pass

if __name__ == "__main__":
    playGame()