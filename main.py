from asyncio.windows_events import NULL
from sre_parse import WHITESPACE
from time import time
import pygame
from settings import *
import os
import sys
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
KEYHIT_SOUND = pygame.mixer.Sound("Asset/drum-hitnormal.wav")
clock = pygame.time.Clock()

start_tick =0
game_tick = 0

song_data = []
song_data_index = 0
note_popped=0
max_num_of_note= 131
note_list = []
lives=4

click = False

keyBox = Key(WIDTH//2 - KEYBOX_WIDTH//2,475, KEYBOX_WIDTH, KEYBOX_HEIGHT, RED, SHADOW_RED, [pygame.K_LEFT, pygame.K_RIGHT])


def main():
    global start_tick 

    while True:
 
        WIN.fill((255,255,200))
        mouse_x, mouse_y = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(350, 350, 200, 50)
        button_2 = pygame.Rect(350, 500, 200, 50)
        
        
        if button_1.collidepoint((mouse_x, mouse_y)):
            if click:
                start_tick = pygame.time.get_ticks()
                game()
        if button_2.collidepoint((mouse_x, mouse_y)):
            if click:
                help()

        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        pygame.draw.rect(WIN, (255, 0, 0), button_2)
       
        title_text = pygame.font.SysFont('comicsans', 40).render('THE TIGHT GAME', 1, (0,0,0))
        WIN.blit(title_text, (WIDTH/2 - title_text.get_width() /2, HEIGHT/4))
       
        play_text= pygame.font.SysFont('comicsans', 40).render('PLAY', 1, (0,0,0))
        WIN.blit(play_text, (WIDTH/2 - play_text.get_width() /2, 340))
       
        help_text= pygame.font.SysFont('comicsans', 40).render('HELP', 1, (0,0,0))
        WIN.blit(help_text, (WIDTH/2 - help_text.get_width() /2, 490))
       
        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

def help():
    while True:
 
        WIN.fill((255,255,200))
        mouse_x, mouse_y = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(100, 500, 200, 50)        
        
        if button_1.collidepoint((mouse_x, mouse_y)):
            if click:
                main()

        pygame.draw.rect(WIN, (255, 0, 0), button_1)
       
        title_text = pygame.font.SysFont('comicsans', 40).render('HELP', 1, (0,0,0))
        WIN.blit(title_text, (WIDTH/2 - title_text.get_width() /2, HEIGHT/8))
       
        play_text= pygame.font.SysFont('comicsans', 40).render('MENU', 1, (0,0,0))
        WIN.blit(play_text, (200 - play_text.get_width() /2, 490))
       
        line_1_text=" You are a professional bolt tightener."
        line_1 = pygame.font.SysFont('comicsans', 16).render(line_1_text, 1, (0,0,0))
        WIN.blit(line_1, (WIDTH/2 - line_1.get_width() /2, HEIGHT/4))
      
        line_2_text="One day, you enter an amateur bolt tightening competition."
        line_2 = pygame.font.SysFont('comicsans', 16).render(line_2_text, 1, (0,0,0))
        WIN.blit(line_2, (WIDTH/2 - line_2.get_width() /2, (HEIGHT/4)+20))
        
        line_3_text="To hide your identity, you must follow your opponent???s move."
        line_3=pygame.font.SysFont('comicsans', 16).render(line_3_text, 1, (0,0,0))
        WIN.blit(line_3, (WIDTH/2 - line_3.get_width() /2, (HEIGHT/4)+40))

        line_4_text="Do not tighten it too fast nor too slow, make it a tight game "
        line_4=pygame.font.SysFont('comicsans', 16).render(line_4_text, 1, (0,0,0))
        WIN.blit(line_4, (WIDTH/2 - line_4.get_width() /2, (HEIGHT/4)+60))

        line_5_text="press left arrow to turn the bolt clockwise and right to turn the arrow counter-clockwise"
        line_5=pygame.font.SysFont('comicsans', 16).render(line_5_text, 1, (0,0,0))
        WIN.blit(line_5, (WIDTH/2 - line_5.get_width() /2, (HEIGHT/4)+100))

        line_6_text="Song: Rockefeller Street - Nightcore Remix."
        line_6=pygame.font.SysFont('comicsans', 16).render(line_6_text, 1, (0,0,0))
        WIN.blit(line_6, (WIDTH/2 - line_6.get_width() /2, (HEIGHT/4)+140))

  
       
        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()



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
    you_text = pygame.font.SysFont('comicsans', 40).render("you", 1, (0,0,0))
    opp_text = pygame.font.SysFont('comicsans', 40).render("opponent", 1, (0,0,0))

    WIN.blit(draw_text, (0,0))
    WIN.blit(you_text, (275,50))
    WIN.blit(opp_text, (600,50))

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

    text="It is indeed a tight game ;)"
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
        MUSIC_SONG.fadeout(5000)
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

def game():
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
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
                if event.key == pygame.K_LEFT:
                    KEYHIT_SOUND.play()
                    rotation -= handle_collision(pygame.K_LEFT) * 10
                if event.key == pygame.K_RIGHT:
                    KEYHIT_SOUND.play()
                    rotation += handle_collision(pygame.K_RIGHT) * 10
                if event.key in keyBox.key:
                    KEYHIT_SOUND.play()
                    keyBox.set_pressed(True)
            
            if event.type == pygame.KEYUP:
                if event.key in keyBox.key:
                    keyBox.set_pressed(False)
        if check_lives():
            break   
        if check_song():
            break
        update_tick()
        draw_window(rotation, keyBox)
    reset()

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
    global max_num_of_note

    with open(file, "r", encoding='UTF-8') as file:
        song_file_list = file.readlines()
        max_num_of_note = len(song_file_list)

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
        if (note_list[0][0] >= keyBox.getX()-keyBox.getWidth() and note_list[0][0] <= keyBox.getX() + keyBox.getWidth()):
            if (note_list[0][2].getKey() == key):
                note_list.pop(0)
                note_popped+=1
                return 1
    lives-=1
    return 0

def reset():
    global start_tick
    global game_tick
    global song_data 
    global song_data_index 
    global note_popped
    global note_list 
    global lives

    start_tick =0
    game_tick = 0
    song_data = []
    song_data_index = 0
    note_popped=0
    note_list = []
    lives=4

if __name__ == "__main__":
    main()

