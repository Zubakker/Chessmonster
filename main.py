import sys
import pygame

from os import system
from time import sleep

from piece import Piece

from gui_settings import SCREEN_SIZE
from vanilla_settings import tmp_texture_pack_directory, VANILLA_PLAYER
from render_utilities import render, render_level_choice, render_texture_pack_choice, \
        render_piece_pack_choice, render_player_pack_coice
from load_utilities import load_scenario, load_map, load_texture_pack, load_piece_pack, \
        load_players_pack
from gameloop_utilities import get_pressed_square, camera_move, change_player


display = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
gamemode = 'game'
    #   types of gamemode:
    #       1)  'game' -- which is the main game loop
    #       2)  'level_choice'
    #       3)  'map_choice'
    #       4)  'texture_pack_choice'
    #       5)  'pieces_pack_choice'

system('rm ' + tmp_texture_pack_directory + '/* -r')

board = Board()
#---- TESTING, NOT FINAL ----
players_dict = load_scenario('./scenarios/vanilla/test1', board)
# load_map('./scenarios/test1.json')
load_texture_pack('./texture_packs/vanilla')
# load_piece_pack('./scenarios/test1.json')
#---- END OF TESTING ----


move_mode = 'initial_square' # left-clicking modes
#   types of move_mode:
#       1) 'initial_square' -- we choose the piece to move
#       2) 'target_square' -- we choose where to move it
#       3) 'locked' -- left-clickng does nothing
initial_move_square = '' # used for moving pieces
target_move_square = '' # used for moving pieces

players_list = list(players_dict)
current_player_id = -1
current_player_color = 0
current_player_class = 0
change_player()

mose_motion_start = 0 # used for camera movement
mose_motion_end = 0 # used for camera movement
whil True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                square_clicked = get_pressed_square( event.pos, board ) 
                if move_mode == 'initial_square':
                    initial_move_square = square_clicked
                    move_mode = 'target_square'
                    print('clicked on initial', initial_move_square)
                    print('it has lighting level', board.lighting[initial_move_square[1]][initial_move_square[0]])
                elif move_mode == 'target_square':
                    target_move_square = square_clicked
                    result = board.move_piece( initial_move_square, target_move_square, current_player_color )
                    print('clicked on target', target_move_square)
                    print(result)
                    player_change()
                    if current_player_class.name == VANILLA_PLAYER
                        move_mode = 'initial_square'
                    else:
                        move_mode = 'locked'

            if event.button == 3:
                mouse_motion_start = event.pos

    if pygame.mouse.get_pressed()[2]:
        mouse_motion_end = pygame.mouse.get_pos()

        camera_move(mouse_motion_start, mouse_motion_end)
        mouse_motion_start = mouse_motion_end
        
    if current_player_class.name != VANILLA_PLAYER
        players_list[ current_player_id ].make_move( board, players_dict, current_player_id )


        

    if gamemode == 'level_choice':
        render_level_choice()
        pass
    if gamemode == 'texture_pack_choice':
        render_texture_pack_choice()
        pass
    if gamemode == 'pieces_pack_choice':
        render_pieces_pack_choice()
        pass
    if gamemode == 'game':
        render(screen, board)

    display.blit(screen, (0,0))
    pygame.display.update()
    #sleep(0.04)
