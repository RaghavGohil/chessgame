from ctypes import cast
from shutil import move
from pygame import mixer
import os

import l_settings

mixer.init()

mixer.music.set_volume(l_settings.master_audio_volume)

# music (paths)

start = os.path.join(l_settings.base_path,'../audio/Start.wav')
over = os.path.join(l_settings.base_path,'../audio/Over.wav')
stale_mate = os.path.join(l_settings.base_path,'../audio/StaleMate.wav')
check_mate = os.path.join(l_settings.base_path,'../audio/CheckMate.wav')
move_piece = os.path.join(l_settings.base_path,'../audio/Move.wav')
capture = os.path.join(l_settings.base_path,'../audio/Capture.wav')
castling = os.path.join(l_settings.base_path,'../audio/Castling.wav')
check = os.path.join(l_settings.base_path,'../audio/Check.wav')

audio_playlist = [

    start,
    over,
    stale_mate,
    check_mate,
    move_piece,
    capture,
    castling,
    check

]

def stop_music():
    mixer.music.stop()

def play(i:int,mode:int): # play at index from the playlist (mode specifies if provided audio is music or sound)
    for x in range(len(audio_playlist)):
        if(i == x):
            if(mode == 0):
                play_sound(audio_playlist[x])
            elif(mode == 1):
                play_music(audio_playlist[x])
            else:
                raise Exception("Invalid audio mode.")
            return
    raise Exception("Audio file cannot be played.")

def play_sound(soundpath:str):
    mixer.Sound(soundpath).play()

def play_music(musicpath:str):
    mixer.music.load(musicpath)
    mixer.music.play()

def pquit(): #pquit stands for pygame quit
    mixer.quit()