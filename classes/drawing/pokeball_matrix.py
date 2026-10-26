from ..my_types import Color
from .matrix_object import MatrixObject
from .circle import Circle
from .rect import Rect


class PokeballMatrix(MatrixObject):

    def __init__(self, w, h, r):
        super().__init__(w, h)
        WHITE: Color = (256, 256, 256)
        RED: Color = (256, 0, 0)
        BLACK: Color = (0, 0, 0)

        d = r * 2
        step0 = Circle(r, WHITE)

        top = Rect(d, r, RED)
        step1 = step0.paint(top.data)

        middle = Rect(d, d / 6, WHITE)
        step2 = step1.paint(middle.data, 0, r / 6)

        button = Circle(r /, BLACK)

