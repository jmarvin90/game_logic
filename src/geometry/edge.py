from __future__ import annotations
from typing import Optional, List
import math

from geometry.point import Point


class Edge: 
    def __init__(self, origin: Point, termination: Point):
        self.origin = origin
        self.termination = termination

    def __str__(self):
        return f"{self.origin.__str__()} -> {self.termination.__str__()}"

    @property
    def _x_diff(self) -> float:
        return self.origin.x - self.termination.x
    
    @property
    def _y_diff(self) -> float:
        return self.origin.y - self.termination.y

    @property
    def diagonal_distance(self) -> int: 
        """"""
        x_delta = self.origin.x - self.termination.x
        y_delta = self.origin.y - self.termination.y
        return max(abs(x_delta), abs(y_delta))
    
    @property
    def length(self) -> float: 
        """Return the length of the edge."""
        return self.origin.distance_to(self.termination)
    
    @property
    def angle(self) -> float:
        """"""
        return math.atan2(self._x_diff, self._y_diff)

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
        
        print(self.origin, self.termination, self._y_diff / self._x_diff)
        return self._y_diff / self._x_diff

    @staticmethod
    def orientation(point_a: Point, point_b: Point, point_c: Point) -> int:
        """Return the orientation of three points.
        
        -1 denotes counterclock; 0 denotes vertical, and +1 denotes clock.
        """

        # TODO: check if there is some better way to calculate val using magic methods

        edge_1 = Edge(point_b, point_a)
        edge_2 = Edge(point_c, point_b)

        val = (
            (edge_1._y_diff * edge_2._x_diff) - 
            (edge_1._x_diff * edge_2._y_diff)
        )

        if val > 1: 
            return 1
        
        if val < 0: 
            return -1
        
        return 0
    
    def intersects(self, edge: Edge) -> bool:
        """Check if the current edge intersects another."""
        # TODO - streamline
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

    def _interpolate(self, start: int, end: int, step: float) -> float: 
        """Interpolate the next 'step' between a given start and end."""
        difference = end - start
        portion = difference * step
        result = start + portion
        return round(result)
    
    def intermediary_points(self, steps: Optional[int]=None) -> List[Point]:
        """Return intermediary points between start and end."""
        points = [self.origin, self.termination]
        
        if steps is None: 
            steps = self.diagonal_distance

        for step in range(1, steps + 1): 
            t = step / steps
            x = self._interpolate(self.origin.x, self.termination.x, t)
            y = self._interpolate(self.origin.y, self.termination.y, t)
            points.insert(-1, Point(x, y))

        return points
        
