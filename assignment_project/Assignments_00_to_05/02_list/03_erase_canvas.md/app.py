import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser on Canvas")

rows, cols = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

def draw_grid():
    """Draw the grid on the screen."""
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col], 
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    """Erase cells by setting them to white."""
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            eraser = pygame.Rect(x, y, ERASER_SIZE, ERASER_SIZE)
            if rect.colliderect(eraser):
                grid[row][col] = WHITE

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pygame.mouse.get_pressed()[0]:  
        mouse_x, mouse_y = pygame.mouse.get_pos()
        erase(mouse_x, mouse_y)
    
    pygame.display.flip()

pygame.quit()
