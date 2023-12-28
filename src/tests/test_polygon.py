from geometry.polygon import Polygon
from geometry.point import Point

class TestPolygon:
    def test_edges_from_points(self):
        output = Polygon.edges_from_points(
            Point(1, 1), 
            Point(1, 3), 
            Point(1, 5), 
            Point(5, 5), 
            Point(5, 1)
        )

        for item in output:
            print(item)
        assert False