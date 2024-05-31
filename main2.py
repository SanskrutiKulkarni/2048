import pygame
import random

from moves import *

pygame.init()

# Set up the window
WIDTH, HEIGHT = 630, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
D_GRAY = (85, 85, 85)
BOX_COLORS = [
    WHITE, (130, 0, 255), (230, 0, 255), (255, 255, 0), (0, 255, 0),
    (0, 130, 130), (0, 25, 255), (255, 150, 0), (0, 255, 255),
    (255, 120, 0), (255, 140, 140), (255, 0, 0), (255, 0, 0)
]

# Define fonts
WORD_FONT = pygame.font.SysFont('comicsans', 300)

# Initialize main grid
grid = [[0] * 4 for _ in range(4)]

# Place two initial tiles with value 2
for _ in range(2):
    x, y = random.randint(0, 3), random.randint(0, 3)
    while grid[x][y] != 0:
        x, y = random.randint(0, 3), random.randint(0, 3)
    grid[x][y] = 2

def draw():
    # Clear the window
    WIN.fill(D_GRAY)
    # Draw the grid
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(WIN, BOX_COLORS[lg(grid[i][j])], (5 + 150 * i, 5 + 150 * j, 145, 145))
            if grid[i][j] != 0:
                output = WORD_FONT.render(str(grid[i][j]), True, BLACK)
                output = pygame.transform.scale(output, (75, 75))
                WIN.blit(output, (40 + 150 * i, 40 + 150 * j))

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Handle arrow key presses
            if event.key == pygame.K_LEFT:
                grid, _ = move_left(grid)
            elif event.key == pygame.K_RIGHT:
                grid, _ = move_right(grid)
            elif event.key == pygame.K_UP:
                grid, _ = move_up(grid)
            elif event.key == pygame.K_DOWN:
                grid, _ = move_down(grid)
            # Place a new tile after each move
            x, y = random.randint(0, 3), random.randint(0, 3)
            while grid[x][y] != 0:
                x, y = random.randint(0, 3), random.randint(0, 3)
            grid[x][y] = 2

    # Draw the updated grid
    draw()
    pygame.display.update()

pygame.quit()
