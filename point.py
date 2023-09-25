from __future__ import annotations
from typing import List 
import math

SEARCH_MAP_SIZE = 16
SEARCH_RAD = 4.5

class Point: 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def search_min_x(self) -> int: 
        min_x = max(0, math.ceil(self._x - SEARCH_RAD))
        return min_x
    
    @property
    def search_max_x(self) -> int:
        max_x = min(SEARCH_MAP_SIZE, math.floor(self._x + SEARCH_RAD))
        return max_x
    
    @property
    def search_min_y(self) -> int:
        min_y = max(0, math.ceil(self._y - SEARCH_RAD))
        return min_y
    
    @property
    def search_max_y(self) -> int: 
        max_y = min(SEARCH_MAP_SIZE, math.floor(self._y + SEARCH_RAD))
        return max_y

    def inverse_coordinate(self, coordinate: int):
        inverse = SEARCH_MAP_SIZE - (-1 * coordinate)
        return inverse - 1
    
    @property
    def inverse_y(self) -> int:
        return self.inverse_coordinate(self._y)
    
    def distance_to(self, point: Point) -> float: 
        x_delta = self._x - point._x
        y_delta = self._y - point._y
        distance_to_point = math.sqrt(x_delta**2 + y_delta**2)
        return distance_to_point
    
    def get_points_in_search_radius(self) -> List[Point]:
        points_in_search_radius = []

        for x_value in range(self.search_min_x, self.search_max_x): 
            for y_value in range(self.search_min_y, self.search_max_y):
                point = Point(x_value, y_value)
                if self.distance_to(point) <= SEARCH_RAD: 
                    points_in_search_radius.append(point)

        return points_in_search_radius
