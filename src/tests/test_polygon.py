from geometry.polygon import Polygon
from geometry.point import Point

class TestPolygon:
    def test_edges_from_points(self):
        output = Polygon.edges_from_points(
            Point(1, 5), 
            Point(3, 5), 
            Point(5, 5), 
            Point(5, 1), 
            Point(1, 1)
        )

        assert False