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


    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        if 'impassable' in map_path or 'impassible_imjumpable' in map_path:
            return ['Error', 'Impassable square in the way']

        if board_path[1] != '':
            target_piece = board_path[1]
            if target_piece.color == self.color:
                return ['Error', 'Same color piece on target square']

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
            if map_path[ square ][0] in ['passable', 'imjumpable'] and \
                        attack_path[ square ][0] == list():
                validated_attack.append( map_path[ square ][1] )
        return validated_attack
