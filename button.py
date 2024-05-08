import pygame


class Button:

    def __init__(self, button_type, x, y):
        self.x = x
        self.y = y
        if button_type == "save":
            self.image = pygame.image.load("images/save_button.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


