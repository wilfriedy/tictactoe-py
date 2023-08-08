gameboard = [[' ', ' ',  ' '],[' ', ' ',  ' '],[' ', ' ',  ' ']]
players = ["X", "Y"]
player_track = 0
gameOver = False

def drawBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2 :
             print('|', end="")
        print("")
        if i < 2 :
            print("-" * 5)


def swithPlayers(players, currentPlayer):
    print(f"{players[currentPlayer]} is playing")
    row = int(input("Select a row (0-2): "))
    column = int(input("Select a column (0-2): "))

    if 0 <= row <= 2 or 0 <= column <= 2:
        if gameboard[row][column] != " ":
            print(f"Please that box has been selected already")
            return False
        else:
            gameboard[row][column] = players[currentPlayer]
            return True
    else:
        print(f"Please select within range of (0-2)")
        return False



drawBoard(gameboard)

def winnings (board):
    #check row winnings
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False

def draw(board) :
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True



while not gameOver:
    if swithPlayers(players, player_track):
        if winnings(gameboard):
            print(f"{players[player_track]} has won! Game Over")
            gameOver = True
        if draw(gameboard) :
            print(f"It is a Draw")
            gameOver = True
        player_track = 1 if player_track == 0 else 0
        drawBoard(gameboard)

