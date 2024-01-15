from __future__ import annotations
from typing import List
import math

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
    def _invert_coordinate(coordinate: int, span: int) -> int:
        """Inverse a coordinate value as per a bottom-right-oriented grid."""
        return (span - coordinate) -1

    def invert_point(self, width: int, height: int) -> Point:
        return Point(
            self._invert_coordinate(self.x, width), 
            self._invert_coordinate(self.y, height)
        )

    def binary_grid_index_pos(self, width: int, height: int) -> int:
        inverted = self.invert_point(width, height)
        return (width * inverted.y) + inverted.x

    def binary_grid_value(self, width: int, height: int) -> int:
        return 2**self.binary_grid_index_pos(width, height)

    @staticmethod
    def __min_search(coordinate: int, search_radius: float) -> int:
        return max(0, math.floor(coordinate - search_radius))

    @staticmethod
    def __max_search(coordinate: int, search_radius: float, span: int) -> int:
        return min(span, math.ceil(coordinate + search_radius))

    def min_search_x(self, search_radius:float) -> int:
        return Point.__min_search(self.x, search_radius)

    def max_search_x(self, search_radius:float, width: int) -> int:
        return Point.__max_search(self.x, search_radius, width)

    def min_search_y(self, search_radius:float) -> int:
        return Point.__min_search(self.y, search_radius)

    def max_search_y(self, search_radius: float, height: int) -> int:
        return Point.__max_search(self.y, search_radius, height)
        
    @property
    def x(self) -> int: 
        """Return the point X coordinate."""
        return self._x  
    
    @property
    def y(self) -> int: 
        """Return the point Y coordinate."""
        return self._y

    @property
    def distance_to_origin(self) -> float:
        """Return the distance to the origin (0, 0). Useful for sorting."""
        return self.distance_to(Point(0,0))
    
    def distance_to(self, point: Point) -> float: 
        """Calculate the distance to another point."""
        x_delta = self.x - point.x
        y_delta = self.y - point.y
        distance_to_point = math.hypot(x_delta, y_delta)
        return distance_to_point
    
    # @property
    # def is_in_bounds(self) -> bool: 
    #     """Indicate whether the specified point is in bounds of the map."""
    #     in_x = 0 <= self.x <= SEARCH_MAP_SIZE
    #     in_y = 0 <= self.y <= SEARCH_MAP_SIZE
    #     return in_x and in_y