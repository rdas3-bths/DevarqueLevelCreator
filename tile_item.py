import pygame

class TileItem:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        if type == "coin":
            self.image = pygame.image.load("images/coin.png")
        if type == "enemy":
            self.image = pygame.image.load("images/enemy.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.is_active = False