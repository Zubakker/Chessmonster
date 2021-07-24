from piece import Piece

class VanillaWazir(Piece):
    def __init__(self, position: list[int], color: str) -> None:
        super().__init__(position, color)
        self.value = 1
        self.name = 'vanilla:wazir'
        return


    def return_path(self, relative_movement: list[int]) -> list[list[int]]:
        delta_x, delta_y = relative_movement

        if abs(delta_x) + abs(delta_y) != 1:
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
    

    def validate_placement(self, map_square: str, board_square: Piece) -> list[str, str]:
        if map_square == 'impassable':
            return ['Error', 'Impassable square in the way']
        return ['Success', 'Succsess']

    def return_attack(self, movement_points: int) -> list[list[int, int]]:
        return [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def validate_attack( self, map_path: dict, board_path: dict, attack_path: dict, movement_points: int ):
        validated_attack = list()
        for es in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 'impassible' in map_path[ str(es) ][0]:
                continue
            else:
                validated_attack.append(es)

        return validated_attack
