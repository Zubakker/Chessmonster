from piece import Piece

from vanilla_settings import impassable_squares


class Board:
    def __init__(self):
        pass

# gamemap dictionary format:
#   {
#       name:   "vanilla:map1",
#       size:   [width, height],
#       map:    [                                       
#                   ['vanilla:border', 'vanilla:wall', 'vanilla:wall', 'vanilla:floor_light'],
#                   ['vanilla:floor_light', 'vanilla:floor_dark3', 'vanilla:floor_light', 'vanilla:floor_dark'],
#                   [...],
#                   ...
#               ],
#       visibility_radius:  3,
#       impassable_squares: [
#                               'myblocks:mywall1',
#                               ...
#                           ],
#       camera_pos: [4.5, 3] # < coordinates
#       players_dict: {'white': 'vanilla:player',
#                      'black': 'vanilla:AI',
#                      'red': 'myais:AI'
#                     }
#       ...
#   }
#
#
    def set_map(self, gamemap: dict) -> list:
        global impassable_squares

        self.name = gamemap['name']
        self.width, self.height = gamemap['size']
        self.map = gamemap['map']
        self.board = [ [''] * self.width for x in range(self.height) ]
        # the difference between self.map, self.board are that self.map contains types of squares, e.g. floor or wall, self.board contains pieces (the Piece class) 
        self.fog = [ ['#'] * self.width for x in range(self.height) ]
        self.lighting =  [ [0] * self.width for x in range(self.height) ]
        # self.fog and self.lighting are needed for graphical show off, self.fog contains which squares are seen by the player, '#' means for is there and '' means no fog, self.lighting contains the amount of light in different squares, 0 means not light, squares near player's pieces are more bright
        if gamemap['visibility_radius'] > 10:
            return ['Error', 'Visibility radius too great']
        self.visibility_radius = gamemap['visibility_radius']

        self.light_stages = list()

        if self.visibility_radius < 0:
            self.lighting =  [ [255] * self.width for x in range(self.height) ]
            self.light_stages = [255, 0]

        for i in range(self.visibility_radius + 1):
            self.light_stages.append(255 - i*(255//(self.visibility_radius+1)))

        for item in gamemap['impassable_squares']:
            impassable_squares.append(item)
            
        self.center = gamemap['camera_pos']
        self.fog_texture = gamemap['fog_texture']

        return ['Success', 'Success']

    def set_piece(self, piece: Piece, position_square: list ) -> list: 
        map_square = self.map[ position_square[1] ][ position_square[0] ]
        if map_square in impassable_squares:
            map_square = 'impassable'
        else:
            map_square = 'passable'
        board_square = self.board[ position_square[1] ][ position_square[0] ]
        if piece.validate_placement( map_square, board_square )[0] == 'Error':
            return ['Error', 'Invalid piece placement']
        
        self.board[ position_square[1] ][ position_square[0] ] = piece
        self.calculate_light_board()
        return ['Success', 'Success']


    # moving and capturing enemy pieces
    def move_piece(self, initial_move_square: list, target_move_square: list, 
               current_player: str ) -> list: 
        # both move_squares are absolute coordinates
        # current_player is either 'black' or 'white' (or maybe smth else idk)
        # it returns a list of ['Result', 'Comment'], e.g. ['Error', 'Invalid piece movement']
        current_piece = self.board[ initial_move_square[1] ][ initial_move_square[0] ]
        
        if not current_piece:
            return ['Error', 'No piece in the initial square']
        if current_piece.color != current_player:
            return ['Error', "Trying to move other player's piece"]

        relative_movement = [ target_move_square[0] - initial_move_square[0], 
                              target_move_square[1] - initial_move_square[1] ]
        
        relative_path = current_piece.return_path(relative_movement)
        if relative_path[0] == 'Error':
            print(relative_path)
            return ['Error', 'Invalid target square']
        path_offset = initial_move_square[::]

        map_path = list()
        board_path = list()

        piece_flag = relative_path[0] # some pieces require flags to how to react, e.g. pawn needs no know if it is going diagonally to check for enemy pieces
        board_path.append(piece_flag) 

        for square in relative_path[1:]:
            if self.map[ square[1] + path_offset[1] ][ square[0] + path_offset[0] ] in impassable_squares:
                map_path.append('impassable')
            else:
                map_path.append('passable')
            board_path.append( self.board[ square[1] + path_offset[1] ][ square[0] + path_offset[0] ] )

        movement_validation = current_piece.validate_path(map_path, board_path)
        print(movement_validation)

        if movement_validation[0] == 'Error':
            return ['Error', 'Invalid move']

        if self.board[ target_move_square[1] ][ target_move_square[0] ] != '':
            # CAPTURING PIECE
            pass

        self.board[ initial_move_square[1] ][ initial_move_square[0] ] = ''
        self.set_piece( current_piece, target_move_square )

        #self.board[ target_move_square[1] ][ target_move_square[0] ] = current_piece
        return ['Success', 'Success']

    def calculate_light_board(self) -> None:
        if self.visibility_radius < 0:
            return

        for i in range(self.height):
            for j in range(self.width):
                self.lighting[i][j] = self.light_stages[-1]
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != '':
                    self.calculate_light_piece([j, i])
        return

    def calculate_light_piece(self, position_square) -> None:
        for i in range(-self.visibility_radius, self.visibility_radius+1):
            for j in range(-self.visibility_radius, self.visibility_radius+1):
                if abs(i) + abs(j) > self.visibility_radius:
                    continue

                if position_square[1] + i < 0 or position_square[1] + i >= self.height:
                    continue
                if position_square[0] + j < 0 or position_square[0] + j >= self.width:
                    continue
                self.fog[ position_square[1] + i ][ position_square[0] + j ] = ''
                this_square_light = self.lighting[ position_square[1] + i ][ position_square[0] + j ]
                #this_square_light = 0
                this_square_light = max(this_square_light, self.light_stages[abs(i) + abs(j)])
                self.lighting[ position_square[1] + i ][ position_square[0] + j ] = \
                        this_square_light
        return



