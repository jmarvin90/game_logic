from typing import Tuple

from src.geometry.point import Point
from src.geometry.edge import Edge

class Polygon:
    def __init__(self, *points):
        self.points = points
        self.edges = ()

    @staticmethod
    def remove_redundant_points(*points: Point) -> Tuple[Point]:
        """Remove points in a series which aren't needed to plot a polygon."""
        output = []

        for number, point in enumerate(points):
            point_after = points[(number + 1) % len(points)]
            point_before = points[number -1]

            # we don't need points on the same line as the one before/after
            if not Edge.points_are_collinear(point_before, point, point_after):
                output.append(point)

        return tuple(output)
    
    @staticmethod
    def edges_from_points(*points: Point) -> Tuple[Edge]:
        """Return a sequence of edges from ordered points tuple."""
        rationalised_points = Polygon.remove_redundant_points(*points)
        output = []

        for number in range(len(rationalised_points)):
            output.append(
                Edge(
                    rationalised_points[number], 
                    rationalised_points[(number+1) % len(rationalised_points)]
                )
            )

        return tuple(output)

    def covers_point(self, point: Point) -> bool:
        """Check whether the polygon covers a specified point."""
        # TODO: this method probably should be on the Point
        # Moving it to Point (e.g. Point.is_inside(polygon)) would create a 
        # circular import - need to find a fix
        off_chart_point = Point(-1, point.y)
        intersect_edge = Edge(off_chart_point, point)

        crossed_edges = [
            edge for edge in self.edges if edge.intersects(intersect_edge)
        ]

        for item in crossed_edges:
            print(item)

        if len(crossed_edges) % 2 == 0:
            return False
        
        return True
