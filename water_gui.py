import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
BROWN = (143, 87, 75)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def run_game(width, height, grid, current_pos):
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(BROWN)

    
    while True:
        drawGrid(width, height, grid, current_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def drawGrid(width, height, grid, current_pos):
    block_width = 400/width #Set the size of the grid block
    block_height = 400/height
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
            for pos_x, pos_y in current_pos:
                if (pos_x == x and pos_y == y):
                    pygame.draw.rect(SCREEN, BLUE, rect)
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    pygame.display.update()
                    pygame.time.wait(500)

                    
            
    