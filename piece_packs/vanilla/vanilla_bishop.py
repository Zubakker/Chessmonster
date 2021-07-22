from piece import Piece

class VanillaBishop(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 3
        self.name = 'vanilla:bishop'
        return


    def return_path(self, relative_movement: list[int]) -> list[str, list[int]]:
        delta_x, delta_y = relative_movement
        if delta_x * delta_y == 0 or abs(delta_x) != abs(delta_y):
            return ['Error', 'Invalid target square']
        movement_path = ['']
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


