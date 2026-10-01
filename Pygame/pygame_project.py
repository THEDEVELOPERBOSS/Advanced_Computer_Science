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
                
                pygame.draw.rect(
                    win, 
                    WHITE,
                    (x, y, CELL_SIZE, CELL_SIZE),
                    1
                )
class Game:
    # controls overall game
    def __init__(self):
        self.board = Board()
        self.current_piece = Tetrimino(make_next_piece()) # randomly selects next piece and puts it into tetrimino
        
        print(self.current_piece.shape)
    def run(self):

        running = True

        while running:

            # Check for player input
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            # Draw the game
            win.fill((0, 0, 0))
            self.board.draw()

            pygame.display.update()

            # Keep the game running at the correct FPS
            timer.tick(fps)

        pygame.quit()
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