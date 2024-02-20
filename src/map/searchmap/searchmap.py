from typing import List
import math
from functools import cached_property

from src.geometry.point import Point
from src.geometry.edge import Edge

class SearchMap: 
    def __init__(
        self, 
        map_width_px: int,
        map_height_px: int,
        search_radius_px: float, 
        map: int=0, 
        scale_factor: float=1.0
    ):
        # TODO: make map private, getters / setters etc
        self.map = map

        self.map_width_px = map_width_px
        self.map_height_px = map_height_px

        # TODO: total_px % scale_factor should == 0.
        # An exception should be raised if not.
        # Similarly, a scale-factor > 1 shouldn't be allowed.
        self.total_px = self.map_height_px * self.map_width_px

        self.search_radius_px = search_radius_px
        self.scale_factor = scale_factor

        # Must be whole bits
        self.map_width_bits = int(self.map_width_px * self.scale_factor)
        self.map_height_bits = int(self.map_height_px * self.scale_factor)

        self.search_radius_bits = self.search_radius_px * self.scale_factor

    @cached_property
    def n_bits(self):
        """Return the total number of bits in the searchmap."""
        return self.map_height_bits * self.map_width_bits

    def __str__(self) -> str:
        """Return a line-adjusted string representation of the map."""
        input = self.__as_str()
        output = ""

        for row in range(0, self.n_bits, self.map_width_bits):
            output += input[row:row+self.map_width_bits] + "\n"

        return output

    def __as_str(self) -> str: 
        """Return a string representation of the map."""
        str_map_val = str(bin(self.map))[2:]
        return str_map_val.rjust(self.n_bits, "0")

    @cached_property
    def _max_grid_val(self) -> int:
        """Return the maximum possible raw searchmap number."""
        return (2**self.n_bits) - 1

    def reveal(self, point: Point) -> None: 
        """Alter to map to reveal the 'tile' at the given Point position."""
        self.map |= self.bit_value(point)

    def reveal_radius(self, point: Point) -> None:
        """Reveal all points within the search radius around a given point."""
        for given_point in self.points_in_search_radius(
            centre=point
        ): 
            self.reveal(given_point)

    def invert_point(self, point: Point) -> Point:
        """Return a point with x, y inverted (top -> bottom, left -> right)."""
        invert_x = (self.map_width_bits -1) - point.x
        invert_y = (self.map_height_bits -1) - point.y
        return Point(invert_x, invert_y)

    def bit_position(self, point: Point) -> int:
        """Return the searchmap bit index position for a given point."""
        inverted = self.invert_point(point)
        return (self.map_width_bits * inverted.y) + inverted.x

    def bit_value(self, point: Point) -> int:
        """Return the binary value for a point's searchmap index position."""
        return 2 ** self.bit_position(point)

    def points_in_search_radius(
        self, 
        centre: Point
    ) -> List[Point]:
        """List of points within search radius of a given point."""
        points_in_search_radius = []

        # TODO - remedy the need to use -1 due to an indexing error

        # Define a bounding box around the centre using the radius
        # The left and right of the box
        min_x = max(
            0, math.floor(centre.x - self.search_radius_bits)
        )

        max_x = min(
            self.map_width_px -1, math.ceil(centre.x + self.search_radius_bits)
        )

        # The top and bottom of the box
        min_y = max(
            0, math.floor(centre.y - self.search_radius_bits)
        )

        max_y = min(
            self.map_height_px -1, math.ceil(centre.y + self.search_radius_bits)
        )

        # TODO: figure out how to generate the sides array programatically
        sides = [
            Edge(Point(min_x, min_y), Point(min_x, max_y)),         # Left
            Edge(Point(min_x, max_y), Point(max_x, max_y)),         # Top
            Edge(Point(max_x, max_y), Point(max_x, min_y)),         # Right
            Edge(Point(max_x, min_y), Point(min_x, min_y))          # Bottom
        ]

        points_evaluated = []

        for side in sides:
            for side_point in side.intermediary_points():
                ray = Edge(origin=centre, termination=side_point)
                for point in ray.intermediary_points():
                    if point not in points_evaluated:
                        points_evaluated.append(point)
                    else:
                        pass

                    # Stop traversing the ray if the ray gets blocked
                    # TODO: implement the check
                    # if point in blocked_points: 
                    #     break

                    # Stop traversing the ray if its length exceeds search 
                    # radius
                    if centre.distance_to(point) > self.search_radius_bits:
                        break

                    points_in_search_radius.append(point)

        return points_in_search_radius