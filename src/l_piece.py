import pygame
import os

import l_settings
import l_audio
from l_border import Border
from l_board import Board
import l_colors

class Piece:
    def __init__(self,defaultspawnpt:list,base_path:str,piece:str):
        self.position = defaultspawnpt
        self.piece = piece
        if(piece == 'P'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_pawn.png')).convert_alpha()
        elif(piece == 'R'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_rook.png')).convert_alpha()
        elif(piece == 'N'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_knight.png')).convert_alpha()
        elif(piece == 'B'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_bishop.png')).convert_alpha()
        elif(piece == 'Q'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_queen.png')).convert_alpha()
        elif(piece == 'K'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_king.png')).convert_alpha()
        elif(piece == 'p'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_pawn.png')).convert_alpha()
        elif(piece == 'r'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_rook.png')).convert_alpha()
        elif(piece == 'n'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_knight.png')).convert_alpha()
        elif(piece == 'b'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_bishop.png')).convert_alpha()
        elif(piece == 'q'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_queen.png')).convert_alpha()
        elif(piece == 'k'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_king.png')).convert_alpha()

    def display(self,screen):
        self.piece = screen.blit(self.piece_img,self.position)

def initialize_pieces(board:Board): # optimized
    global pieces

    pieces = []

    for x in range(len(board.xblocks)):
        for y in range(len(board.yblocks)):
            if(board.char_board[y+(x*8)] == 'e'):
                continue
            elif(board.char_board[y+(x*8)] == 'P'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'P'))
            elif(board.char_board[y+(x*8)] == 'R'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'R'))
            elif(board.char_board[y+(x*8)] == 'N'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'N'))
            elif(board.char_board[y+(x*8)] == 'B'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'B'))
            elif(board.char_board[y+(x*8)] == 'Q'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'Q'))
            elif(board.char_board[y+(x*8)] == 'K'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'K'))
            elif(board.char_board[y+(x*8)] == 'p'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'p'))
            elif(board.char_board[y+(x*8)] == 'r'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'r'))
            elif(board.char_board[y+(x*8)] == 'n'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'n'))
            elif(board.char_board[y+(x*8)] == 'b'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'b'))
            elif(board.char_board[y+(x*8)] == 'q'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'q'))
            elif(board.char_board[y+(x*8)] == 'k'):
                pieces.append(Piece([y*board.isps,x*board.isps],l_settings.base_path,'k'))

# game variables
piece_is_held = False
pieces_are_moved = False
clear_attached_pieces = False
offsetx,offsety = 0,0
attached_pieces = []
piece_prev_pos = [0,0]
recent_move = [0,0]

def move_piece(events , board:Board , border:Border , mousemotionconst:int , screen): # optimized i guess
    global piece_is_held,offsetx,offsety,attached_pieces,clear_attached_pieces,recent_move,pieces_are_moved
    mousepos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pieces_are_moved:
        pygame.draw.rect(screen,l_colors.clicked_location_box,(piece_prev_pos[0],piece_prev_pos[1],75,75))
    if ((not piece_is_held and pieces_are_moved) and not pressed[0]) and recent_move != piece_prev_pos:
        pygame.draw.rect(screen,l_colors.dropped_location_box,(recent_move[0],recent_move[1],75,75))
    for e in events:
        for p in pieces:
            if((mousepos[0] > p.position[0] and mousepos[0] < (p.position[0]+board.isps)) and (mousepos[1] > p.position[1] and mousepos[1] < (p.position[1]+board.isps))):
                if(pressed[0]):
                    if(len(attached_pieces) != 0):
                        if(p not in attached_pieces):
                            attached_pieces.append(p)
                    else:
                        attached_pieces.append(p)
                    for piece in attached_pieces:
                        if(piece != attached_pieces[0]):
                            if(piece.position[0] == border.position[0] and piece.position[1] == border.position[1]):
                                pass
                            else:
                                clear_attached_pieces = True

                    if clear_attached_pieces and len(attached_pieces) != 0:
                        attached_pieces = [attached_pieces[0]]
                        clear_attached_pieces = False

                if pressed[0] and not piece_is_held:
                    piece_is_held = True
                    offsetx = (mousepos[0]-attached_pieces[0].position[0]) # set mouse offset for holding the piece
                    offsety = (mousepos[1]-attached_pieces[0].position[1])
                    piece_prev_pos[0] = attached_pieces[0].position[0]
                    piece_prev_pos[1] = attached_pieces[0].position[1]
                if not pressed[0] and piece_is_held:      
                        piece_is_held = False
                        if len(attached_pieces) < 2: # check if there are extra pieces attached / there is a piece on desired landing location
                            attached_pieces[0].position[0] = border.position[0]
                            attached_pieces[0].position[1] = border.position[1] # works lmao
                            recent_move[0] = border.position[0]
                            recent_move[1] = border.position[1]
                            pieces_are_moved = True
                        else:
                            attached_pieces[0].position[0] = piece_prev_pos[0]
                            attached_pieces[0].position[1] = piece_prev_pos[1] # prevpos
                        if(attached_pieces[0].position[0] != piece_prev_pos[0] or attached_pieces[0].position[1] != piece_prev_pos[1]): # play audio only when moved
                            l_audio.play(4,0)
                        attached_pieces = []
                        offsetx,offsety = 0,0
        if e.type == mousemotionconst and piece_is_held:
            attached_pieces[0].position[0] = mousepos[0]-offsetx
            attached_pieces[0].position[1] = mousepos[1]-offsety

def display_pieces(screen:pygame.Surface):
    for x in pieces:
        x.display(screen)