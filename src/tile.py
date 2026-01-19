# Tile class representing a single cell on the game board


class Tile:
    def __init__(self, x, y):
        """
        Initialize a tile with coordinates

        Args:
            x: X coordinate in pixels
            y: Y coordinate in pixels
        """
        self.x = x
        self.y = y
