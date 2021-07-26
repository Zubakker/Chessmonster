from piece import Piece

class VanillaKing(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 900
        self.name = 'vanilla:king'
        return


    def return_path(self, relative_movement: list[int]) -> list[list[int]]:
        delta_x, delta_y = relative_movement
        if abs(delta_x) + abs(delta_y) == 0 or abs(delta_x) > 1 or abs(delta_y) > 1:
            return ['Error', 'Invalid target square']

        return ['', relative_movement]


    def validate_path(self, map_path: dict, board_path: dict, attack_path: dict) -> list[list[int]]:
        square = str(list(map_path)[0])
        # map_values = list(map_path.values())
        if 'impassable' in map_path[ square ][0] or \
                        'impassible_imjumpable' in map_path[ square ][0]:
            return ['Error', 'Impassable square in the way']
        
        board_values = list(board_path.values())
        if board_path[ square ] != '':
            target_piece = board_path[ square ][0]
            if target_piece == self.color:
                return ['Error', 'Same color piece on target square']
        for attack in  attack_path[ square ][0]:
            if attack[0] != self.color:
                return ['Error', 'Target square under attack']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        attack_squares = list()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                attack_squares.append( [i, j] )
        return attack_squares


    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int):
        validated_attack = list()
        for square in list(map_path):
            if map_path[ square ][0] not in ['passable', 'imjumpable']:
                continue
            for attack in  attack_path[ square ][0]:
                if attack[0] != self.color:
                    break
            else:
                validated_attack.append( map_path[ square ][1] )
        return validated_attack
