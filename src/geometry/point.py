from __future__ import annotations
from typing import List
import math

from geometry.constants import SEARCH_MAP_SIZE, SEARCH_RAD

class Point: 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, point: Point) -> bool:
        return self.x == point.x and self.y == point.y

    def __add__(self, point: Point) -> Point:
        return Point(self._x + point.x, self._y + point.y)

    def __sub__(self, point: Point) -> Point:
        return Point(self._x - point.x, self._y - point.y)
    
    def cross(self, point: Point) -> float:
        return (self._x * point.y) - (self._y * point.x)
    
    def scaled(self, scale_factor: float):
	    return Point(self._x * scale_factor, self._y * scale_factor)

    @staticmethod
    def inverse_coordinate(coordinate: int) -> int: 
        """Inverse a coordinate value as per a bottom-right-oriented grid."""
        inversed = SEARCH_MAP_SIZE - coordinate
        return inversed - 1
        
    @property
    def x(self) -> int: 
        """Return the point X coordinate."""
        return self._x  
    
    @property
    def y(self) -> int: 
        """Return the point Y coordinate."""
        return self._y
    
    @property
    def _inverse_x(self) -> int:
        return Point.inverse_coordinate(self._x)
    
    @property
    def _inverse_y(self) -> int: 
        return Point.inverse_coordinate(self._y)

    @property
    def search_min_x(self) -> int: 
        """Return the left-most X coordinate for the point's bounding box."""
        min_x = max(0, math.floor(self._x - SEARCH_RAD))
        return min_x
    
    @property
    def search_max_x(self) -> int:
        """Return the right-most X coordinate for the point's bounding box."""
        max_x = min(SEARCH_MAP_SIZE, math.ceil(self._x + SEARCH_RAD))
        return max_x
    
    @property
    def search_min_y(self) -> int:
        """Return the bottom-most Y coordinate for the point's bounding box."""
        min_y = max(0, math.floor(self._y - SEARCH_RAD))
        return min_y
    
    @property
    def search_max_y(self) -> int: 
        """Return the top-most Y coordinate for the point's bounding box."""
        max_y = min(SEARCH_MAP_SIZE, math.ceil(self._y + SEARCH_RAD))
        return max_y
    
    @property
    def binary_grid_index_position(self) -> int: 
        """Return the grid index position for the point."""
        return (SEARCH_MAP_SIZE * self._inverse_y) + self._inverse_x
    
    @property
    def binary_grid_value(self) -> int: 
        """Derive a binary number from the point's grid index position."""
        return 2**self.binary_grid_index_position
    
    def distance_to(self, point: Point) -> float: 
        """Calculate the distance to another point."""
        x_delta = self._x - point._x
        y_delta = self._y - point._y
        distance_to_point = math.hypot(x_delta, y_delta)
        return distance_to_point
    
    def get_points_in_search_radius(self) -> List[Point]:
        """List of points within the current point's search radius."""
        points_in_search_radius = []

        for x_value in range(self.search_min_x, self.search_max_x): 
            for y_value in range(self.search_min_y, self.search_max_y):
                point = Point(x_value, y_value)
                if self.distance_to(point) <= SEARCH_RAD: 
                    points_in_search_radius.append(point)

        return points_in_search_radius
    
    @property
    def is_in_bounds(self) -> bool: 
        """Indicate whether the specified point is in bounds of the map."""
        in_x = 0 <= self._x <= SEARCH_MAP_SIZE
        in_y = 0 <= self._y <= SEARCH_MAP_SIZE
        return in_x and in_y