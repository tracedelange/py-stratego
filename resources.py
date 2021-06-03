import pygame

def generate_grid(x,y):
    grid = []
    for row in range(y):
        grid.append([])
        for col in range(x):
            grid[row].append(1)
            
    grid[4][3] = 0
    grid[5][3] = 0
    grid[4][2] = 0
    grid[5][2] = 0
    grid[5][6] = 0
    grid[4][6] = 0
    grid[4][7] = 0
    grid[5][7] = 0

    return grid

def generate_sidebar():
    sidebar_grid = []
    for row in range(9):
        sidebar_grid.append([])
        for col in range(3):
            sidebar_grid[row].append(None)

    return sidebar_grid

unit_sidebar_positions = {
    (0,0) : ("F"),
    (0,1) : ("S"),
    (0,2) : (1),
    (0,3) : (2),
    (1,0) : (3),
    (1,1) : (3),
    (1,2) : (4),
    (1,3) : (4),
    (2,0) : (4),
    (2,1) : (5),
    (2,2) : (5),
    (2,3) : (5),
    (3,0) : (5),

}

print(unit_sidebar_positions[(0,0)])



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = pygame.Color("#01B636")
RED = (255, 0, 0)
BLUE = pygame.Color("#7494ec")
BURGUNDY = '#9f1d35'