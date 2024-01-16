from typing import List
import math
from functools import cached_property

from geometry.point import Point

class SearchMap: 
    def __init__(
        self, 
        map_width_px: int,
        map_height_px: int,
        search_radius_px: float, 
        map: int=0, 
        scale_factor: float=0.0
    ):
        # TODO: make map private, getters / setters etc
        self.map = map
        self.map_width_px = map_width_px
        self.map_height_px = map_height_px
        self.search_radius_px = search_radius_px
        self.scale_factor = scale_factor

        self.map_width_bits = self.map_width_px * self.scale_factor
        self.map_height_bits = self.map_height_px * self.scale_factor
        self.search_radius_bits = self.search_radius_px * self.scale_factor

    @cached_property
    def n_bits(self):
        return self.map_height_px * self.map_width_px

    def __str__(self) -> str:
        """Iterate through the string map to print to console."""
        input = self.__as_str()
        output = ""

        for row in range(0, self.n_bits, self.map_width_px):
            output += input[row:row+self.map_width_px] + "\n"

        return output

    def __as_str(self) -> str: 
        """Return a string representation of the map."""
        str_map_val = str(bin(self.map))[2:]
        return str_map_val.rjust(self.n_bits, "0")

    def __max_grid_val(self) -> int:
        return (2**self.n_bits) - 1

    def reveal(self, point: Point) -> None: 
        """Alter to map to reveal the 'tile' at the given Point position."""
        self.map |= self.grid_binary_value(point)

    def reveal_radius(self, point: Point) -> None:
        """Reveal a radius around a point."""
        for given_point in self.get_points_in_search_radius(
            centre=point
        ): 
            self.reveal(given_point)

    def invert_point(self, point: Point) -> Point:
        invert_x = (self.map_width_px - point.x) -1
        invert_y = (self.map_height_px - point.y) -1
        return Point(invert_x, invert_y)

    def grid_index_pos(self, point: Point) -> int:
        inverted = self.invert_point(point)
        return (self.map_width_px * inverted.y) + inverted.x

    def grid_binary_value(self, point: Point) -> int:
        return 2 ** self.grid_index_pos(point)

    def get_points_in_search_radius(
        self, 
        centre: Point
    ) -> List[Point]:
        """List of points within search radius of a given point."""
        points_in_search_radius = []

        min_x = max(0, math.floor(centre.x - self.search_radius_px))
        max_x = min(self.map_width_px, math.ceil(centre.x + self.search_radius_px))

        min_y = max(0, math.floor(centre.y - self.search_radius_px))
        max_y = min(self.map_height_px, math.ceil(centre.y + self.search_radius_px))

        for x_value in range(min_x, max_x): 
            for y_value in range(min_y, max_y):
                point = Point(x_value, y_value)
                if centre.distance_to(point) <= self.search_radius_px: 
                    points_in_search_radius.append(point)

        return points_in_search_radius