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

        self.isPressed = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def set_pressed(self, flag):
        self.isPressed = flag
    
    def get_colour(self):
        return self.color_press if self.isPressed else self.color_initial
        
