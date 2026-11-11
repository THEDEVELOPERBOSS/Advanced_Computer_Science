import random 


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

winning_messages = {
    "X": "Congratulations Player One! You beat the AI!",
    "O": "The AI wins! You lost to random chance."
}


def checkWinner():
    global game_over

    directions = [
        (0, 1),   # Horizontal
        (1, 0),   # Vertical
        (1, 1),   # Diagonal \
        (1, -1)   # Diagonal /
    ]

    for row in range(6):
        for col in range(7):

            current = board[row][col]

            # Skip empty positions
            if current == "":
                continue

            # Check all four directions
            for row_change, col_change in directions:

                positions = []

                for i in range(4):
                    new_row = row + (row_change * i)
                    new_col = col + (col_change * i)

                    # Make sure position is inside the board
                    if 0 <= new_row < 6 and 0 <= new_col < 7:
                        positions.append(board[new_row][new_col])

                # Check whether all four positions match
                if len(positions) == 4 and all(position == current for position in positions):
                    print(winning_messages[current])
                    game_over = True
                    return

while game_over == False:
    
    checkWinner()
    
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
        print("Choose a number (1-7) to place an X:")
        spot = int(input())
        
    elif turn == "Player Two":
        print("The AI is thinking")
        spot = random.randint(1, 7)
    
    if spot == 1:
        spot_r, spot_c = 5, 0
    elif spot == 2:
        spot_r, spot_c = 5, 1 
    elif spot == 3:
        spot_r, spot_c = 5, 2 
    elif spot == 4:
        spot_r, spot_c = 5, 3
    elif spot == 5:
        spot_r, spot_c = 5, 4
    elif spot == 6:
        spot_r, spot_c = 5, 5 
    elif spot == 7:
        spot_r, spot_c = 5, 6
    else: 
        print("Invalid selection")
        continue
    
    # Check whether board pos is occupied and adds one to column
    column_full = True

    for row in range(5, -1, -1):
        if board[row][spot_c] == "":
            spot_r = row
            column_full = False
            break

    if column_full:
        print("Column is full!")
        continue
    
    if turn == "Player One":
        board[spot_r][spot_c] = "X"
        turn = "Player Two"
    else:
        board[spot_r][spot_c] = "O"
        turn = "Player One"