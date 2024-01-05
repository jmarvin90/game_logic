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
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point: Point) -> Point:
        return Point(self.x - point.x, self.y - point.y)

    def __gt__(self, point: Point) -> bool:
        """Check if a point is further from origin."""
        # TODO: this might not work
        # What if there are two points equidistant from origin?
        # This was originally supposed to enable sorting of points in a sequence
        # but that could be achieved by other means
        return self.distance_to(Point(0, 0)) > point.distance_to(Point(0, 0))

    def __lt__(self, point: Point) -> bool:
        """Check if a point is closer to origin."""
        # TODO: as above
        return self.distance_to(Point(0, 0)) < point.distance_to(Point(0, 0))

    def __mul__(self, point: Point) -> Point:
        """"""
        # TODO: docstring & check if multiplication is appropriate
        return Point(self.x * point.y, self.y * point.x)

    def dot_product(self, point: Point) -> float:
        """Return dot product of two points."""
        return (self.x * point.x) + (self.y * point.y)
    
    def scaled(self, scale_factor: float):
        return Point(self.x * scale_factor, self.y * scale_factor)

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
    def inverse_x(self) -> int:
        return Point.inverse_coordinate(self.x)
    
    @property
    def inverse_y(self) -> int: 
        return Point.inverse_coordinate(self.y)

    @property
    def search_min_x(self) -> int: 
        """Return the left-most X coordinate for the point's bounding box."""
        min_x = max(0, math.floor(self.x - SEARCH_RAD))
        return min_x
    
    @property
    def search_max_x(self) -> int:
        """Return the right-most X coordinate for the point's bounding box."""
        max_x = min(SEARCH_MAP_SIZE, math.ceil(self.x + SEARCH_RAD))
        return max_x
    
    @property
    def search_min_y(self) -> int:
        """Return the bottom-most Y coordinate for the point's bounding box."""
        min_y = max(0, math.floor(self.y - SEARCH_RAD))
        return min_y
    
    @property
    def search_max_y(self) -> int: 
        """Return the top-most Y coordinate for the point's bounding box."""
        max_y = min(SEARCH_MAP_SIZE, math.ceil(self.y + SEARCH_RAD))
        return max_y
    
    @property
    def binary_grid_index_position(self) -> int: 
        """Return the grid index position for the point."""
        return (SEARCH_MAP_SIZE * self.inverse_y) + self.inverse_x
    
    @property
    def binary_grid_value(self) -> int: 
        """Derive a binary number from the point's grid index position."""
        return 2**self.binary_grid_index_position
    
    def distance_to(self, point: Point) -> float: 
        """Calculate the distance to another point."""
        x_delta = self.x - point.x
        y_delta = self.y - point.y
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
        in_x = 0 <= self.x <= SEARCH_MAP_SIZE
        in_y = 0 <= self.y <= SEARCH_MAP_SIZE
        return in_x and in_y