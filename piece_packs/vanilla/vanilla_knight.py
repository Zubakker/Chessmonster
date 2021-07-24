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
        if abs(delta_y) == 2:
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
        if abs(delta_x) == 2:
            for j in range(delta_y + 1):
                for i in range(delta_x + 1):
                    movement_path.append([i, j])
                for i in range(-delta_x + 1):
                    movement_path.append([i, -j])
            for j in range(-delta_y + 1):
                for i in range(delta_x + 1):
                    movement_path.append([-i, j])
                for i in range(-delta_x + 1):
                    movement_path.append([-i, -j])


        return movement_path

    def validate_path(self, map_path: list[str], board_path: list[Piece]) -> list[list[int]]:
        invalid_list = ['imjumpable', 'impassable_imjumpable']
        if (map_path[1] in invalid_list or map_path[2] in invalid_list) and \
                    (map_path[3] in invalid_list or map_path[4] in invalid_list):
            return ['Error', 'Imjumpable square in the way']
        if map_path[-1] in invalid_list:
            return ['Error', 'Imjumpable square in the way']
        if board_path[-1] != '' and board_path[-1].color == self.color:
            return ['Error', 'Same color piece on target square']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square != 'passable':
            return ['Error', 'Imjumpable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        if movement_points < 1: #temporary value
            return list()
        attack_squares
        if abs(delta_y) == 2:
            for i in range(delta_x + 1):
                for j in range(delta_y + 1):
                    attack_squares.append([i, j])
                for j in range(-delta_y + 1):
                    attack_squares.append([i, -j])
            for i in range(-delta_x + 1):
                for j in range(delta_y + 1):
                    attack_squares.append([-i, j])
                for j in range(-delta_y + 1):
                    attack_squares.append([-i, -j])
        if abs(delta_x) == 2:
            for j in range(delta_y + 1):
                for i in range(delta_x + 1):
                    attack_squares.append([i, j])
                for i in range(-delta_x + 1):
                    attack_squares.append([i, -j])
            for j in range(-delta_y + 1):
                for i in range(delta_x + 1):
                    attack_squares.append([-i, j])
                for i in range(-delta_x + 1):
                    attack_squares.append([-i, -j])
        return attack_squares


    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int) -> list[list[int, int]]:
        invalid_list = ['imjumpable', 'impassable_imjumpable']
        if (map_path[1][0] in invalid_list or map_path[2][0] in invalid_list) and \
                    (map_path[3][0] in invalid_list or map_path[4][0] in invalid_list):
            return list()
        if map_path[-1][0] in invalid_list:
            return ['Error', 'Imjumpable square in the way']

        return map_path[-1][1]


