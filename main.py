import pygame
import time

pygame.init()

def get_neighbors(row, col, rows, cols):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < cols - 1:
        neighbors.append((row, col + 1))

    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))
    if row < rows - 1 and col < cols-1:
        neighbors.append((row + 1, col + 1))
    if row < rows - 1 and col > 0:
        neighbors.append((row + 1, col - 1))
    if row > 0 and col < cols - 1:
        neighbors.append((row - 1, col + 1))

    return neighbors

def get_grid_pos(mouse_pos, size):
    mx, my = mouse_pos
    row = int(my // size)
    col = int(mx // size)

    return row, col

def copy_matrixes(m1, m2):
    '''
    copies the contents of m1 onto m2
    '''
    for i, row in enumerate(m1):
            for j, value in enumerate(row):
                m2[i][j] = value

class DrawInfo:
    BG_COLOR = "white"

    GREY = (100, 100, 100)
    LIGHT_GREY = (140, 140, 140)
    WIDTH = 1000
    HEIGHT = 800
    SIZE = 20
    CLICKED_COLOR = (220, 180, 125)

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("John Conway's Game of Life")
        self.rows = int(self.HEIGHT/self.SIZE)
        self.cols = int(self.WIDTH/self.SIZE)

    def create_field(self):
        self.field = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw_field(self):
        self.window.fill(self.BG_COLOR)

        for i, row in enumerate(self.field):
            y = self.SIZE * i
            for j, value in enumerate(row):
                x = self.SIZE * j
                
                if value == 0:
                    pygame.draw.rect(self.window, self.GREY, (x, y, self.SIZE, self.SIZE))
                    pygame.draw.rect(self.window, self.LIGHT_GREY, (x, y, self.SIZE, self.SIZE), 1)
                elif value == 1:
                    pygame.draw.rect(self.window, self.CLICKED_COLOR, (x, y, self.SIZE, self.SIZE))
                    pygame.draw.rect(self.window, self.LIGHT_GREY, (x, y, self.SIZE, self.SIZE), 1)
        pygame.display.update()

    def iterate_field(self):
        temp_field = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        copy_matrixes(self.field, temp_field)
        
        for i, row in enumerate(self.field):
            for j, value in enumerate(row):
                num_of_neighbors = self.neighbor_count(i,j)
                if num_of_neighbors < 2 or num_of_neighbors > 3:
                    temp_field[i][j] = 0
                if temp_field[i][j] == 0 and num_of_neighbors == 3:
                    # print("true")
                    temp_field[i][j] = 1
                
        copy_matrixes(temp_field, self.field)

    def neighbor_count(self, row, col):
        neighbors = get_neighbors(row, col, self.rows, self.cols)
        neighbor_count = 0

        for neighbor in neighbors:
            neighborrow, neighborcol = neighbor
            if self.field[neighborrow][neighborcol] == 1:
                neighbor_count += 1
        
        return neighbor_count

                
def main():
    run = True
    # clock = pygame.time.Clock() will be useful later for auto generation
    draw_info = DrawInfo()
    draw_info.create_field()

    while run:
        # clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:

                row, col = get_grid_pos(pygame.mouse.get_pos(), draw_info.SIZE)
                mouse_button_pressed = pygame.mouse.get_pressed()

                if mouse_button_pressed[0]: #left click

                    neighbors = get_neighbors(row, col, draw_info.rows, draw_info.cols)
                    neighbor_count = 0
                    for neighbor in neighbors:
                        neighborrow, neighborcol = neighbor
                        if draw_info.field[neighborrow][neighborcol] == 1:
                            neighbor_count += 1
                    print(neighbor_count)

                    if draw_info.field[row][col] == 0: # blank
                        draw_info.field[row][col] = 1
                    elif draw_info.field[row][col] == 1: # already checked
                        draw_info.field[row][col] = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_info.iterate_field()

        draw_info.draw_field()


if __name__ == "__main__":
    main()
