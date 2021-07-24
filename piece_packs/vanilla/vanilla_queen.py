from piece import Piece

class VanillaQueen(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 9 
        self.name = 'vanilla:queen'
        return


    def return_path(self, relative_movement: list[int]) -> list[str, list[int]]:
        delta_x, delta_y = relative_movement
        if abs(delta_x) + abs(delta_y) == 0:
            return ['Error', 'Invalid target square']
        if abs(delta_x) != abs(delta_y) and delta_x * delta_y != 0:
            return ['Error', 'Invalid target square']
        movement_path = ['']
        if delta_x * delta_y == 0:
            for i in range( delta_x):
                movement_path.append([i+1, 0])
            for i in range(-delta_x):
                movement_path.append([-i-1, 0])
            for i in range( delta_y):
                movement_path.append([0, i+1])
            for i in range(-delta_y):
                movement_path.append([0, -i-1])
        else:
            y_sign = delta_y // abs(delta_y)
            for i in range( delta_x):
                movement_path.append([i+1, (i+1)*y_sign])
            for i in range(-delta_x):
                movement_path.append([-i-1, (i+1)*y_sign])
        return movement_path

    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        if 'impassable' in map_path or 'impassible_imjumpable' in map_path:
            return ['Error', 'Impassable square in the way']
        for square in board_path[:-1]:
            if square != '':
                return ['Error', 'Piece in the way']
        if board_path[-1] != '' and board_path[-1].color == self.color:
            return ['Error', 'Same color piece on target square']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        return ['Success', 'Succsess']


    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        attack_squares = list()
        for i in range(1, movement_points+1):
            attack_sqaures.append( [i, 0] )
            attack_sqaures.append( [-i, 0] )
            attack_sqaures.append( [0, -i] )
            attack_sqaures.append( [0, i] )

            attack_sqaures.append( [i, i] )
            attack_sqaures.append( [i, -i] )
            attack_sqaures.append( [-i, -i] )
            attack_sqaures.append( [-i, i] )

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
        for i in range(1, movement_points + 1):
            if 'impassable' in map_path[ str([i, i]) ][0]:
                break
            validated_attack.append( [i, i] ) 
            if board_path[ str([i, i]) ][0] != '':
                break
        for i in range(1, movement_points + 1):
            if 'impassable' in map_path[ str([-i, -i]) ][0]:
                break
            validated_attack.append( [-i, -i] ) 
            if board_path[ str([-i, -i]) ][0] != '':
                break
        for i in range(1, movement_points + 1):
            if 'impassable' in map_path[ str([i, -i]) ][0]:
                break
            validated_attack.append( [i, -i] ) 
            if board_path[ str([i, -i]) ][0] != '':
                break
        for i in range(1, movement_points + 1):
            if 'impassable' in map_path[ str([-i, i]) ][0]:
                break
            validated_attack.append( [-i, i] ) 
            if board_path[ str([-i, i]) ][0] != '':
                break

        return validated_attack

