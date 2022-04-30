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

KEYBOX_WIDTH = 80
KEYBOX_HEIGHT = 20

clock = pygame.time.Clock()


def draw_window(rotation, keyBox):
    WIN.fill((255,255,200))
    
    pygame.draw.rect(WIN, keyBox.get_colour(), keyBox.rect)
    draw_wrench(rotation)
    pygame.display.update()

def draw_wrench(rotation):
    WRENCH_ROTATED = pygame.transform.rotate(WRENCH_SCALED,rotation)
    RECT_LEFT= WRENCH_ROTATED.get_rect(center = (WRENCH_WIDTH//2,WRENCH_HEIGHT//2))
    RECT_RIGHT= WRENCH_ROTATED.get_rect(center =((WRENCH_WIDTH//2)+WRENCH_WIDTH,(WRENCH_HEIGHT//2)) )

    WIN.blit(WRENCH_ROTATED, RECT_LEFT)
    WIN.blit(WRENCH_ROTATED, RECT_RIGHT)


RED = (255,0,0)
SHADOW_RED = (150,0,0)

def main():
    run = True
    clock = pygame.time.Clock()

    keyBox = Key(WIDTH//2 - KEYBOX_WIDTH//2,500, KEYBOX_WIDTH, KEYBOX_HEIGHT, RED, SHADOW_RED, pygame.K_a)

    rotation=0
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation -= 10
                if event.key == pygame.K_RIGHT:
                    rotation += 10
                if event.key == keyBox.key:
                    keyBox.set_pressed(True)
                    
            if event.type == pygame.KEYUP:
                if event.key == keyBox.key:
                    keyBox.set_pressed(False)
        
        pygame.draw.rect(WIN, keyBox.color_initial, keyBox.rect)

        
        draw_window(rotation, keyBox)

    pygame.quit()



if __name__ == "__main__":
    main()

