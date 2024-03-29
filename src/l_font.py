import pygame
import l_settings

pygame.font.init()

font_name_path = '../fonts/TheleahFat.ttf'
font_antialiasing = l_settings.font_antialiasing

def render_text(screen:pygame.Surface,font_size:int,x:int,y:int,text:str,color:tuple): # render text on desired location on the screen
    try:
        initialized_font = pygame.font.SysFont(font_name_path , font_size)
    except:
        raise Exception("Unable to load font.")
    rendered_font = initialized_font.render(text,font_antialiasing,color) # therenderedfont
    screen.blit(rendered_font,(x,y))

def render_text_load_already(screen:pygame.Surface,initialized_font:pygame.font,x:int,y:int,text:str,color:tuple): # (more optimized) render text on desired location on the screen + load already made font
    rendered_font = initialized_font.render(text,font_antialiasing,color) # therenderedfont
    screen.blit(rendered_font,(x,y))

def pquit(): #pquit stands for pygame quit
    pygame.font.quit()