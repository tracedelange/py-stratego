# Pygame Template
# Use this to start a new Pygame project
# KidsCanCode 2015
import pygame
import random
import resources


# basic constants to set up your game
WIDTH = 100
HEIGHT = 100

MARGIN = 2

FPS = 30
BGCOLOR = (255,255,255)

# initialize pygame
pygame.init()


# create the game window and set the title

screen = pygame.display.set_mode((1022, 1022))
pygame.display.set_caption("Stratego")


example = "9"

font_size = 80
font = pygame.font.Font('freesansbold.ttf', font_size)
#text = font.render(example, True, resources.GREEN)


text = font.render(example, False, (255, 0, 0))
textRect = text.get_rect()

# start the clock
clock = pygame.time.Clock()

#Generate Grid
grid = resources.generate_grid(10,10)

print(grid)

# set the 'running' variable to False to end the game
running = True
# start the game loop
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)
    # Game loop part 1: Events #####
    for event in pygame.event.get():
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos() # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            #try:
                #grid[row][column] += 1
            #except:
                #continue
            
            #x = ((MARGIN + (WIDTH + WIDTH / 2) * column + MARGIN))
            #y = ((MARGIN + HEIGHT) * row + MARGIN)

            x = (WIDTH/2 + (WIDTH + MARGIN) * column) + font_size/15
            y = (HEIGHT/2 + (HEIGHT + MARGIN) * row) + font_size/15
            
            textRect.center = (x, y)

            print(x, y)
            

            #If you click the margin out of bounds, ignore click
            
            # Set that location to one
            print("Click ", pos, "Grid coordinates: ", row, column)
            print("Grid value: " + str(grid[row][column]))



    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    screen.fill(BGCOLOR)

    
    

    for row in range(10):
        for column in range(10):
            color = resources.WHITE
            if grid[row][column] == 0:
                color = resources.BLUE
            elif grid[row][column] == 1:
                color = resources.GREEN
            pygame.draw.rect(screen,
                color,
                [(MARGIN + WIDTH) * column + MARGIN,
                (MARGIN + HEIGHT) * row + MARGIN,
                WIDTH,
                HEIGHT])

                
    screen.blit(text,textRect)
    # after drawing, flip the display
    pygame.display.flip()

# close the window
pygame.quit()