import sys
import pygame

from os import system
from time import sleep

from piece import Piece

from gui_settings import SCREEN_SIZE
from vanilla_settings import tmp_texture_pack_directory, VANILLA_PLAYER
from render_utilities import render_game, render_level_choice, render_texture_pack_choice, \
        render_piece_pack_choice, render_player_pack_choice
from load_utilities import load_scenario, load_map, load_texture_pack, load_piece_pack, \
        load_players_pack
from gameloop_utilities import get_pressed_square, camera_move, camera_zoom, change_player

import vanilla_settings as VS

from board import Board


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
#players_dict = load_scenario('./scenarios/vanilla/test1', board)
load_texture_pack('./texture_packs/vanilla')
#load_piece_pack('./piece_packs/vanilla')
#load_player_pack'./player_packs/vanilla')
VS.players_dict = load_map('./scenarios/vanilla/test1/chess.json', board)
#---- END OF TESTING ----


move_mode = 'initial_square' # left-clicking modes
#   types of move_mode:
#       1) 'initial_square' -- we choose the piece to move
#       2) 'target_square' -- we choose where to move it
#       3) 'locked' -- left-clickng does nothing
initial_move_square = '' # used for moving pieces
target_move_square = '' # used for moving pieces

VS.players_list = list(VS.players_dict)
#players_list, players_dict, current_player_id, current_player_color, current_player_class = change_player(players_list, players_dict, current_player_id, current_player_color, current_player_class)
change_player()

mouse_motion_start = 0 # used for camera movement
mouse_motion_end = 0 # used for camera movement
piece_dragged = ''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if VS.current_player_class.name != VANILLA_PLAYER:
                    continue
                square_clicked = get_pressed_square( event.pos, board ) 
                square_check = board.check_for_piece( square_clicked )
                if square_check['result'] == 'Piece on square' and \
                        square_check['color'] == VS.current_player_color:
                    origin_move_square = square_clicked
                    piece_dragged = board.get_piece( square_clicked )
                    board.remove_piece( origin_move_square )
                else:
                    origin_move_square = ''
                    piece_dragged = ''


                '''
                if move_mode == 'initial_square':
                    initial_move_square = square_clicked
                    move_mode = 'target_square'
                    print('clicked on initial', initial_move_square)
                elif move_mode == 'target_square':
                    target_move_square = square_clicked
                    result = board.move_piece( initial_move_square, \
                                     target_move_square, VS.current_player_color )
                    print('clicked on target', target_move_square)
                    if result[0] == 'Success':
                        #players_list, players_dict, current_player_id, current_player_color, current_player_class = change_player(players_list, players_dict, current_player_id, current_player_color, current_player_class)
                        change_player()
                    if VS.current_player_class.name == VANILLA_PLAYER:
                        move_mode = 'initial_square'
                    else:
                        move_mode = 'locked'
                        '''

            if event.button == 3:
                mouse_motion_start = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if VS.current_player_class.name != VANILLA_PLAYER:
                    continue
                square_clicked = get_pressed_square( event.pos, board ) 
                target_move_square = square_clicked
                if piece_dragged != '':
                    print(piece_dragged)
                    set_result = board.set_piece( piece_dragged, origin_move_square )
                    if set_result[0] == 'Error':
                        piece_dragged = ''
                        origin_move_square = ''
                        continue
                    move_result = board.move_piece( origin_move_square, \
                                        target_move_square, VS.current_player_color)
                    if move_result[0] == 'Success':
                        piece_dragged = ''
                        origin_move_square = ''
                        change_player()
                    else:
                        piece_dragged = ''
                        origin_move_square = ''



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                camera_zoom(1.3)
            if event.key == pygame.K_DOWN:
                camera_zoom(-1.3)

    if pygame.mouse.get_pressed()[2]:
        mouse_motion_end = pygame.mouse.get_pos()

        camera_move(mouse_motion_start, mouse_motion_end)
        mouse_motion_start = mouse_motion_end
        
    if VS.current_player_class.name != VANILLA_PLAYER:
        current_player_class.make_move( board, VS.players_dict, VS.current_player_id )


        

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
        render_game(screen, board, piece_dragged, pygame.mouse.get_pos())

    display.blit(screen, (0,0))
    pygame.display.update()
    #sleep(0.04)
