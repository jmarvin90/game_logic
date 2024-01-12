from typing import List
import math
from functools import cached_property

from geometry.point import Point

class SearchMap: 
    def __init__(
        self, 
        map_width_px: int,
        map_height_px: int,
        search_radius: float, 
        map: int=0
    ):
        # TODO: make map private, getters / setters etc
        self.map = map
        self.map_width_px = map_width_px
        self.map_height_px = map_height_px
        self.search_radius = search_radius

    @cached_property
    def n_bits(self):
        return self.map_height_px * self.map_width_px

    def __str__(self) -> str:
        """Iterate through the string map to print to console."""
        input = self.__as_str()
        output = ""
        
        for row in range(0, self.map_height_px): 
            min = row * self.map_width_px
            max = min + self.map_width_px
            output += input[min:max] + "\n"

        return output

    def __as_str(self) -> str: 
        """Return a string representation of the map."""
        str_map_val = str(bin(self.map))[2:]
        return str_map_val.rjust(self.n_bits, "0")

    def __max_search_val(self) -> int:
        return (1 << (self.n_bits)) -1

    def reveal(self, point: Point) -> None: 
        """Alter to map to reveal the 'tile' at the given Point position."""
        self.map |= self.point_binary_grid_value(point)

    def reveal_radius(self, point: Point) -> None:
        """Reveal a radius around a point."""
        for given_point in self.get_points_in_search_radius(
            centre=point
        ): 
            self.reveal(given_point)

    def __inverse_coordinate(self, coordinate: int, span: int) -> int:
        """Inverse a coordinate value as per a bottom-right-oriented grid."""
        return (span - coordinate) -1

    def __inverse_point_x(self, point: Point) -> int:
        return self.__inverse_coordinate(point.x, self.map_width_px)

    def __inverse_point_y(self, point: Point) -> int:
        return self.__inverse_coordinate(point.y, self.map_height_px)

    def __inverse_point(self, point: Point) -> int:
        return Point(
            self.__inverse_point_x(point), self.__inverse_point_y(point)
        )

    def point_binary_grid_index_position(self, point: Point) -> int:
        inversed = self.__inverse_point(point)

        return (
            (self.map_width_px * inversed.y) +
            inversed.x
        )

    def point_binary_grid_value(self, point: Point) -> int:
        return 2**self.point_binary_grid_index_position(point)

    def point_search_min_x(self, point: Point) -> int:
        return max(0, math.floor(point.x - self.search_radius))

    def point_search_max_x(self, point: Point) -> int:
        return min(self.map_width_px, math.ceil(point.x + self.search_radius))

    def point_search_min_y(self, point: Point) -> int:
        return max(0, math.floor(point.y - self.search_radius))

    def point_search_max_y(self, point: Point) -> int:
        return min(self.map_height_px, math.ceil(point.y + self.search_radius))

    def get_points_in_search_radius(
        self, 
        centre: Point, 
        search_radius: float = None
    ) -> List[Point]:
        """List of points within search radius of a given point."""
        if not search_radius:
            search_radius = self.search_radius

        points_in_search_radius = []

        for x_value in range(
            self.point_search_min_x(centre), self.point_search_max_x(centre)
        ): 
            for y_value in range(
                self.point_search_min_y(centre), self.point_search_max_y(centre)
            ):
                point = Point(x_value, y_value)
                if centre.distance_to(point) <= search_radius: 
                    points_in_search_radius.append(point)

        return points_in_search_radius