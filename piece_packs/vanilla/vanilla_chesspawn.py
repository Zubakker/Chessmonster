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


