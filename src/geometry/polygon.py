from typing import Tuple

from geometry.point import Point
from geometry.edge import Edge

class Polygon:
    def __init__(self, *points):
        self.points = points
    
    @staticmethod
    def edges_from_points(*points: Tuple[Point]) -> tuple:
        """Return a sequence of edges from ordered points tuple."""
        anchor = -1
        mid = 0
        output = []
        return output

        """ 

        0         1         2
        x ------- x ------- x 
        |                   |
        |                   |
        |                   |
        x-------------------x
        4, -1               3

        """



