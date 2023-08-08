players = ["X","Y"]
current_player = 0
gameBoard = [
    [' ',' ', ' '],[' ',' ', ' '],[' ',' ', ' ']
]

def drawBoard (board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print('|', end="")
        print("")
        if i < 2:
            print('-' * 5)


drawBoard(gameBoard)