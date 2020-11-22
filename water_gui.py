import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
BROWN = (143, 87, 75)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def run_game(width, height, grid, current_pos, best_pos):
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(BROWN)

    
    while True:
        drawAstarSearch(width, height, grid, best_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def drawPath(width, height, grid, best_pos):
    '''
    This function draws the best path to the goal point
    '''
    block_width = 400/width #Set the size of the grid block
    block_height = 400/height
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*block_width, y*block_height,
                               block_width, block_height)
            if (grid[y][x] == 1):
                pygame.draw.rect(SCREEN, BLACK, rect)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
    print(best_pos)
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*block_width, y*block_height,
                            block_width, block_height)
            for pos_y, pos_x in best_pos:
                if (pos_x == x and pos_y == y):
                    pygame.draw.rect(SCREEN, BLUE, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    pygame.display.update()
                    pygame.time.wait(500)

def drawAstarSearch(width, height, grid, current_pos):
    '''
    This function shows which grid points are looked at in the AStar search an in what order.
    '''
    
    block_width = 400/width #Set the size of the grid block
    block_height = 400/height
    wave = pygame.image.load('images\wave.jfif')
    wave = pygame.transform.scale(wave, (int(block_width), int(block_height)))
    house = pygame.image.load('images\house.jfif')
    house = pygame.transform.scale(house, (int(block_width), int(block_height)))

    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*block_width, y*block_height,
                               block_width, block_height)
            if (grid[y][x] == 1):
                pygame.draw.rect(SCREEN, BLACK, rect)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*block_width, y*block_height,
                            block_width, block_height)
            for pos_y, pos_x in current_pos:
                if (pos_x == x and pos_y == y):
                    pygame.draw.rect(SCREEN, BLUE, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    SCREEN.blit(wave, (0, 0))
                    SCREEN.blit(house, ((width-1)*block_width, (height-1)*block_height))
                    pygame.display.update()
                    pygame.time.wait(500)
                     
    

                    
            
    