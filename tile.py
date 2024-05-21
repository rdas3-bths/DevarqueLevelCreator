import pygame

class Tile:

    def __init__(self, x, y, tile_type, grid_row, grid_column):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.row = grid_row
        self.column = grid_column
        self.set_image()
        self.coin_image = pygame.image.load("images/coin.png")
        self.coin_image_size = self.coin_image.get_size()
        self.coin_rect = pygame.Rect(self.x+3, self.y+.5, self.coin_image_size[0], self.coin_image_size[1])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.has_coin = False

    def switch_tile(self):
        self.tile_type += 1
        if self.tile_type >= 2:
            self.tile_type = 0
        self.set_image()

    def set_tile(self, tile_type):
        self.tile_type = tile_type
        self.set_image()

    def set_image(self):
        if self.tile_type == 0:
            self.image = pygame.image.load("images/floor.png")
        elif self.tile_type == 1:
            self.image = pygame.image.load("images/wall.png")
        elif self.tile_type == 2:
            self.image = pygame.image.load("images/start_floor.png")

    def draw_tile(self, screen):
        screen.blit(self.image, self.rect)
        if self.has_coin:
            screen.blit(self.coin_image, self.coin_rect)


