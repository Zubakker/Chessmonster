from math import floor

from board import Board

from gui_settings import SCREEN_SIZE, screen_zoom, camera_pos, SQUARE_SIZE


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

def change_player():
    global players_list, current_player_id, players_dict
    global current_player_color, current_player_class

    current_player_id += 1
    if current_plyaer_id >= len(players_list):
        current_players_id = 0
    current_player_color = players_list[ current_player_id ]
    current_player_class = players_dict[ current_player_color ]
    

