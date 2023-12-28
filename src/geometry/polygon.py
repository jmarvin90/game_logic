from typing import Tuple

import geometry.point
import geometry.edge

class Polygon:
    def __init__(self, *points):
        self.points = points
    
    @staticmethod
    def edges_from_points(*points: Tuple[geometry.point.Point]) -> tuple:
        """Return a sequence of edges from ordered points tuple."""
        upper = len(points)
        anchor = 0

        output = []

        for number in range(len(points) -1):
            up_next = geometry.edge.Edge(points[anchor], points[number+1])
            after_that = geometry.edge.Edge(points[number+1], points[number+2])

            if not up_to_now.is_parallel_to(up_next):
                anchor = number
                output.append(up_to_now)

        return tuple(output)



