from __future__ import annotations
from typing import List 
import math

SEARCH_MAP_SIZE = 32
SEARCH_RAD = 4.5

class MovementException(Exception): 
    def __init__(self): 
        super().__init__("Must use move method to alter point coordinates")


class SearchMap: 
    def __init__(self, map: int=0):
        self._map = 0

    def reveal(self, point: Point) -> None: 
        self._map |= point.binary_grid_value

    def show(self) -> None:
        str_map = str(bin(self._map))[2:]
        str_map = str_map.rjust(SEARCH_MAP_SIZE**2, "0")
        for row in range(0, SEARCH_MAP_SIZE): 
            min = row * SEARCH_MAP_SIZE
            max = min + SEARCH_MAP_SIZE
            print(str_map[min:max])


class Point: 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @staticmethod
    def inverse_coordinate(coordinate: int) -> int: 
        inversed = SEARCH_MAP_SIZE - coordinate
        return inversed - 1

    @property
    def x(self) -> int: 
        return self._x
    
    @property
    def y(self) -> int: 
        return self._y
    
    @x.setter
    def x(self, value) -> None: 
        raise MovementException
        
    @y.setter
    def y(self, value) -> None: 
        raise MovementException

    @property
    def search_min_x(self) -> int: 
        min_x = max(0, math.floor(self._x - SEARCH_RAD))
        return min_x
    
    @property
    def search_max_x(self) -> int:
        max_x = min(SEARCH_MAP_SIZE, math.ceil(self._x + SEARCH_RAD))
        return max_x
    
    @property
    def search_min_y(self) -> int:
        min_y = max(0, math.floor(self._y - SEARCH_RAD))
        return min_y
    
    @property
    def search_max_y(self) -> int: 
        max_y = min(SEARCH_MAP_SIZE, math.ceil(self._y + SEARCH_RAD))
        return max_y
    
    @property
    def binary_grid_index_position(self) -> int: 
        inverse_x = Point.inverse_coordinate(self._x)
        inverse_y = Point.inverse_coordinate(self._y)
        return (SEARCH_MAP_SIZE * inverse_y) + inverse_x
    
    @property
    def binary_grid_value(self) -> int: 
        return 2**self.binary_grid_index_position
    
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
    
    def search(self, search_map: SearchMap) -> int: 
        for point in self.get_points_in_search_radius(): 
            search_map.reveal(point)
        
        return search_map
    
my_search_map = SearchMap()
my_point = Point(10, 10)
my_search_map = my_point.search(my_search_map)
my_search_map.show()

#           beginning -> 111110000
# 00000000000000000000001111111000
# 00000000000000000000011111111000
# 00000000000000000000011111111000
# 00000000000000000000011111111000
# 00000000000000000000011111111000
# 00000000000000000000011111111000
# 00000000000000000000001111111000
# 00000000000000000000000000000000
# 00000000000000000000000000000000
# 00000000000000000000000000000000 -> end


