import pygame
import random 

pygame.init()

# settings
WIDTH, HEIGHT = 1000, 900 # game window size 

WHITE = (255, 255, 255)
CYAN = (0, 255, 255) # color of tetris pieces 

score = 0 

# pieces
PIECES = [
    "I",
    "O",
    "T",
    "S",
    "Z",
    "J", 
    "L"
]
SHAPES = { # the shape that will show up on the board 
        "I": [
        [1, 1, 1, 1]
    ],

    "O": [
        [1, 1],
        [1, 1]
    ],

    "T": [
        [0, 1, 0],
        [1, 1, 1]
    ],

    "S": [
        [0, 1, 1],
        [1, 1, 0]
    ],

    "Z": [
        [1, 1, 0],
        [0, 1, 1]
    ],

    "J": [
        [1, 0, 0],
        [1, 1, 1]
    ],

    "L": [
        [0, 0, 1],
        [1, 1, 1]
    ]
}
# Board sizes
ROWS = 20
COLUMNS = 10 
CELL_SIZE = 30
# pygame setup 

# setting up actual game window 
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Welcome to Tetris!') 
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60 
FALL_SPEED = 30 # controls how quickly the piece fall
class Tetrimino:
    # handles the falling pieces
    
    def __init__(self, shape):
        self.shape = SHAPES[shape] # stores the Tetris piece this object represents
        self.x = 3 # starting column 
        self.y = 0 # starting row    
    def draw(self):
        for row in range(len(self.shape)): # Ex:T would return 2 here since there are 2 rows init. Loops through each row of the piece
            for column in range(len(self.shape[row])): # loops through each cell in the current row 
                
                if self.shape[row][column] == 1: # only draws cells that contain a block 
                    x = (self.x + column) * CELL_SIZE # converts the piece's screen postion into the screen coordinates
                    y = (self.y + row) * CELL_SIZE
                    
                    pygame.draw.rect( # draws the tetris block 
                        win, 
                        CYAN, 
                        (x,y, CELL_SIZE, CELL_SIZE)
                    )
    def move_left(self):
        if self.x > 0:
            self.x -= 1 # moves the piece one column left
    
    def move_right(self):
        # prevents the piece from moving outside the board 
        if self.x + len(self.shape[0]) < COLUMNS:
            self.x += 1 # moves the piece one column right
    
    def move_down(self):
        self.y += 1 # moves the peice down one row
class Board:
    # manages the board
    
    def __init__(self):
        self.grid = [
            [0 for _ in range(COLUMNS)]
            for _ in range(ROWS)
        ]
    def draw(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                x = column * CELL_SIZE # converts grid cordinates into screen cordinates
                y = row * CELL_SIZE
                
                # draws blocks that have been locked into the board
                if self.grid[row][column] == 1:
                    pygame.draw.rect(
                        win, 
                        CYAN, 
                        (x, y, CELL_SIZE, CELL_SIZE)
                    )
                pygame.draw.rect(
                    win, 
                    WHITE,
                    (x, y, CELL_SIZE, CELL_SIZE),
                    1
                )
    def check_collision(self, piece):
        for row in range(len(piece.shape)): # loops through each row of the piece
            for column in range(len(piece.shape[row])): # loops through each cell in the current row

                if piece.shape[row][column] == 1: # only checks cells that contain a block

                    board_row = piece.y + row # finds the block's row on the board
                    board_column = piece.x + column # finds the block's column on the board

                    # checks if the piece reaches the bottom
                    if board_row >= ROWS:
                        return True

                    # checks if the piece hits another locked block
                    if self.grid[board_row][board_column] == 1:
                        return True

        return False # no collision was found
    def lock_piece(self, piece):
        # adds the piece's blocks to the board
        for row in range(len(piece.shape)): # loops through each row of the piece
            for column in range(len(piece.shape[row])): # loops through each cell in the current row
                # only stores cells that contain a block
                if piece.shape[row][column] == 1:
                    board_row = piece.y + row 
                    board_column = piece.x + column 
                    
                    self.grid[board_row][board_column] = 1 # stores the block on the board
    def clear_lines(self):
        # finds rows that are completely filled
        completed_rows = []
        
        for row in range(ROWS): # stores the rows that are completely filled
            if all(self.grid[row]): # checks every row on the board
                completed_rows.append(row) # checks if every cell in the row is filled 
        
        # removes the completed rows 
        for row in completed_rows:
            del self.grid[row]
            
        # adds an empty row for every row that was removed 
        for _ in completed_rows:
            self.grid.insert(0, [0 for _ in range(COLUMNS)])
                
        return len(completed_rows) # returns how many lines were cleared 
class Game:
    # controls overall game
    def __init__(self):
        self.board = Board()
        self.current_piece = Tetrimino(make_next_piece()) # randomly selects next piece and puts it into tetrimino
        
        self.fall_timer = 0 # tracks when the piece should move down
        self.score = 0 # keeps track of the players score
    def run(self):

        running = True

        while running:

            # Check for player input
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN: # checks if a key was pressed
                    
                    if event.key == pygame.K_LEFT: # moves piece left
                        self.current_piece.move_left()
                        
                    elif event.key == pygame.K_RIGHT: # moves piece right
                        self.current_piece.move_right()
                        
            self.fall_timer += 1 
            # checks if enough time has passed for the piece to fall
            if self.fall_timer >= FALL_SPEED:

                self.current_piece.move_down() # tries to move the piece down

                if self.board.check_collision(self.current_piece): # step 9.3 
                    self.current_piece.y -= 1 # moves the piece back if it hits the button 

                    self.board.lock_piece(self.current_piece) # saves the piece to the board

                    lines_cleared = self.board.clear_lines() # removes completed rows

                    self.score += lines_cleared * 100 # gives 100 points for each line cleared

                    self.current_piece = Tetrimino(make_next_piece()) # creates a new piece
                    
                self.fall_timer = 0 # resets the fall timer
            # Draw the game
            win.fill((0, 0, 0))
            
            self.board.draw()
            self.current_piece.draw() # tells the piece to draw itself 
            self.draw_score() # displays the player's score
            
            pygame.display.update()

            # Keep the game running at the correct FPS
            timer.tick(fps)
            pygame.quit()
    def draw_score(self):
        # displays the current score
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        
        win.blit(score_text, (650, 50))
def make_next_piece():
    next_piece = random.choice(PIECES) # get next piece randomly 
    return next_piece

def game_over_screen():
    global score
    win.fill((0, 0, 0)) # clears the entire window with black
    game_over_font = pygame.font.SysFont("consolas", 50)
    game_over_text = game_over_font.render(f"Game Over! Score: {score}", True, WHITE)
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2 )) # centers the game over text 
    pygame.display.update() # makes things drawn visible
    while True:
        for event in pygame.event.get(): # waits for the player to restart or quit
            if event.type == pygame.QUIT: # closes game if window is closed 
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # checks to see if r is pressed to restart
                    main()  # replay the game
                    return
                elif event.key == pygame.K_q: # quits the game when Q is pressed 
                    pygame.quit()  # quit the game
                    return
                
def main():
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()