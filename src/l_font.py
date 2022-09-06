from pygame import font

font.init()

font_size = 35
font_name_path = '../fonts/TheleahFat.ttf'
font_antialiasing = True

def render_text(screen,initialized_font,antialiasing,x,y,text,color): # render text on desired location on the screen
    rendered_font = initialized_font.render(text,antialiasing,color) # therenderedfont
    screen.blit(rendered_font,(x,y))

def pquit(): #pquit stands for pygame quit
    font.quit()