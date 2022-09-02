import pygame
import os

class Border:
    def __init__(self,base_path):
        self.border= pygame.image.load(os.path.join(base_path, "../images/Border.png"))
        self.position = [0,0]

    def display(self,screen,board):
        mousepos = pygame.mouse.get_pos()
        if (mousepos[1] < board.size[1] and mousepos[1] > 0) and (mousepos[0] < board.size[0] and mousepos[0] > 0):
            for x in range(len(board.yblocks)):
                for y in range(len(board.yblocks)):
                    if(mousepos[0] > x*board.isps):
                        self.position[0] = x*board.isps
                    if(mousepos[1] > y*board.isps):
                        self.position[1] = y*board.isps
                    
        screen.blit(self.border,self.position)