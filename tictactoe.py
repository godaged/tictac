import os


board=[" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
pc = ""
player = ""

def printBoad():
    os.system('cls ||clear')
    row = ''
    leftPadding = " " * 5
    print(leftPadding, "Tic Tac Toe")
    print(leftPadding, "===========")

    for index in range(len(board)):
        index += 1
        if index%3 == 0:
            row += str(board[index-1])
            devider = '\n {}---|----|---'.format(leftPadding)
            if index == 9:
                devider = ''
            print(leftPadding, row, devider)
            row = ''
        if index%3 != 0:
            row += str(board[index-1]) + '  | '

def selectCharacter():
    val = input("Enter your mark ('X'/'O') : ").upper()
    if val not in ('X', 'O'):
        val = ""
        selectCharacter()
    else:
        player = val         
        pc = 'O' if player == 'X' else 'X'
        print("Player = {}, PC = {}".format(player, pc))



# def playGame():
#     selectCharacter()
#     printBoad()
#     pass

# selectCharacter()


# if __name__ == "__main__":
#     playGame()