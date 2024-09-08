import time
import pygame

size = 10
sleepInterval = 0.1

# set colors
black_color = (10, 10, 10)
pink_color = (243, 157, 211)
grid_color = (40, 40, 40)

colors = {
    'Red': (255, 174, 174),
    'Pink': (255, 179, 186),
    'Orange': (255, 223, 186),
    'Yellow': (255, 255, 186),
    'Green': (186, 255, 201),
    'Blue': (186, 225, 255),
    'Purple': (234, 184, 255),
}


ALIVE_CELL = 1
DEAD_CELL = 0


# --------------------------------Implement this function--------------------------------
def get_neighbors(mat, col, row):
    neighbors = []
    for k in {row - 1, row, row + 1}:
        for l in {col - 1, col, col + 1}:
            if (k, l) != (row, col) and 0 <= k <= len(mat[0]) and 0 <= l <= len(mat) :
                neighbors.append(mat[k][l])
    return neighbors



def next_generation(current_generation_matrix):
    num_rows = len(current_generation_matrix)
    num_cols = len(current_generation_matrix[0])
    for i in range(num_rows-1):
        for j in range(num_cols-1):
            num_of_neighbors = get_neighbors(current_generation_matrix, j, i).count(1)
            if  current_generation_matrix[i][j] == 1:
                if num_of_neighbors == 1 or num_of_neighbors > 3:
                    current_generation_matrix[i][j] = 0
            elif num_of_neighbors == 3 and current_generation_matrix[i][j] == 0:
                current_generation_matrix[i][j] = 1
    pygame.display.update()
    return current_generation_matrix


# Update screen colors by the recieved matrix. Cell with '0' value will be black, otherwise white.
def fill_colors(matrix, screen, size, alive_color):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 0:
                color = black_color
            else: color = colors[alive_color]
            pygame.draw.rect(screen, color, (j * size, i * size, size - 1, size - 1))
    pygame.display.update()


# Main function
def main(width, height, color):
    # Initial pygame
    pygame.init()
    # Set the screen size
    num_cols, num_rows = width, height
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    screen.fill(grid_color)
    pygame.display.flip()
    pygame.display.update()
    running = False
    # Create zeros matrix
    current_generation_matrix = [[0 for x in range(num_cols)] for y in range(num_rows)]
    fill_colors(current_generation_matrix, screen, size, color)

    while True:
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # If space was pressed, stop/resume the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

            # Mouse is used to active cells
            # If mouse was pressed
            if pygame.mouse.get_pressed()[0]:
                # Get the location of the mouse
                position = pygame.mouse.get_pos()
                # Change the cell of which the mouse pressed value to 1
                current_generation_matrix[position[1] // size][position[0] // size] = 1
                # pygame.draw.rect(screen, alive_color, ((position[0] // size) * size, (position[1] // size) * size, size - 1, size - 1))
                fill_colors(current_generation_matrix, screen, size, color)
                pygame.display.update()

        if running:
            next_generation_matrix = next_generation(current_generation_matrix)
            current_generation_matrix = next_generation_matrix
            fill_colors(current_generation_matrix, screen, size, color)

        # sleep for sleepInterval seconds
        time.sleep(sleepInterval)


