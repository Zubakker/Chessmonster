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
                    movement_path[0] += str([i, j]) + "_"
                    movement_path.append([i, j])
                for j in range(-delta_y + 1):
                    movement_path[0] += str([i, -j]) + "_"
                    movement_path.append([i, -j])
            for i in range(-delta_x + 1):
                for j in range(delta_y + 1):
                    movement_path[0] += str([-i, j]) + "_"
                    movement_path.append([-i, j])
                for j in range(-delta_y + 1):
                    movement_path[0] += str([-i, -j]) + "_"
                    movement_path.append([-i, -j])
        if abs(delta_x) == 2:
            for j in range(delta_y + 1):
                for i in range(delta_x + 1):
                    movement_path[0] += str([i, j]) + "_"
                    movement_path.append([i, j])
                for i in range(-delta_x + 1):
                    movement_path[0] += str([-i, j]) + "_"
                    movement_path.append([-i, j])
            for j in range(-delta_y + 1):
                for i in range(delta_x + 1):
                    movement_path[0] += str([i, -j]) + "_"
                    movement_path.append([i, -j])
                for i in range(-delta_x + 1):
                    movement_path[0] += str([-i, -j]) + "_"
                    movement_path.append([-i, -j])


        return movement_path

    def validate_path(self, map_path: dict, board_path: dict, attack_path: dict) -> list[list[int]]:
        last_square = list(map_path)[-1]
        squares = board_path['flag'].split('_')
        invalid_list = ['imjumpable', 'impassable_imjumpable']
        if (map_path[squares[1]][0] in invalid_list or \
                    map_path[squares[2]][0] in invalid_list) and  \
                    (map_path[squares[3]][0] in invalid_list or \
                    map_path[squares[4]][0] in invalid_list):
            return ['Error', 'Imjumpable square in the way']
        if map_path[ last_square ][0] in invalid_list:
            return ['Error', 'Imjumpable square in the way']
        if board_path[ last_square ][0] != '' and \
                    board_path[ last_square ][0] == self.color:
            return ['Error', 'Same color piece on target square']

        return ['Success', 'Succsess']
    

    def validate_placement(self, map_square, board_square):
        if map_square != 'passable':
            return ['Error', 'Imjumpable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self,  movement_points: int) -> list[list[int, int]]:
        if movement_points < 1: #temporary value
            return list()
        attack_squares = list()
        for i in range(3):
            for j in range(2):
                if i == j == 0:
                    continue
                attack_squares.append([i, j])
                attack_squares.append([-i, j])
                attack_squares.append([-i, -j])
                attack_squares.append([i, -j])
                
                attack_squares.append([j, i])
                attack_squares.append([-j, i])
                attack_squares.append([-j, -i])
                attack_squares.append([j, -i])

        return attack_squares


    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int) -> list[list[int, int]]:
        invalid_list = ['imjumpable', 'impassable_imjumpable']
        validated_attack = list()
        for i_s in [-1, 1]:
            for j_s in [-1, 1]:
                if map_path[ str([2*i_s, 1*j_s]) ][0] in invalid_list:
                    continue
                if (map_path[ str([i_s, 0]) ][0] in invalid_list or \
                        map_path[ str([2*i_s, 0]) ][0] in invalid_list) and \
                        (map_path[ str([0, j_s]) ][0] in invalid_list or \
                        map_path[ str([i_s, j_s]) ][0] in invalid_list):
                    continue
                validated_attack.append( [2*i_s, j_s] )
        for i_s in [-1, 1]:
            for j_s in [-1, 1]:
                if map_path[ str([1*i_s, 2*j_s]) ][0] in invalid_list:
                    continue
                if (map_path[ str([0, j_s]) ][0] in invalid_list or \
                        map_path[ str([0, j_s]) ][0] in invalid_list) and \
                        (map_path[ str([i_s, 0]) ][0] in invalid_list or \
                        map_path[ str([i_s, j_s]) ][0] in invalid_list):
                    continue
                validated_attack.append( [i_s, 2*j_s] )
        return validated_attack


