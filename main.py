import pygame
import time

pygame.init()

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

    def create_field(self):
        self.field = [[0 for _ in range(int(self.WIDTH/self.SIZE))] for _ in range(int(self.HEIGHT/self.SIZE))]

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

def get_grid_pos(mouse_pos, size):
    mx, my = mouse_pos
    row = int(my // size)
    col = int(mx // size)

    return row, col

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
                    print(draw_info.field[row][col], draw_info.field[row][col] == 0)
                    if draw_info.field[row][col] == 0: # blank
                        draw_info.field[row][col] = 1
                        print(draw_info.field[row][col])
                    elif draw_info.field[row][col] == 1: # already checked
                        draw_info.field[row][col] = 0
                    

        draw_info.draw_field()


if __name__ == "__main__":
    main()
