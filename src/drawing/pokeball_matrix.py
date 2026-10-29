from src import MatrixObject, Rect, Circle
from src.types import Color


class PokeballMatrix(MatrixObject):
    """
    a class that represents a 2D matrix of colors (RGB tuples) in the shape of a pokeball,
    it provides methods to manipulate and to convert it to and from binary data to use in bitmaps
    """

    def __init__(self, r: int):
        """
        :param r: the radius of the pokeball
        """
        d = r * 2
        super().__init__(d, d)

        WHITE: Color = (256, 256, 256)
        RED: Color = (256, 0, 0)
        BLACK: Color = (0, 0, 0)

        white_circle: Circle = Circle(r, WHITE)

        red_top: Rect = Rect(d, r, RED)
        malasian_flag: MatrixObject = white_circle.paint(red_top.data)

        middle: Rect = Rect(d, d / 7, BLACK)
        pokeball_from_behind: MatrixObject = malasian_flag.paint(middle.data, 0, r / 7)

        button_ring: Circle = Circle(d / 4, BLACK)
        broken_pokeball: MatrixObject = pokeball_from_behind.paint(button_ring.data, r / 4, r / 4)

        button: Circle = Circle(d / 3, WHITE)
        pokeball: MatrixObject = broken_pokeball.paint(button.data, r / 3, r / 3)

        self.data = pokeball.data
