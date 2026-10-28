from .matrix_object import MatrixObject
from .circle import Circle
from .rect import Rect
from ..types.color import Color


class PokeballMatrix(MatrixObject):
    """
    a class that represents a 2D matrix of colors (RGB tuples) in the shape of a pokeball,
    it provides methods to manipulate and to convert it to and from binary data to use in bitmaps
    """

    def __init__(self, w, h, r):
        super().__init__(w, h)
        WHITE: Color = (256, 256, 256)
        RED: Color = (256, 0, 0)
        BLACK: Color = (0, 0, 0)

        d = r * 2
        step0 = Circle(r, WHITE)

        top = Rect(d, r, RED)
        step1 = step0.paint(top.data)

        middle = Rect(d, d / 7, BLACK)
        step2 = step1.paint(middle.data, 0, r / 7)

        button_ring = Circle(d / 4, BLACK)
        step3 = step2.paint(button_ring.data, r / 4, r / 4)

        button_ring = Circle(d / 3, WHITE)
        step3 = step2.paint(button_ring.data, r / 3, r / 3)

        self.data = step3

