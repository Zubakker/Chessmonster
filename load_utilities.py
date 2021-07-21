from sys import path as sys_path
from json import loads
from os import listdir, system

from board import Board

from vanilla_settings import tmp_texture_pack_directory, global_piece_dict, global_player_dict



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
    for player_color in list(map_file['players_dict']):
        player_class_name = map_file['players_dict'][player_color]
        player_class = global_player_dict[player_class_name]
        players_dict[player_color] = player_class
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
