from __future__ import annotations
from typing import Optional, List, Tuple
import math

from src.geometry.point import Point


class Edge: 
    def __init__(self, origin: Point, termination: Point):
        # TODO: may be better to reimplement some @properties
        # It is not likely that they'll need to be recomputed once they've been
        # calcualted for the first time; perhaps cached_property is better

        self.origin = origin
        self.termination = termination

    def __eq__(self, edge_2: Edge):
        """Check if two edges are the same."""
        # TODO: this won't work if Edge.__contains__ is updated for point on line
        return self.origin in edge_2 and self.termination in edge_2

    def __contains__(self, point: Point) -> bool:
        """Check if a given point occurs within the edge."""
        return (
            self.origin == point or
            self.termination == point 
            # TODO: implement 'point is on line' check; 
            # e.g. Point is in self.intermediary_points
        )

    def __str__(self):
        return f"{self.origin} -> {self.termination}"

    @property
    def x_diff(self) -> float:
        return self.termination.x - self.origin.x
    
    @property
    def y_diff(self) -> float:
        return self.termination.y - self.origin.y

    @property
    def y_intercept(self) -> float:
        """Return the y-intercept."""
        return self.origin.y - (self.gradient * self.origin.x)

    @property
    def diagonal_distance(self) -> int: 
        """"""
        return max(abs(self.x_diff), abs(self.y_diff))
    
    @property
    def length(self) -> float: 
        """Return the length of the edge."""
        return self.origin.distance_to(self.termination)
    
    @property
    def angle(self) -> float:
        """"""
        return math.atan2(self.x_diff, self.y_diff)

    @property
    def is_vertical(self) -> bool: 
        return self.origin.x == self.termination.x
    
    @property
    def is_horizontal(self) -> bool: 
        return self.origin.y == self.termination.y
    
    @property
    def gradient(self) -> float: 
        """"""
        if self.is_vertical: 
            return 1
        
        if self.is_horizontal: 
            return 0
        
        return self.y_diff / self.x_diff

    @property
    def centre(self) -> Point:
        """Return the centre point of the edge."""
        mid_x = self.origin.x + (self.x_diff / 2)
        mid_y = self.origin.y + (self.y_diff / 2)
        # TODO: Point constructor is going to round float values down - 
        # that'll likely be a problem
        return Point(mid_x, mid_y)

    @staticmethod
    def orientation(point_a: Point, point_b: Point, point_c: Point) -> int:
        """Return the orientation of three points.
        
        -1 denotes counterclock; 0 denotes vertical, and +1 denotes clock.
        """

        # TODO: check if there is some repeatable way to calculate val at instance level
        # TODO: also check if this interface can be improved (e.g. can it accept an edge+point)

        edge_1 = Edge(point_b, point_a)
        edge_2 = Edge(point_c, point_b)

        val = (
            (edge_1.y_diff * edge_2.x_diff) - 
            (edge_1.x_diff * edge_2.y_diff)
        )

        if val > 1: 
            return 1
        
        if val < 0: 
            return -1
        
        return 0
    
    def intersects(self, edge: Edge) -> bool:
        """Check if the current edge intersects another."""
        # TODO: streamline
        acd = Edge.orientation(self.origin, edge.origin, edge.termination)
        bcd = Edge.orientation(self.termination, edge.origin, edge.termination)
        abc = Edge.orientation(self.origin, self.termination, edge.origin)
        abd = Edge.orientation(self.origin, self.termination, edge.termination)

        return acd != bcd and abc != abd
    
    def is_parallel_to(self, edge_2: Edge) -> bool: 
        """Check if the current edge is parallel to another."""
        if self.is_horizontal and edge_2.is_horizontal: 
            return True
        
        if self.is_vertical and edge_2.is_vertical: 
            return True
        
        return self.gradient == edge_2.gradient

    def interpolate(self, start: int, end: int, step: float) -> float: 
        """Interpolate the next 'step' between a given start and end."""
        difference = end - start
        portion = difference * step
        return round(start + portion)
    
    def intermediary_points(self, n_steps: Optional[int]=None) -> List[Point]:
        """Return intermediary points between start and end."""
        # TODO: perhaps could be a cached property
        points = [self.origin, self.termination]
        
        if n_steps is None: 
            n_steps = self.diagonal_distance

        for step in range(1, n_steps + 1): 
            t = step / n_steps
            x = self.interpolate(self.origin.x, self.termination.x, t)
            y = self.interpolate(self.origin.y, self.termination.y, t)
            points.insert(-1, Point(x, y))

        # TODO: check that points will be returned in order origin->termination
        return points

    @staticmethod
    def points_are_collinear(*points: Tuple[Point]) -> bool:
        """Check if points are collinear based on their y-intercept."""
        initial_edge = Edge(points[0], points[1])
        for number in range(1, len(points)):
            comparison_edge = Edge(points[0], points[number])
            if comparison_edge.y_intercept != initial_edge.y_intercept:
                return False

        return True
