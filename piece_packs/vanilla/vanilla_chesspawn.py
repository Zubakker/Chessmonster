from piece import Piece

class VanillaChessPawn(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 1
        self.name = 'vanilla:chesspawn'
        self.moved_flag = False
        return


    def return_path(self, relative_movement: list[int]) -> list[list[int]]:
        delta_x, delta_y = relative_movement
        if self.color == 'black':
            if not self.moved_flag and delta_y == 2:
                return ['nocapturing', [0, 1], [0, 2]]
            if delta_y == 1 and delta_x == 0:
                return ['nocapturing', [0, 1]]
            if delta_y == 1 and abs(delta_x) == 1:
                return ['capturing', relative_movement]
            return ['Error', 'Invalid target square']

        if self.color == 'white':
            if not self.moved_flag and delta_y == -2:
                return ['nocapturing', [0, -1], [0, -2]]
            if delta_y == -1 and delta_x == 0:
                return ['nocapturing', [0, -1]]
            if delta_y == -1 and abs(delta_x) == 1:
                return ['capturing', relative_movement]
            return ['Error', 'Invalid target square']

        if self.color == 'red':
            if not self.moved_flag and delta_x == 2:
                return ['nocapturing', [1, 0], [2, 0]]
            if delta_y == 0 and delta_x == 1:
                return ['nocapturing', [1, 0]]
            if delta_x == 1 and abs(delta_y) == 1:
                return ['capturing', relative_movement]
            return ['Error', 'Invalid target square']

        if self.color == 'blue':
            if not self.moved_flag and delta_x == -2:
                return ['nocapturing', [-1, 0], [-2, 0]]
            if delta_y == 0 and delta_x == 1:
                return ['nocapturing', [-1, 0]]
            if delta_x == -1 and abs(delta_y) == 1:
                return ['capturing', relative_movement]
            return ['Error', 'Invalid target square']
        return ['Error', 'Invalid target square']

    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        if 'impassable' in map_path or 'impassible_imjumpable' in map_path:
            return ['Error', 'Impassable square in the way']

        if board_path[0] == 'nocapturing':
            if board_path[1] != '' or (len(board_path) == 3 and board_path[2] != ''):
                return ['Error', 'Path obstructed by pieces']
        if board_path[0] == 'capturing':
            if board_path[1] == '' or board_path[1].color == self.color:
                return ['Error', 'No one to capture']
        self.moved_flag = True

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        if self.color == 'black':
            return [[1, 1], [-1, 1]]
        if self.color == 'white':
            return [[1, -1], [-1, -1]]
        if self.color == 'red':
            return [[1, 1], [1, -1]]
        if self.color == 'blue':
            return [[-1, 1], [-1, -1]]

    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int) -> list[list[int, int]]:
        validated_attack = list()
        for square in list(map_path):
            if 'impassable' not in map_path[square][0]:
                validated_atack.append(map_path[square][1])




