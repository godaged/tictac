import os
import datetime

class TicTacToe:
    def __init__(self):
        self.pc = ""
        self.player = ""
        self.leftPadding = " " * 5
        self.moves = range(1,10)

    def setUpList(self):
        # Declare and initialize the list.
        emptyList = []
        for _ in range(9):
            # Populate list with empty string "".
            emptyList.append("")
        return emptyList

    def isBoardEmpty(self, board, index):
        # Check cell of the board is empty.
        # return " " if cell is empty else return cell value.
        cellValue = ""
        if len(board[index]) > 0:
            cellValue = board[index]
        else:
            cellValue = " "
        return cellValue

    def printGameTitle(self):
        print()
        print("    ______  @                                                                    ") 
        print("   /   |  \       ___   __|__   ___      __   __|__   __     __      1 | 2  | 3  ") 
        print("       |    |    /   \    |    /   |    /  \    |    /\ \   /  \   ----|----|----") 
        print("       |    |   |         |   |    |   |        |   |  \ | |   /     4 | 5  | 6  ")    
        print("       |    |   |         |   |    |   |        |   |   \|_|__/    ----|----|----") 
        print("       | __/ \_/ \___/   /\__/ \__/ \_/ \__/   / \_/ \__/   \__/     7 | 8  | 9  ")
        print("     ============================================================>   By Dan God  ") 
        print()

    def WriteToFile(self, text):
        with open("log.txt", "a") as logFile:
            logFile.write(text + "\n")

    def selectTurnAndMarker(self):
        # Select the marker and first turn of player 1's choice
        os.system('cls ||clear')
        playChoice = ["Player", "PC"]
        markerChoice = ['X', 'O']
        marker = ''
        print()
        self.printGameTitle()

        # Initialize with -1
        pcOrPlayer = -1 
        while pcOrPlayer not in (0, 1):
            answer = input(self.leftPadding + " Play against PC or another player(Player = 0, pc = 1) ? ")
            if answer in ("0", "1"):
                pcOrPlayer = int(answer)
        # Selected value of play against PC or another player
        playAgainst = playChoice[pcOrPlayer]

        if playAgainst == "Player":
            # Select the marker, if only play against another player
            while marker not in markerChoice:
                marker = input(self.leftPadding + " Player 1, Select your marker('X' goes first) ('X'/'O') : ").upper()
                if marker not in markerChoice:
                    marker = ""
        else:
            # Player goes first withplaying against PC and marker is 'X'
            print(self.leftPadding + " Player goes first with 'X'")
            marker = "X"

        return playAgainst, marker

    def printBoard(self, board):
        # prints the board.
        os.system('cls ||clear')
        row = ''
        self.printGameTitle()
        for index in self.moves:
            # start index with 1.
            if index%3 == 0:
                # print row and devider if reached to third cell of the row.
                row += str(self.isBoardEmpty(board, index - 1))
                devider = '\n {}---|----|---'.format(self.leftPadding)
                if index == 9:
                    # do not print devider if reached to 9th cell
                    devider = ''
                print(self.leftPadding, row, devider)
                row = ''
            #if index%3 != 0:
            else:
                # set first and second sell value content of the row.
                row += str(self.isBoardEmpty(board, index-1)) + '  | '

    def getLocation(self, player):
        # get only integer
        question = "\n" + self.leftPadding + " '{}' turn, What place do you want to mark (1-9)? ".format(player)
        move = input(question)
        while not move.isnumeric():
            print(self.leftPadding + " '{}' is not a valid entry".format(move.upper()) + "\n" + self.leftPadding + " Enter number between 1 and 9")
            move = input(question)
        return int(move)

    def playerMove(self, board, player):
        # make your move 1 to 9 otherwise out of range
        # if already filled, select empty cell
        move = 1
        while move in self.moves:
            move = self.getLocation(player)
            if move not in self.moves:
                print(self.leftPadding + " {} is out of range".format(move))
                move = 1
            elif self.isBoardEmpty(board, move-1) == " ":
                board[move-1] = player
                #self.WriteToFile(', '.join(board))
                break
            else:
                print(self.leftPadding + " {} th place is already taken.".format(move))

    def setMessage(self, against, marker, pc):
        # This sets the Player marker and PC marker
        message = "\n" + self.leftPadding + " Player 1 = " + marker
        if against == "PC":
            message += '\n' + self.leftPadding + " PC = " + pc
        else:
            message += '\n' + self.leftPadding + " Player 2 = " + pc
        return message

    def checkWin(self, board, sign):
        # Check who won or no one won.
        message = ""
        if board.count("") <= 4:
            win = self.leftPadding + " {} won the game".format(sign)
            if board[0] == board[1] == board[2] == sign:
                message = win
            elif board[3] == board[4] == board[5] == sign:
                message = win
            elif board[6] == board[7] == board[8] == sign:
                message = win
            elif board[0] == board[3] == board[6] == sign:
                message = win
            elif board[1] == board[4] == board[7] == sign:
                message = win
            elif board[2] == board[5] == board[8] == sign:
                message = win
            elif board[0] == board[4] == board[8] == sign:
                message = win
            elif board[2] == board[4] == board[6] == sign:
                message = win
            elif board.count("") == 0:
                message =  self.leftPadding + " No one won the game"
        return message

    def pcMove(self, board, pc, player):
        # This decides how PC moves against player
        # PC's preffered move order
        cellNumber = (4, 0, 2, 6, 8, 1, 3, 5, 7)
        block = success = ""
        if board.count("") == 8:
            # PC's first move
            for i in cellNumber:
                if board[i] == "":
                    board[i] = pc
                    break
        elif board.count("") <= 6:
            # PC's 2nd and subsequent moves to win or block
            success = self.blockOrWin(board, pc, "O")
            if not success:
                block = self.blockOrWin(board, pc, "X")
        if not success and not block and board.count("") <= 6:
            # PC's 2nd and subsequent moves in prefered order
            for i in cellNumber:
                if board[i] == "":
                    board[i] = pc
                    break

    def blockOrWin(self, board, pc, marker):
        # This will decide which cell, PC should be marked.
        # loop through each touple to decide the prefered cell to move.
        blockers = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        found = False
        for blocker in blockers:
            found = False
            x = blocker[0]
            y = blocker[1]
            z = blocker[2]
            if board[x] == board[y] == marker and board[z] == "":
                board[z] = pc
                found = True
            elif board[x] == board[z] == marker and board[y] == "":
                board[y] = pc
                found = True
            elif board[y] == board[z] == marker and board[x] == "":
                board[x] = pc
                found = True
            if found == True:
                return found
        return found

    def playGame(self, board):
        # This will play the game.
        against, marker = self.selectTurnAndMarker()
        pc = 'O' if marker == 'X' else 'X'

        # 'X' goes first
        turn = "X"

        # Set message
        message = self.setMessage(against, marker, pc)
        now = datetime.datetime.now()
        self.WriteToFile("\n" + now.strftime("%m/%d/%Y %H:%M:%S")  + "\n" + message.strip())
        
        # Print empty board
        self.printBoard(board)
        print(message)

        # Start the game
        for _ in range(9):
            
            # Play againt PC (Need to fix this if)
            if against == "PC" and board.count("") < 9:
                self.pcMove(board, pc, marker)
                self.printBoard(board)
                self.WriteToFile(', '.join(board))
                print(message)
                win = self.checkWin(board, pc)
                if "won the game" in win:
                    self.WriteToFile(win.strip())
                    print("\n" + win + "\n")
                    break

            self.playerMove(board, turn)
            self.printBoard(board)
            self.WriteToFile(', '.join(board))
            print(message)
            win = self.checkWin(board, turn)
            if "won the game" in win:
                self.WriteToFile(win.strip())
                print("\n" + win + "\n")
                break

            if against == "Player":
                turn = "O" if turn == "X" else "X"

            if board.count("") == 0:
                break



if __name__ == "__main__":
    ttt = TicTacToe()
    cont = "y"
    while cont == "y":
        board =  ttt.setUpList()
        ttt.playGame(board)
        cont = input(ttt.leftPadding + " Do you want to play another game(y = yes, n = no) ? ")
