import pygame


class Tile:

    def __init__(self, x, y, tile_type, grid_row, grid_column):
        self.x = x
        self.y = y
        self.row = grid_row
        self.column = grid_column
        if tile_type == 0:
            self.image = pygame.image.load("images/floor.png")
        elif tile_type == 1:
            self.image = pygame.image.load("images/wall.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


