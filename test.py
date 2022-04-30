import pygame

song_data = []

def load_song(file):

    with open(file, "r", encoding='UTF-8') as file:
        song_file_list = file.readlines()

        for song_file in song_file_list:
            time_slot_format = song_file.split("-")[0].strip()
            time_list = time_slot_format.split(":")
            time_slot = int(time_list[0]) * 60000 + int(time_list[1]) * 1000 + int(time_list[2]) * 10

            note_key = song_file.split("-")[1].strip()

            song_data.append([time_slot,note_key])

load_song("Asset/song1.ini")
for elem in song_data:
    print(elem)

