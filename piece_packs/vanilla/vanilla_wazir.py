from piece import Piece

class VanillaWazir(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 1
        self.name = 'vanilla:wazir'
        return


    def return_path(self, relative_movement: list[int]) -> list[list[int]]:
        delta_x, delta_y = relative_movement

        if (delta_x != 0 and delta_y != 0) or (delta_x == 0 and delta_y == 0):
            return ['Error', 'Invalid target square']
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            return ['Error', 'Invalid target square']
        return [relative_movement]


    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        if 'impassable' in map_path:
            return ['Error', 'Impassable square in the way']

        if board_path[0] != '':
            target_piece = board_path[0]
            if target_piece.color == self.color:
                return ['Error', 'Same color piece in target square']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        if board_square != '':
            return ['Error', 'A piece in the way']
        return ['Success', 'Succsess']


