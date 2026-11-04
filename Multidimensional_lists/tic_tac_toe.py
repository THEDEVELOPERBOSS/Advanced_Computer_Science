board = [
    ["|", "|", "|"],
    ["|", "|", "|"],
    ["|", "|", "|"]
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
x_win = [
    ["|", "|", "|"],
    ["|", "|", "|"],
    ["|", "|", "|"]
]
y_win = [
    ["|", "|", "|"],
    ["|", "|", "|"],
    ["|", "|", "|"]
]
while True:
    for combination in winning_combinations:
        first = combination[0] # First coordinate
        second = combination[1] # Second coordinate
        third = combination[2] # Third Coordinate
        
        if board[first[0]][first[1]] == board[second[0]][second[1]] == board[third[0]][third[1]] and board[first[0]][first[1]] != "|":