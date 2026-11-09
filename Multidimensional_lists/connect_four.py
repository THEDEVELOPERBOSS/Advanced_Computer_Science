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

while game_over == False:
    
    # add checks to see if someone won/draw
    
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
        print("Choose a number (1-7) to place an O:")
        spot = int(input())
    
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
    if board[spot_r][spot_c] == "X" or board[spot_r][spot_c] == "O":
        spot_c += 1
        continue
    
    if turn == "Player One":
        board[spot_r][spot_c] = "X"
        turn = "Player Two"
    else:
        board[spot_r][spot_c] = "O"
        turn = "Player One"