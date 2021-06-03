# Pygame Template
# Use this to start a new Pygame project
# KidsCanCode 2015
import pygame
import random
import resources

#Move screen height over - lets figure this out
#screenWidth = 700
#screenHeight = 700


#TODO adjust text heights to scale with screen size as defined here

#Constants (Keep width and height even numbers)
WIDTH = 80
HEIGHT = 80
MARGIN = 1

#Top left cor, Top right cor, Bot left cor, bot right cor
sidebarDims = [((WIDTH+MARGIN)*10), (((WIDTH+MARGIN)+(int(WIDTH/2)))*10)]

BURGUNDY = pygame.Color("#c39b77")

FPS = 30
BGCOLOR = (255,255,255)


# initialize pygame
pygame.init()


# create the game window and set the title

screen = pygame.display.set_mode((((WIDTH+MARGIN)+(int(WIDTH/2)))*10, ((HEIGHT+MARGIN)*10)))
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
field_grid = resources.generate_grid(10,10)
side_grid = resources.generate_sidebar()

print("Running")

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
            

            x = (WIDTH/2 + (WIDTH + MARGIN) * column) + font_size/15
            y = (HEIGHT/2 + (HEIGHT + MARGIN) * row) + font_size/15
            
            textRect.center = (x, y)

            print(x,y)

            #If you click the margin out of bounds, ignore click
            
            # Set that location to one
            #print("Click ", pos, "Grid coordinates: ", row, column)

            try:

                print("Field Grid value: " + str(field_grid[row][column]))
            except:
                column = column - 10
                #print("Side Grid value: " + str(side_grid[row][column]))
                print(row, column)
                print(resources.unit_sidebar_positions[(row,column)])



    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    screen.fill(BGCOLOR)

    #Draw sidebar
    pygame.draw.rect(screen,
                (BURGUNDY),
                [sidebarDims[0],
                0,
                WIDTH*10,
                (HEIGHT+MARGIN)*10])

    #Draw Field
    for row in range(10):
        for column in range(10):
            color = resources.WHITE
            if field_grid[row][column] == 0:
                color = resources.BLUE
            elif field_grid[row][column] == 1:
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