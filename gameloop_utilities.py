import pygame

from sys import path as sys_path
from json import loads
from os import listdir, system
from math import floor

from board import Board

from vanilla_settings import tmp_texture_pack_directory, global_piece_dict
from vanilla_settings import texture_error_path
from gui_settings import *

def render(screen, board):
    screen.fill((0,0,0,255))

    num_of_squares_hor = SCREEN_SIZE[0]// (SQUARE_SIZE * screen_zoom) 
    num_of_squares_ver = SCREEN_SIZE[1]// (SQUARE_SIZE * screen_zoom)

    leftest_square = int(camera_pos[0] + board.center[0] - num_of_squares_hor//2 - 1)
    rightest_square = int(camera_pos[0] + board.center[0] + num_of_squares_hor//2 + 2)

    uppest_square = int(camera_pos[1] + board.center[1] - num_of_squares_ver//2 - 1)
    downest_square = int(camera_pos[1] + board.center[1] + num_of_squares_ver//2 + 1)

    delta_hor = leftest_square - camera_pos[0] - board.center[0]
    delta_ver = uppest_square - camera_pos[1] - board.center[1]
    ni = 0

    square_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)).convert_alpha()
    for i in range(uppest_square, downest_square):
        if i < 0 or i >= board.height:
            ni += 1
            continue
        nj = 0
        for j in range(leftest_square, rightest_square):
            if j < 0 or j >= board.width:
                nj += 1
                continue
            map_square = board.map[i][j] + '.png'
            if map_square not in listdir(tmp_texture_pack_directory + '/squares'):
                # TEXTURE NOT FOUND
                print('TEXTURE NOT FOUND', map_square, listdir(tmp_texture_pack_directory + '/squares'))
                texture = pygame.image.load(texture_error_path)
            else:
                texture = pygame.image.load(tmp_texture_pack_directory + '/squares/' + map_square)
            texture = pygame.transform.scale(texture, (SQUARE_SIZE, SQUARE_SIZE))

            screen.blit(texture, 
                    (
                        int(SCREEN_SIZE[0]/2 + (delta_hor+ nj)*SQUARE_SIZE*screen_zoom),
                        int(SCREEN_SIZE[1]/2 + (delta_ver+ ni)*SQUARE_SIZE*screen_zoom)
                    )
            )
            pygame.draw.rect(square_surface, (0,0,0, 255-board.lighting[i][j]), [0, 0, SQUARE_SIZE, SQUARE_SIZE])
            screen.blit(square_surface,
                          ( 
                            int(SCREEN_SIZE[0]/2 + (delta_hor+ nj)*SQUARE_SIZE*screen_zoom),
                            int(SCREEN_SIZE[1]/2 + (delta_ver+ ni)*SQUARE_SIZE*screen_zoom)
                            )
            )
            if board.lighting[i][j] != board.light_stages[-1]:
                if board.board[i][j] != '':
                    piece_square = board.board[i][j].name + '_' + board.board[i][j].color + '.png'
                    if piece_square not in listdir(tmp_texture_pack_directory + '/pieces'):
                        # TEXTURE NOT FOUND
                        print('TEXTURE NOT FOUND', map_square, listdir(tmp_texture_pack_directory + '/squares'))
                        piece_texture = pygame.image.load(texture_error_path)
                    else:
                        piece_texture = pygame.image.load(tmp_texture_pack_directory + '/pieces/' + piece_square)
                    piece_texture = pygame.transform.scale(piece_texture, (SQUARE_SIZE, SQUARE_SIZE))
                    screen.blit(piece_texture, 
                            (
                                int(SCREEN_SIZE[0]/2 + (delta_hor+ nj)*SQUARE_SIZE*screen_zoom),
                                int(SCREEN_SIZE[1]/2 + (delta_ver + ni)*SQUARE_SIZE*screen_zoom)
                            )
                    )

            if board.fog[i][j] == '#':
                fog_texture = pygame.image.load(tmp_texture_pack_directory + '/squares/' + board.fog_texture + '.png')
                fog_texture = pygame.transform.scale(fog_texture, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(fog_texture, 
                        (
                            int(SCREEN_SIZE[0]/2 + (delta_hor+ nj)*SQUARE_SIZE*screen_zoom),
                            int(SCREEN_SIZE[1]/2 + (delta_ver + ni)*SQUARE_SIZE*screen_zoom)
                        )
                )


            nj += 1
        ni += 1
    



    # left of screen center there will be 
    
    pass

def render_level_choice():
    pass

def render_texture_pack_choice():
    pass

def render_piece_pack_choice():
    pass


def get_pressed_square( cursor_coords: list[int], board: Board ) -> list[int]:
    num_of_squares_hor = SCREEN_SIZE[0]// (SQUARE_SIZE * screen_zoom) 
    num_of_squares_ver = SCREEN_SIZE[1]// (SQUARE_SIZE * screen_zoom)

    leftest_square = int(camera_pos[0] + board.center[0] - num_of_squares_hor//2 - 1)
    uppest_square = int(camera_pos[1] + board.center[1] - num_of_squares_ver//2 - 1)

    delta_hor = leftest_square - camera_pos[0] - board.center[0]
    delta_ver = uppest_square - camera_pos[1] - board.center[1]

    nj = (cursor_coords[0] - SCREEN_SIZE[0]//2)/(screen_zoom*SQUARE_SIZE) - delta_hor
    ni = (cursor_coords[1] - SCREEN_SIZE[1]//2)/(screen_zoom*SQUARE_SIZE) - delta_ver
    #print(leftest_square + nj, uppest_square + ni)

    return [floor(leftest_square + nj + 0), floor(uppest_square + ni + 0)]

def camera_move( mouse_motion_start: tuple[int], mouse_motion_end: tuple[int] ) -> None:
    global camera_pos

    delta_x = mouse_motion_end[0] - mouse_motion_start[0]
    delta_y = mouse_motion_end[1] - mouse_motion_start[1]

    camera_pos[0] -= (delta_x / SQUARE_SIZE)
    camera_pos[1] -= (delta_y / SQUARE_SIZE)
    return






def load_scenario( directory: str, board: Board ) -> dict:
    if 'textures' in listdir( directory ):
        load_texture_pack( directory + '/textures' )
    if 'pieces' in listdir( directory ):
        load_piece_pack( directory )
    if 'players' in listdir( directory ):
        load_players_pack( directory )
    return load_map( directory + '/map1.json', board )

def load_map( filename: str, board: Board ) -> dict:
    file = open(filename, 'r').read()
    map_file = loads( file )
    board.set_map( map_file )
    for piece in map_file["pieces"]:
        piece[0], color = piece[0].split('_')
        piece_class = global_piece_dict[piece[0]]
        board.set_piece(piece_class([], color), piece[1])

    players_dict = dict()
    for player_name in list(map_file['players_dict']):
        player_class = global_players_dict[player_name]
        players_dict[player_name] = player_class
    return players_dict

def load_texture_pack( directory: str ) -> None:
    tmp_dir = tmp_texture_pack_directory
    system('mkdir ' + tmp_dir + '/squares')
    system('mkdir ' + tmp_dir + '/pieces')

    for texture_name in listdir( directory + '/squares' ):
        if texture_name not in tmp_dir + '/squares':
            system('cp ' + directory + '/squares/' + texture_name + \
                    ' ' + tmp_dir + '/squares/' + texture_name)
            # (tmp_dir + '/squares').append(texture_name)
        else:
            # CONFLICT !!! CONFLICT !!! CONFLICT !!!
            pass
    for texture_name in listdir( directory + '/pieces' ):
        if texture_name not in tmp_dir + '/pieces':
            system('cp ' + directory + '/pieces/' + texture_name + \
                    ' ' + tmp_dir + '/pieces/' + texture_name)
        else:
            # CONFLICT !!! CONFLICT !!! CONFLICT !!!
            pass
    return

def load_piece_pack( filename: str ) -> None:
    global sys_path, global_piece_dict

    if filename not in sys_path:
        sys_path.append(filename)

    from piece_list import piece_dict
    for key in list(piece_dict):
        if key in list(global_piece_dict):
            # CONFLICT !!! CONFLICT !!! CONFLICT !!!
            pass
        global_piece_dict[key] = piece_dict[key]

    sys_path = sys_path[:-1]
    return

def load_players_pack( filename: str ) -> None:
    global sys_path, global_player_dict

    if filename not in sys_path:
        sys_path.append(filename)

    from players_list import players_dict 
    for key in list():
        if key in list(global_player_dict):
            # CONFLICT !!! CONFLICT !!! CONFLICT !!!
            pass
        global_player_dict[key] = player_dict[key]() # it is an instance not a class
    sys_path = sys_path[:-1]
    return





def change_player():
    global players_list, current_player_id

    current_player_id += 1
    if current_plyaer_id >= len(players_list):
        current_players_id = 0

