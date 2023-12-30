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
        output = []

        # TODO: the algorithm here
        
        for item in output:
            print(item)
        return output

        """ 

        0         1         2         3
        x ------- x ------- x ------- x
        |                             |
        |                             |
        |                             |
        x ----------------- x ------- x
        6, -1               5         4

        """



