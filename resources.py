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



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)