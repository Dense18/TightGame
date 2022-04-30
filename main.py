from asyncio.windows_events import NULL
from sre_parse import WHITESPACE
from time import time
import pygame
from settings import *
import os
from Key import *
from Note import *

pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tight Game!")

RED = (255,0,0)
SHADOW_RED = (150,0,0)

WRENCH_WIDTH=400
WRENCH_HEIGHT=400
WRENCH_IMAGE = pygame.image.load(os.path.join('Asset', 'wrench bolt.png'))
WRENCH_SCALED = pygame.transform.scale(WRENCH_IMAGE,(WRENCH_WIDTH,WRENCH_HEIGHT))
MIDDLE=(WRENCH_WIDTH/2,WRENCH_HEIGHT/2)

CLOCKWISE_IMAGE=pygame.image.load(os.path.join('Asset', 'clockwise.png'))
COUNTER_CLOCKWISE_IMAGE=pygame.image.load(os.path.join('Asset', 'counter_clockwise.png'))
COUNTER_CLOCKWISE=pygame.transform.flip(pygame.transform.scale(COUNTER_CLOCKWISE_IMAGE,(50,50)),True,False)
CLOCKWISE = pygame.transform.scale(CLOCKWISE_IMAGE,(50,50))

KEYBOX_WIDTH = 50 
KEYBOX_HEIGHT = 50 

NOTE_WIDTH = 45 
NOTE_HEIGHT = 45 
NOTE_SPEED = 3

MUSIC_SONG = pygame.mixer.Sound("Songs/Rockefeller Street (Nightcore).mp3")
clock = pygame.time.Clock()

start_tick = pygame.time.get_ticks()
game_tick = 0

song_data = []
song_data_index = 0
note_popped=0
max_num_of_note= 131
note_list = []
lives=4
iteration=1

keyBox = Key(WIDTH//2 - KEYBOX_WIDTH//2,475, KEYBOX_WIDTH, KEYBOX_HEIGHT, RED, SHADOW_RED, [pygame.K_LEFT, pygame.K_RIGHT])
def draw_window(rotation, keyBox):
    WIN.fill((255,255,200))
    
    pygame.draw.rect(WIN, keyBox.get_colour(), keyBox.rect)
    draw_wrench(rotation)

    for elem in note_list:
        note = elem[2]
        if (note.getKey() == pygame.K_LEFT):
            WIN.blit(CLOCKWISE, (elem[0], elem[1]))
        else:
            WIN.blit(COUNTER_CLOCKWISE, (elem[0], elem[1]))
    text="lives: "+str(lives)
    draw_text = pygame.font.SysFont('comicsans', 40).render(text, 1, (0,0,0))
    WIN.blit(draw_text, (0,0))
    pygame.display.update()

def draw_wrench(rotation):
    WRENCH_ROTATED = pygame.transform.rotate(WRENCH_SCALED,rotation)
    RECT_LEFT= WRENCH_ROTATED.get_rect(center = (WRENCH_WIDTH//2,WRENCH_HEIGHT//2))
    RECT_RIGHT= WRENCH_ROTATED.get_rect(center =((WRENCH_WIDTH//2)+WRENCH_WIDTH,(WRENCH_HEIGHT//2)) )

    WIN.blit(WRENCH_ROTATED, RECT_LEFT)
    WIN.blit(WRENCH_ROTATED, RECT_RIGHT)

def draw_lose():
    WIN.fill((255,255,200))

    text="it's no longer a tight game :(."
    draw_text = pygame.font.SysFont('comicsans', 28).render(text, 1, (0,0,0))
    
    lives_text="lives: "+str(lives)
    draw_lives_text = pygame.font.SysFont('comicsans', 40).render(lives_text, 1, (0,0,0))
    WIN.blit(draw_lives_text, (0,0))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_win():
    WIN.fill((255,255,200))

    text="you finished at the same time, it is indeed a tight game ;)"
    draw_text = pygame.font.SysFont('comicsans', 28).render(text, 1, (0,0,0))
    
    lives_text="lives: "+str(lives)
    draw_lives_text = pygame.font.SysFont('comicsans', 40).render(lives_text, 1, (0,0,0))
    WIN.blit(draw_lives_text, (0,0))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def check_lives():
    global lives
    if lives<=0:
        draw_lose()
        return 1
def check_song():
    global note_list
    global song_data_index
    global max_num_of_note

    if note_popped==max_num_of_note:
        MUSIC_SONG.fadeout(5000)
        draw_win()
        return 1


def main():
    run = True
    MUSIC_SONG.play()
    clock = pygame.time.Clock()

    #keyBox = Key(WIDTH//2 - KEYBOX_WIDTH//2,475, KEYBOX_WIDTH, KEYBOX_HEIGHT, RED, SHADOW_RED, [pygame.K_LEFT, pygame.K_RIGHT])

    rotation=0
    load_song("Asset/song1.ini")

    while (run):
        clock.tick(FPS)

        update_song()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation -= handle_collision(pygame.K_LEFT) * 10
                if event.key == pygame.K_RIGHT:
                    rotation += handle_collision(pygame.K_RIGHT) * 10
                if event.key in keyBox.key:
                    keyBox.set_pressed(True)
            
            if event.type == pygame.KEYUP:
                if event.key in keyBox.key:
                    keyBox.set_pressed(False)
        if check_lives()  :
            break   
        if  check_song():
            break
        update_tick()
        draw_window(rotation, keyBox)

    pygame.quit()





def update_song():
    global lives
    global song_data_index
    global note_popped

    if (song_data and song_data_index < len(song_data)):
        song = song_data[song_data_index]
        if (game_tick > song[0]):
            if (song[1] == "L"):
                note_list.append([WIDTH,475,Note(NOTE_HEIGHT,NOTE_HEIGHT, pygame.K_LEFT)])
            else:
                note_list.append([WIDTH,475,Note(NOTE_HEIGHT,NOTE_HEIGHT, pygame.K_RIGHT)])
            song_data_index += 1
    
    for note in note_list:
        note[0] -= NOTE_SPEED

    if len(note_list)>0:
        if note_list[0][0] <= keyBox.getX()- keyBox.getWidth():
            note_list.pop(0)
            note_popped+=1
            lives-=1


def load_song(file):
    with open(file, "r", encoding='UTF-8') as file:
        song_file_list = file.readlines()

        for song_file in song_file_list:
            time_slot_format = song_file.split("-")[0].strip()
            time_list = time_slot_format.split(":")
            time_slot = int(time_list[0]) * 60000 + int(time_list[1]) * 1000 + int(time_list[2]) * 10

            note_key = song_file.split("-")[1].strip()

            song_data.append([time_slot,note_key])

def update_tick():
    global game_tick

    game_tick = pygame.time.get_ticks() - start_tick

def handle_collision(key):
    global lives
    global note_popped
    if (len(note_list) > 0):
        print("note x :" + str(note_list[0][0]))
        print("key x left :" + str(keyBox.getX()))
        print("key x right :" + str(keyBox.getY()))
        if (note_list[0][0] >= keyBox.getX()-keyBox.getWidth() and note_list[0][0] <= keyBox.getX() + keyBox.getWidth()):
            print("Hi")
            if (note_list[0][2].getKey() == key):
                note_list.pop(0)
                note_popped+=1
                return 1
    lives-=1
    return 0

    pass
if __name__ == "__main__":
    main()

