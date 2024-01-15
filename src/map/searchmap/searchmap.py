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
        self.map |= point.binary_grid_value(
            width=self.map_width_px, 
            height=self.map_height_px
        )

    def reveal_radius(self, point: Point) -> None:
        """Reveal a radius around a point."""
        for given_point in self.get_points_in_search_radius(
            centre=point
        ): 
            self.reveal(given_point)

    def get_points_in_search_radius(
        self, 
        centre: Point
    ) -> List[Point]:
        """List of points within search radius of a given point."""
        points_in_search_radius = []

        for x_value in range(
            centre.min_search_x(search_radius=self.search_radius), 
            centre.max_search_x(
                search_radius=self.search_radius,
                width=self.map_width_px
            )
        ): 
            for y_value in range(
                centre.min_search_y(search_radius=self.search_radius), 
                centre.max_search_y(
                    search_radius=self.search_radius, 
                    height=self.map_height_px
                )
            ):
                point = Point(x_value, y_value)
                if centre.distance_to(point) <= self.search_radius: 
                    points_in_search_radius.append(point)

        return points_in_search_radius