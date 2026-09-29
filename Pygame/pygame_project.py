import pygame
import random 

pygame.init()

WIDTH, HEIGHT = 600, 600

WHITE = (255, 255, 255)

score = 0 

# setting up display
win = pygame.display.set_mode((WIDTH, HEIGHT))

def make_next_piece():
    next_piece = random() # get next piece


def game_over_screen():
    global score
    win.fill((0, 0, 0))
    game_over_font = pygame.font.SysFont("consolas", 50)
    game_over_text = game_over_font.render(f"Game Over! Score: {score}", True, WHITE)
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2 ))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # replay the game
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()  # quit the game
                    return
                
def main():
    pass
WIDTH = 1000
HEIGHT = 900
pygame.display.set_caption('Welcome to Tetris!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60 

class tetrimino:
    # handles the falling piece
    pass
class Board:
    # makes the board
    pass
class Game:
    pass
