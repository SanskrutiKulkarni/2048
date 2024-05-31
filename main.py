import pygame
import random

from moves import* # imports
# from expectimax import*
from minimax import*
pygame.init() # initialize the game module

WIDTH, HEIGHT = 630,630
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # window object , used in draw
BLACK = (0,0,0)
WHITE=(255, 255, 255)
GRAY = (170,170,170)
D_GRAY = (85,85,85)

PURPLE = (130,0,255)
PINK = (230,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
L_BLUE = (0,130,130)
D_BLUE = (0,25,255)
ORANGE = (255,150,0)
SKY_BLUE = (0,255,255)
D_ORANGE = (255,120,0)
L_RED = (255,140,140)
RED = (255,0,0)



box_color = [WHITE, PURPLE, PINK, YELLOW, GREEN, L_BLUE, D_BLUE, ORANGE, SKY_BLUE, D_ORANGE, L_RED, RED, RED]
# color tuple

WORD_FONT = pygame.font.SysFont('comicsans', 300)

pygame.display.set_caption("2048")


run = True


#initialize main grid
grid = {} # dictionary
for i in range(4):
    grid[i] = [] # list , inside the dictionary
    for j in range(4):
        grid[i].append(0) # initialised all with zero



#create 2 random 2s

temporary_x = random.randint(0,3) # generates an index
temporary_y = random.randint(0,3) # index generated
grid[temporary_x][temporary_y]=2 # we place 2
while(grid[temporary_x][temporary_y]==2):  # till the time you find empty cell
    temporary_x = random.randint(0,3)
    temporary_y = random.randint(0,3)
grid[temporary_x][temporary_y]=2 # empty found place 2





def draw(): # displaying the rectangles
    for i in range(4):
        for j in range(4): # lg is used to map index of grid with box_color index
            pygame.draw.rect(WIN, box_color[lg(grid[i][j])], (5+150*i,5+150*j, 145, 145)) # (x , y , width , height) px
            output = WORD_FONT.render(f"{grid[i][j]}", 100, BLACK)
            output = pygame.transform.scale(output, (75,75)) # we scale the output
            WIN.blit(output, (40+150*i,40+150*j)) # blit is used to place one surface on the other
            if(grid[i][j]==0): # empty cell , we give the color assigned for empty cell
                pygame.draw.rect(WIN, box_color[lg(grid[i][j])], (5+150*i,5+150*j, 145, 145))






while run:
 # while true
    execute = False
    ok = False
    #time delay
    pygame.time.delay(1000)


    for event in pygame.event.get(): # events queue se items li hai -> mouse movements, keyboard presses, or window events.
        if (event.type==pygame.QUIT): run = False # terminates loop
    #type is the attribute

    newMove = findBestMovePlayer(grid)
    #print(newMove)
    if(newMove == "left"):
        grid, ok = move_left(grid)
    if(newMove == "right"):
        grid, ok = move_right(grid)
    if(newMove == "up"):
        grid, ok = move_up(grid)
    if(newMove == "down"):
        grid, ok = move_down(grid)

    WIN.fill(D_GRAY) # window clear karke we redraw the grid
    draw()
    pygame.display.update() # update the content of the grid
    pygame.time.delay(0)


    if(ok==False):continue
    # if move is successfully then next randomly generated tiles are introduced
    temporary_x = random.randint(0,3)
    temporary_y = random.randint(0,3)
  # its redundant
    Full = True
    for i in range(4):
        for j in range(4):
            if(grid[i][j] == 0): Full = False # empty
    if(Full==False):
        while(grid[temporary_x][temporary_y]!=0): # until we do not find an empty tile , once we find it we break
            temporary_x = random.randint(0,3)
            temporary_y = random.randint(0,3)

        that = 2 # initialise with 2 , dafault
        l = random.randint(1,10) # generate random integer , agar 10 aagya to 100% prob to palce 4
        if(l==10):that = 4 #
        grid[temporary_x][temporary_y] = that







    WIN.fill(D_GRAY)
    draw()
    pygame.display.update()







pygame.quit()