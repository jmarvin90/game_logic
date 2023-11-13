from __future__ import annotations
from typing import List, Optional
import math
import time

SEARCH_MAP_SIZE = 16
SEARCH_RAD = 3.5


class SearchMap: 
    def __init__(self, map: int=0):
        self._map = map

    @property
    def str_map(self) -> str: 
        """Return a string representation of the map."""
        str_map_val = str(bin(self._map))[2:]
        return str_map_val.rjust(SEARCH_MAP_SIZE**2, "0")

    def reveal(self, point: Point) -> None: 
        """Alter to map to reveal the 'tile' at the given Point position."""
        self._map |= point.binary_grid_value

    def show(self) -> None:
        """Iterate through the string map to print to console."""
        for row in range(0, SEARCH_MAP_SIZE): 
            min = row * SEARCH_MAP_SIZE
            max = min + SEARCH_MAP_SIZE
            print(self.str_map[min:max])


class Edge: 
    def __init__(self, origin: Point, termination: Point):
        self.origin = origin
        self.termination = termination

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
    
    def solve_intersection(self, point: Point):
    	# computes the intersection between two line segments; a to b, and c to d
	
        ab = self.termination - self.origin
        cd = point.termination - point.origin
	
        ab_cross_cd = ab.cross(cd)
        
        if ab_cross_cd == 0:
            
            return None
        else:
            ac = point.origin - self.origin
            t1 = ac.cross(cd) / ab_cross_cd
            t2 = -ab.cross(ac) / ab_cross_cd
            intersect_point = self.origin + ab.scaled(t1)
            print(intersect_point.x, intersect_point.y)
            return intersect_point, t1, t2
    
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
        

class Point: 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

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
        """Inverse a coordinate value according to a bottom-right-oriented grid."""
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
    
    def search(self, search_map: SearchMap) -> int: 
        """Alter the map to reveal all tiles for points in the search radius."""
        for point in self.get_points_in_search_radius(): 
            search_map.reveal(point)
        
        return search_map
    
    @property
    def is_in_bounds(self) -> bool: 
        """Indicate whether the specified point is in bounds of the map."""
        in_x = 0 <= self._x <= SEARCH_MAP_SIZE
        in_y = 0 <= self._y <= SEARCH_MAP_SIZE
        return in_x and in_y



if __name__ == "__main__":
    my_search_map = SearchMap()

    edge1p1 = Point(8, 0)
    edge1p2 = Point(8, 10)

    edge2p1 = Point(15, 0)
    edge2p2 = Point(6, 10)

    edge1 = Edge(edge1p1, edge1p2)
    edge2 = Edge(edge2p2, edge2p1)

    for point in [*edge1.intermediary_points(), *edge2.intermediary_points()]:
        my_search_map.reveal(point)

    my_search_map.show()

    print(edge1.solve_intersection(edge2))


    

    
    # my_edge = Edge(point_1, point_2)
    # for point in my_edge.intermediary_points():
    #     point.search(my_search_map)
    #     my_search_map.show()
    #     time.sleep(0.5)


