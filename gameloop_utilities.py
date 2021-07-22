from math import floor

from board import Board

import gui_settings as GS
from vanilla_settings import players_dict, players_list, current_player_id, current_player_color, current_player_class 
import vanilla_settings as VS


def get_pressed_square( cursor_coords: list[int], board: Board ) -> list[int]:
    num_of_squares_hor = GS.SCREEN_SIZE[0]// (GS.SQUARE_SIZE * GS.screen_zoom) 
    num_of_squares_ver = GS.SCREEN_SIZE[1]// (GS.SQUARE_SIZE * GS.screen_zoom)

    leftest_square = int(GS.camera_pos[0] + board.center[0] - num_of_squares_hor//2 - 1)
    uppest_square = int(GS.camera_pos[1] + board.center[1] - num_of_squares_ver//2 - 1)

    delta_hor = leftest_square - GS.camera_pos[0] - board.center[0]
    delta_ver = uppest_square - GS.camera_pos[1] - board.center[1]

    nj = (cursor_coords[0] - GS.SCREEN_SIZE[0]//2)/(GS.screen_zoom*GS.SQUARE_SIZE) - delta_hor
    ni = (cursor_coords[1] - GS.SCREEN_SIZE[1]//2)/(GS.screen_zoom*GS.SQUARE_SIZE) - delta_ver

    return [floor(leftest_square + nj + 0), floor(uppest_square + ni + 0)]

def camera_move( mouse_motion_start: tuple[int], mouse_motion_end: tuple[int] ) -> None:
    delta_x = mouse_motion_end[0] - mouse_motion_start[0]
    delta_y = mouse_motion_end[1] - mouse_motion_start[1]

    GS.camera_pos[0] -= (delta_x / GS.SQUARE_SIZE)
    GS.camera_pos[1] -= (delta_y / GS.SQUARE_SIZE)
    return

def camera_zoom( amount: float ) -> None:
    if amount > 0:
        GS.screen_zoom *= amount
    elif amount < 0:
        GS.screen_zoom /= -amount
    return 

def change_player(): #players_list, players_dict, current_player_id, current_player_color, current_player_class):

    VS.current_player_id += 1
    if VS.current_player_id >= len(VS.players_list):
        VS.current_player_id = 0
    VS.current_player_color = VS.players_list[ VS.current_player_id ]
    VS.current_player_class = VS.players_dict[ VS.current_player_color ]
    #return players_list, players_dict, current_player_id, current_player_color, current_player_class

