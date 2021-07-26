from piece import Piece

class VanillaRook(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 5
        self.name = 'vanilla:rook'
        return


    def return_path(self, relative_movement: list[int]) -> list[str, list[int]]:
        delta_x, delta_y = relative_movement
        if (delta_x * delta_y != 0) or (abs(delta_x) + abs(delta_y) == 0):
            return ['Error', 'Invalid target square']
        movement_path = ['']
        for i in range( delta_x):
            movement_path.append([i+1, 0])
        for i in range(-delta_x):
            movement_path.append([-i-1, 0])
        for i in range( delta_y):
            movement_path.append([0, i+1])
        for i in range(-delta_y):
            movement_path.append([0, -i-1])
        return movement_path

    def validate_path(self, map_path: dict, board_path: dict, attack_path: dict) -> list[list[int]]:
        for square in list(map_path):
            if map_path[ square ][0] not in ['passable', 'imjumpable']:
                return ['Error', 'Impassable square in the way']
            if board_path[ square ][0] != '' and square != list(map_path)[-1]:
                return ['Error', 'Piece in the way']
        last_square = list(map_path)[-1]
        if board_path[ last_square ][0] != '' and \
                    board_path[ last_square ][0].color == self.color:
            return ['Error', 'Same color piece on target square']
        
        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        attack_squares = list()
        for i in range(1, movement_points+1):
            attack_squares.append( [i, 0] )
            attack_squares.append( [-i, 0] )
            attack_squares.append( [0, i] )
            attack_squares.append( [0, -i] )

        return attack_squares

    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int):
        validated_attack = list()
        for i in range(1, movement_points+1):
            if 'impassable' in map_path[ str([i, 0]) ][0]:
                break
            validated_attack.append( [i, 0] )
            if board_path[ str([i, 0]) ][0] != '':
                break
        for i in range(1, movement_points+1):
            if 'impassable' in map_path[ str([-i, 0]) ][0]:
                break
            validated_attack.append( [-i, 0] )
            if board_path[ str([-i, 0]) ][0] != '':
                break
        for i in range(1, movement_points+1):
            if 'impassable' in map_path[ str([0, i]) ][0]:
                break
            validated_attack.append( [0, i] )
            if board_path[ str([0, i]) ][0] != '':
                break
        for i in range(1, movement_points+1):
            if 'impassable' in map_path[ str([0, -i]) ][0]:
                break
            validated_attack.append( [0, -i] )
            if board_path[ str([0, -i]) ][0] != '':
                break

        return validated_attack


