import os

pc = ""
player = ""
leftPadding = " " * 5
moves = range(1,10)

def setUpList():
    # initialize the list
    emptyList = []
    for _ in range(9):
        emptyList.append("")
    return emptyList

def isBoardEmpty(board, index):
    # return " " if cell is empty else return cell value.
    cellValue = ""
    if len(board[index]) > 0:
        cellValue = board[index]
    else:
        cellValue = " "
    return cellValue

def selectTurnAndMarker():
    # Select the marker and first turn of your choice
    #os.system('cls ||clear')
    whoFirst = ["Player", "PC"]
    markers = ['X', 'O']
    marker = ''
    print()
    print(leftPadding * 4 , "Tic Tac Toe")
    print(leftPadding * 4 , "===========")

    pcOrPlayer = -1 
    while pcOrPlayer not in (0, 1):
        answer = input(leftPadding + " Play against PC or another player(Player = 0, pc = 1) ? ")
        if answer in ("0", "1"):
            pcOrPlayer = int(answer)

    playAgainst = whoFirst[pcOrPlayer]

    # Select the marker
    while marker not in markers:
        marker = input(leftPadding + " Player 1, Select your marker('X' goes first) ('X'/'O') : ").upper()
        if marker not in markers:
            marker = ""
    
    return playAgainst, marker

def printBoard(board):
    # prints the board.
    #os.system('cls ||clear')
    row = ''
    print()
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

def getLocation(player):
    # get only integer
    question = leftPadding + " '{}' turn, What place do you want to mark (1-9)? ".format(player)
    move = input(question)
    while not move.isnumeric():
        print(leftPadding + " '{}' is not a valid entry".format(move.upper()) + "\n" + leftPadding + " Enter number between 1 and 9")
        move = input(question)
    return int(move)

def playerMove(board, player):
    # make your move 1 to 9 otherwise out of range
    # if already filled, select empty cell
    move = 1
    while move in moves:
        move = getLocation(player)
        if move not in moves:
            print(leftPadding + " {} is out of range".format(move))
            move = 1
        elif isBoardEmpty(board, move-1) == " ":
            board[move-1] = player
            break
        else:
            print(leftPadding + " {} th place is already taken.".format(move))

def pcMove(board, pc, player, index, turn):
    # PC moves
    i = index + 1
    corners = (0, 2, 6, 8)
    if board.count("") == 9:
        if(turn == "PC"):
            board[4] = pc
    elif board.count("") == 8:
        for i in corners:
            if board[4] == "":
                board[4] = pc
            elif board[corners[i]] == "":
                board[corners[i]] = pc
                break
    elif board.count("") == 7:
        for i in corners:
            if board[4] == "":
                board[4] = pc
            elif board[corners[i]] == "":
                board[corners[i]] = pc
                break
    elif board.count("") == 6:
        pass
    # TBD

def setMessage(against, marker, pc):
    message = "\n" + leftPadding + " Player 1 = " + marker
    if against == "PC":
        message += '\n' + leftPadding + " PC = " + pc
    else:
        message += '\n' + leftPadding + " Player 2 = " + pc
    return message

def CheckWin(board, sign):
    message = ""
    if board.count("") <= 4:
        b = board
        win = leftPadding + " {} won the game".format(sign)
        if b[0] == b[1] == b[2] == sign:
            message = win
        elif b[3] == b[4] == b[5] == sign:
            message = win
        elif b[6] == b[7] == b[8] == sign:
            message = win
        elif b[0] == b[3] == b[6] == sign:
            message = win
        elif b[1] == b[4] == b[7] == sign:
            message = win
        elif b[2] == b[5] == b[8] == sign:
            message = win
        elif b[0] == b[4] == b[8] == sign:
            message = win
        elif b[2] == b[4] == b[6] == sign:
            message = win
        elif b.count("") == 0:
            message =  leftPadding + " No one won the game"
    return message

def playGame(board):
    # plays the game.
    against, marker = selectTurnAndMarker()
    pc = 'O' if marker == 'X' else 'X'

    # 'X' goes first
    turn = "X"

    # Set message
    message = setMessage(against, marker, pc)

    # Print empty board
    printBoard(board)
    print(message)

    # Start the game
    for i in range(9):
        
        # Play againt PC (Need to fix this if)
        if against == "PC" and board.count("") < 9:
            pcMove(board, pc, marker, i, against)
            printBoard(board)
            print(message)

        playerMove(board, turn)
        printBoard(board)
        print(message)
        isWin = CheckWin(board, turn)
        if len(isWin) > 1:
            print(isWin)
            break

        turn = "O" if turn == "X" else "X"

        if board.count("") == 0:
            break

if __name__ == "__main__":
    cont = "y"
    while cont == "y":
        board =  setUpList()
        playGame(board)
        cont = input(leftPadding + " Do you want to play another game(y = yes, n = no) ? ")



