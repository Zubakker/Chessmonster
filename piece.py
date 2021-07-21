class Piece:
    def __init__(self, position, color):
        self.value = 0
        self.position = position
        self.color = color
        self.alive = True
        self.name = 'default_piece'
        pass
    
    def return_path(self, relative_movement):
        pass

    def validate_path(self, map_path, board_path):
        pass

    def validate_placement(self, map_square, board_square):
        pass


