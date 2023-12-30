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

        for number in range(len(points)):
            short = Edge(points[anchor], points[number])
            long = Edge(points[anchor], points[(number+1)%len(points)])
            if not long.is_parallel_to(short):
                output.append(short)
                anchor = number
        
        for item in output:
            print(item)
        return output



