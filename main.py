import pygame
from settings import *
import os
from Key import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tight Game!")

RED = (255,0,0)
SHADOW_RED = (150,0,0)

def main():
    run = True
    clock = pygame.time.Clock()

    keyBox = Key(300,300, 80, 20, RED, SHADOW_RED, pygame.K_a)

    while (run):
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.draw.rect(WIN, keyBox.color_initial, keyBox.rect)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[keyBox.key]:
            pygame.draw.rect(WIN, keyBox.color_press, keyBox.rect)


        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()

