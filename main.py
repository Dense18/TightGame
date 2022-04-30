import pygame
from settings import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tight Game!")

def main():
    run = True
    clock = pygame.time.Clock()

    while (run):
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()

