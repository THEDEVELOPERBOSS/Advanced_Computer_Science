
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

winning_combinations = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

turn = "Player One"
game_over = False

while game_over == False:

    # Check for a winner
    for combination in winning_combinations:
        first = combination[0]
        second = combination[1]
        third = combination[2]

        if board[first[0]][first[1]] == board[second[0]][second[1]] == board[third[0]][third[1]] and board[first[0]][first[1]] != "":
            print(f"{board[first[0]][first[1]]} wins!")
            game_over = True

    # Check for a draw
    if all(position != "" for row in board for position in row):
        print("DRAW")
        game_over = True

    if game_over:
        break

    # Display the board
    print("-------------")
    for row in board:
        print("|", end=" ")
        for position in row:
            print(position, end=" | ")
        print()
        print("-------------")

    if turn == "Player One":
        print("Choose a number (1-9) to place an X:")
        spot = int(input())

    elif turn == "Player Two":
        print("Choose a number (1-9) to place an O:")
        spot = int(input())

    # Convert number-pad selection into coordinates
    if spot == 7:
        spot_r, spot_c = 0, 0
    elif spot == 8:
        spot_r, spot_c = 0, 1
    elif spot == 9:
        spot_r, spot_c = 0, 2
    elif spot == 4:
        spot_r, spot_c = 1, 0
    elif spot == 5:
        spot_r, spot_c = 1, 1
    elif spot == 6:
        spot_r, spot_c = 1, 2
    elif spot == 1:
        spot_r, spot_c = 2, 0
    elif spot == 2:
        spot_r, spot_c = 2, 1
    elif spot == 3:
        spot_r, spot_c = 2, 2
    else:
        print("Invalid selection")
        continue

    # Check whether the position is occupied
    if board[spot_r][spot_c] == "X" or board[spot_r][spot_c] == "O":
        print("Spot already taken")
    else:
        if turn == "Player One":
            board[spot_r][spot_c] = "X"
            turn = "Player Two"
        else:
            board[spot_r][spot_c] = "O"
            turn = "Player One"
