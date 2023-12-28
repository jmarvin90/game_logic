from typing import Tuple

import geometry.point
import geometry.edge

class Polygon:
    def __init__(self, *points):
        self.points = points
    
    @staticmethod
    def edges_from_points(*points: Tuple[geometry.point.Point]) -> tuple:
        """Return a sequence of edges from ordered points tuple."""
        anchor = -1
        output = []

        # TODO: this doesn't currently work.
        # The idea is that it should return the minimum number of points
        # needed to represent the polygon.
        for number in range(0, len(points)):
            short = geometry.edge.Edge(points[anchor], points[number])
            long = geometry.edge.Edge(points[anchor], points[number + 1])
            if not long.is_parallel_to(short):
                print(short)
                output.append(short)
                anchor = number

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



