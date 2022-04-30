import pygame

class Key():
    def __init__(self, x, y, width, height, color_initial, color_press, key):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_initial = color_initial
        self.color_press = color_press
        self.key = key

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)