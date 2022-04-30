from sre_parse import WHITESPACE
import pygame
from settings import *
import os
pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tight Game!")
WRENCH_WIDTH=400
WRENCH_HEIGHT=400
WRENCH_IMAGE = pygame.image.load(os.path.join('Asset', 'wrench bolt.png'))
WRENCH_SCALED = pygame.transform.scale(WRENCH_IMAGE,(WRENCH_WIDTH,WRENCH_HEIGHT))
MIDDLE=(WRENCH_WIDTH/2,WRENCH_HEIGHT/2)

clock = pygame.time.Clock()


def draw_window(rotation):
    WIN.fill((255,255,200))
       
    draw_wrench(rotation)
    pygame.display.update()

def draw_wrench(rotation):
    WRENCH_ROTATED = pygame.transform.rotate(WRENCH_SCALED,rotation)
    RECT_LEFT= WRENCH_ROTATED.get_rect(center = (WRENCH_WIDTH/2,WRENCH_HEIGHT/2))
    RECT_RIGHT= WRENCH_ROTATED.get_rect(center =((WRENCH_WIDTH/2)+WRENCH_WIDTH,(WRENCH_HEIGHT/2)) )

    WIN.blit(WRENCH_ROTATED, RECT_LEFT)
    WIN.blit(WRENCH_ROTATED, RECT_RIGHT)


def main():
    run = True
    rotation=0
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pressed= pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]:
            rotation=rotation-10
        if pressed[pygame.K_RIGHT]:
            rotation=rotation+10
        draw_window(rotation)
    pygame.quit()



if __name__ == "__main__":
    main()

