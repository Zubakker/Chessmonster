impassable_squares = [
           'vanilla:border',
           'vanilla:border1',
           'vanilla:border2',
           'vanilla:border2',
           'vanilla:border3',
           'vanilla:border4',
           'vanilla:border5',
           'vanilla:border6',
           'vanilla:border7',
           'vanilla:border8',
           'vanilla:border9',

           'vanilla:wall',
           'vanilla:wall1',
           'vanilla:wall2',
           'vanilla:wall3',
           'vanilla:wall4',
           'vanilla:wall5',
           'vanilla:wall6',
           'vanilla:wall7',
           'vanilla:wall8',
           'vanilla:wall9',

        ]


tmp_texture_pack_directory = './tmp_texture_pack'
texture_error_path = './texture_packs/vanilla/squares/vanilla:texture_error.png'


from piece import Piece
from piece_packs.vanilla.vanilla_wazir import VanillaWazir
from piece_packs.vanilla.vanilla_chesspawn import VanillaChessPawn
from piece_packs.vanilla.vanilla_rook import VanillaRook
global_piece_dict = {
            # 'vanilla:pawn': Pawn,
            'vanilla:wazir': VanillaWazir,
            'vanilla:chesspawn': VanillaChessPawn,
            'vanilla:rook': VanillaRook,
        }

from player_packs.vanilla.vanilla_classic_ai import VanillaClassicAI
from player_packs.vanilla.vanilla_player import VanillaPlayer
global_player_dict = {
            'vanilla:classic_ai': VanillaClassicAI,
            'vanilla:player': VanillaPlayer
        }

VANILLA_PLAYER = 'vanilla:player'

players_dict = dict()
players_list = list(players_dict)
current_player_id = -1
current_player_color = 0
current_player_class = 0
