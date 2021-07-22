from piece import Piece

class VanillaKnight(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 3
        self.name = 'vanilla:knight'
        return


    def return_path(self, relative_movement: list[int]) -> list[str, list[int]]:
        delta_x, delta_y = relative_movement
        
        if abs(delta_x * delta_y) != 2:
            return ['Error', 'Invalid target square']
        movement_path = ['']
        for i in range(delta_x + 1):
            for j in range(delta_y + 1):
                movement_path.append([i, j])
            for j in range(-delta_y + 1):
                movement_path.append([i, -j])
        for i in range(-delta_x + 1):
            for j in range(delta_y + 1):
                movement_path.append([-i, j])
            for j in range(-delta_y + 1):
                movement_path.append([-i, -j])

        return movement_path

    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        if 'imjumpable' in map_path or 'impassable_imjumpable' in map_path:
            return ['Error', 'Imjumpable square in the way']
        if board_path[-1] != '' and board_path[-1].color == self.color:
            return ['Error', 'Same color piece on target square']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square == 'imjumpable':
            return ['Error', 'Imjumpable square in the way']
        return ['Success', 'Succsess']


