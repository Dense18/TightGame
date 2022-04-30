from sre_parse import WHITESPACE
import pygame
from settings import *
import os
from Key import *
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


RED = (255,0,0)
SHADOW_RED = (150,0,0)

def main():
    run = True
    clock = pygame.time.Clock()

    keyBox = Key(300,300, 80, 20, RED, SHADOW_RED, pygame.K_a)

    rotation=0
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
    
        pressed= pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]:
            rotation=rotation-10
        if pressed[pygame.K_RIGHT]:
            rotation=rotation+10
        draw_window(rotation)
    pygame.quit()



if __name__ == "__main__":
    main()

