from point import Point
import constants

class SearchMap: 
    def __init__(self, map: int=0):
        self._map = map

    def __str__(self) -> str: 
        """Return a string representation of the map."""
        str_map_val = str(bin(self._map))[2:]
        return str_map_val.rjust(constants.SEARCH_MAP_SIZE**2, "0")

    def reveal(self, point: Point) -> None: 
        """Alter to map to reveal the 'tile' at the given Point position."""
        self._map |= point.binary_grid_value

    def reveal_radius(self, point: Point, radius: float = 0.0) -> None:
        """Reveal a radius around a point."""
        for given_point in point.get_points_in_search_radius(): 
            self.reveal(given_point)

    def show(self) -> None:
        """Iterate through the string map to print to console."""
        for row in range(0, constants.SEARCH_MAP_SIZE): 
            min = row * constants.SEARCH_MAP_SIZE
            max = min + constants.SEARCH_MAP_SIZE
            print(self.str_map[min:max])