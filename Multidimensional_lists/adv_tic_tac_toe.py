import random 

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

winning_messages = {
    "X": "Congratulations Player One! You beat the AI!",
    "O": "The AI wins! You lost to random chance."
}

attempts = 0 

while game_over == False:
    
    # Check for a winner
    for combination in winning_combinations:
        first = combination[0]
        second = combination[1]
        third = combination[2]

        if board[first[0]][first[1]] == board[second[0]][second[1]] == board[third[0]][third[1]] and board[first[0]][first[1]] != "":
            winner = board[first[0]][first[1]]
            print(winning_messages[winner])
            game_over = True

    if game_over:
        break
    
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
        print("The AI is thinking")
        spot = random.randint(1, 9)

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
        attempts += 1
        print("Spot already taken")
        print(f"Times attempted to take a clearly taken spot: {attempts}")
    else:
        attempts = 0

        if turn == "Player One":
            board[spot_r][spot_c] = "X"
            turn = "Player Two"
        else:
            board[spot_r][spot_c] = "O"
            print("The AI has made its move")
            turn = "Player One"
