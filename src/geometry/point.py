from __future__ import annotations
import math

class Point: 
    def __init__(self, x: int, y: int):
        self._x = int(x)
        self._y = int(y)

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
        return Point(
            x = self.x * scale_factor, 
            y = self.y * scale_factor
        )
        
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
        return math.hypot(x_delta, y_delta)