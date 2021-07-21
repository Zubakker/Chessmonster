import pygame

from board import Board

from os import listdir, system
from vanilla_settings import tmp_texture_pack_directory, texture_error_path
import gui_settings as GS

def render(screen, board):
    screen.fill((0,0,0,255))

    num_of_squares_hor = GS.SCREEN_SIZE[0]// (GS.SQUARE_SIZE * GS.screen_zoom) 
    num_of_squares_ver = GS.SCREEN_SIZE[1]// (GS.SQUARE_SIZE * GS.screen_zoom)

    leftest_square = int(GS.camera_pos[0] + board.center[0] - num_of_squares_hor//2 - 1)
    rightest_square = int(GS.camera_pos[0] + board.center[0] + num_of_squares_hor//2 + 2)

    uppest_square = int(GS.camera_pos[1] + board.center[1] - num_of_squares_ver//2 - 1)
    downest_square = int(GS.camera_pos[1] + board.center[1] + num_of_squares_ver//2 + 1)

    delta_hor = leftest_square - GS.camera_pos[0] - board.center[0]
    delta_ver = uppest_square - GS.camera_pos[1] - board.center[1]
    ni = 0

    square_surface = pygame.Surface((GS.SQUARE_SIZE, GS.SQUARE_SIZE)).convert_alpha()
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
            texture = pygame.transform.scale(texture, (GS.SQUARE_SIZE, GS.SQUARE_SIZE))

            screen.blit(texture, 
                    (
                        int(GS.SCREEN_SIZE[0]/2 + (delta_hor+ nj)*GS.SQUARE_SIZE*GS.screen_zoom),
                        int(GS.SCREEN_SIZE[1]/2 + (delta_ver+ ni)*GS.SQUARE_SIZE*GS.screen_zoom)
                    )
            )
            pygame.draw.rect(square_surface, (0,0,0, 255-board.lighting[i][j]), [0, 0, GS.SQUARE_SIZE, GS.SQUARE_SIZE])
            screen.blit(square_surface,
                          ( 
                            int(GS.SCREEN_SIZE[0]/2 + (delta_hor+ nj)*GS.SQUARE_SIZE*GS.screen_zoom),
                            int(GS.SCREEN_SIZE[1]/2 + (delta_ver+ ni)*GS.SQUARE_SIZE*GS.screen_zoom)
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
                    piece_texture = pygame.transform.scale(piece_texture, (GS.SQUARE_SIZE, GS.SQUARE_SIZE))
                    screen.blit(piece_texture, 
                            (
                                int(GS.SCREEN_SIZE[0]/2 + (delta_hor+ nj)*GS.SQUARE_SIZE*GS.screen_zoom),
                                int(GS.SCREEN_SIZE[1]/2 + (delta_ver + ni)*GS.SQUARE_SIZE*GS.screen_zoom)
                            )
                    )

            if board.fog[i][j] == '#':
                fog_texture = pygame.image.load(tmp_texture_pack_directory + '/squares/' + board.fog_texture + '.png')
                fog_texture = pygame.transform.scale(fog_texture, (GS.SQUARE_SIZE, GS.SQUARE_SIZE))
                screen.blit(fog_texture, 
                        (
                            int(GS.SCREEN_SIZE[0]/2 + (delta_hor+ nj)*GS.SQUARE_SIZE*GS.screen_zoom),
                            int(GS.SCREEN_SIZE[1]/2 + (delta_ver + ni)*GS.SQUARE_SIZE*GS.screen_zoom)
                        )
                )


            nj += 1
        ni += 1
    
    pass

def render_level_choice():
    pass

def render_texture_pack_choice():
    pass

def render_piece_pack_choice():
    pass

def render_player_pack_choice():
    pass

