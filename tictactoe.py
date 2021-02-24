import os

# initialize the board, pc, player and left spacing.
board = ["", "", "", "", "", "", "", "", "", ]
pc = ""
player = ""
leftPadding = " " * 5
moves = range(1,10)

def isBoardEmpty(board, index):
    # return " " if cell is empty else return cell value.
    cellValue = ""
    if len(board[index]) > 0:
        cellValue = board[index]
    else:
        cellValue = " "
    return cellValue

def selectMarker():
    # set the marker of your choice
    markers = ['X', 'O']
    marker = ''
    while marker not in markers:
        marker = input(" Enter your marker ('X'/'O') : ").upper()
        if marker not in ('X', 'O'):
            marker = ""  
    return marker

def printBoard(board):
    # prints the tic tac toe board.
    os.system('cls')
    row = ''
    print(leftPadding, "Tic Tac Toe")
    print(leftPadding, "===========")

    for index in moves:
        # start index with 1.
        if index%3 == 0:
            # print row and devider if reached to third cell of the row.
            row += str(isBoardEmpty(board, index - 1))
            devider = '\n {}---|----|---'.format(leftPadding)
            if index == 9:
                # do not print devider if reached to 9th cell
                devider = ''
            print(leftPadding, row, devider)
            row = ''
        #if index%3 != 0:
        else:
            # set first and second sell value content of the row.
            row += str(isBoardEmpty(board, index-1)) + '  | '
        if board.count("") == 0:
            exit()

def getLocation(player):
    # get only integer
    question = " '{}', What place do you want to mark (1-9)? ".format(player)
    move = input(question)
    while not move.isnumeric():
        print(" '{}' is not a valid entry".format(move.upper()) + "\n  Enter number between 1 and 9")
        move = input(question)
    return int(move)

def playerMove(board, player):
    # make your move 1 to 9 otherwise out of range
    # if already filled, select empty cell
    move = 1
    while move in moves:
        move = getLocation(player)
        if move not in moves:
            print(" {} is out of range".format(move))
            move = 1
        elif isBoardEmpty(board, move-1) == " ":
            board[move-1] = player
            break
        else:
            print(" {} th place is already taken.".format(move))

def playGame(board):
    # plays the game.
    player = selectMarker()
    pc = 'O' if player == 'X' else 'X'
    message = "\n" + leftPadding + " Player = " + player + '\n' + leftPadding + " PC = " + pc
    printBoard(board)
    for _ in range(5):
        print(message)
        playerMove(board, player)
        printBoard(board)
        print(message)
        playerMove(board, pc)
        printBoard(board)
        pass

if __name__ == "__main__":
    playGame(board)