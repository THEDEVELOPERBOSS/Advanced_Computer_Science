board = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
]
turn = "Player One"
game_over = False

def checkWinner():
    global game_over

    # Check horizontal wins
    for row in range(6):
        for col in range(4):
            if (board[row][col] == "X" and board[row][col + 1] == "X" and board[row][col + 2] == "X" and board[row][col + 3] == "X"):
                print("X won!")
                game_over = True
                return
            elif (board[row][col] == "O" and board[row][col + 1] == "O" and board[row][col + 2] == "O" and board[row][col + 3] == "O"):
                print("O won!")
                game_over = True
                return

    # Check vertical wins
    for row in range(3):
        for col in range(7):
            if (board[row][col] == "X" and board[row + 1][col] == "X" and board[row + 2][col] == "X" and board[row + 3][col] == "X"):
                print("X won!")
                game_over = True
                return
            elif (board[row][col] == "O" and board[row + 1][col] == "O" and board[row + 2][col] == "O" and board[row + 3][col] == "O"):
                print("O won!")
                game_over = True
                return

    # Check diagonal wins (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if (board[row][col] == "X" and board[row + 1][col + 1] == "X" and board[row + 2][col + 2] == "X" and board[row + 3][col + 3] == "X"):
                print("X won!")
                game_over = True
                return
            elif (board[row][col] == "O" and board[row + 1][col + 1] == "O" and board[row + 2][col + 2] == "O" and board[row + 3][col + 3] == "O"):
                print("O won!")
                game_over = True
                return

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if (board[row][col] == "X" and board[row - 1][col + 1] == "X" and board[row - 2][col + 2] == "X" and board[row - 3][col + 3] == "X"):
                print("X won!")
                game_over = True
                return
            elif (board[row][col] == "O" and board[row - 1][col + 1] == "O" and board[row - 2][col + 2] == "O" and board[row - 3][col + 3] == "O"):
                print("O won!")
                game_over = True
                return

    # Check for a draw
    if all(position != "" for row in board for position in row):
        print("It's a draw!")
        game_over = True


while game_over == False:

    # Display the board
    print("-------------")
    for row in board:
        print("|", end=" ")
        for position in row:
            print(position, end=" | ")
        print()
        print("-------------")

    if turn == "Player One":
        print("Choose a number (1-7) to place an X:")
    else:
        print("Choose a number (1-7) to place an O:")

    try:
        spot = int(input())
    except ValueError:
        print("Please enter a number!")
        continue

    if spot == 1:
        spot_c = 0
    elif spot == 2:
        spot_c = 1
    elif spot == 3:
        spot_c = 2
    elif spot == 4:
        spot_c = 3
    elif spot == 5:
        spot_c = 4
    elif spot == 6:
        spot_c = 5
    elif spot == 7:
        spot_c = 6
    else:
        print("Invalid selection")
        continue

    # Check whether board position is occupied and find the lowest empty position
    for row in range(5, -1, -1):
        if board[row][spot_c] == "":
            spot_r = row
            break
    else:
        print("Column is full!")
        continue

    if turn == "Player One":
        board[spot_r][spot_c] = "X"
        turn = "Player Two"
    else:
        board[spot_r][spot_c] = "O"
        turn = "Player One"

    # Check whether someone won or the game is a draw
    checkWinner()

# Display final board
print("-------------")
for row in board:
    print("|", end=" ")
    for position in row:
        print(position, end=" | ")
    print()
    print("-------------")