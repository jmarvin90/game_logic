from geometry.polygon import Polygon
from geometry.point import Point

class TestPolygon:
    def test_remove_redundant_points(self):
        """Test that this method removes unecessary points."""
        output = Polygon.remove_redundant_points(
            Point(1, 5), 
            Point(3, 5), # excluded from output 
            Point(5, 5), # excluded from output
            Point(7, 5),
            Point(9, 1),
            Point(7, 1), # excluded from output
            Point(5, 1), # excluded from output
            Point(1, 1)
        )

        """ 

        0         1         2         3
        x ------- x ------- x ------- x
        |                               \
        |                                \
        |                                 \
        x ----------------- x ------- x -- x
        7, -1               6         5    4

        """
        
        # TODO: the assertion
        assert len(output) == 4

    def test_edges_from_points(self):
        """Test that the method returns the 'right' edges."""
        my_points = (
            Point(1, 5), 
            Point(3, 5), # excluded from output 
            Point(5, 5), # excluded from output
            Point(7, 5),
            Point(9, 1),
            Point(7, 1), # excluded from output
            Point(5, 1), # excluded from output
            Point(1, 1)
        )

        output = Polygon.edges_from_points(*my_points)

        # TODO - the assertion
        assert True
    
    def test_covers_point(self):
        my_points = (
            Point(1, 5),
            Point(3, 5),
            Point(3, 3),
            Point(7, 3),
            Point(7, 5),
            Point(10, 5),
            Point(10, 3),
            Point(13, 3),
            Point(13, 5),
            Point(16, 5), 
            Point(16, 1), 
            Point(1, 1)
        )

        my_polygon = Polygon()
        my_polygon.edges = my_polygon.edges_from_points(*my_points)

        inside = Point(8, 4)
        outside = Point(12, 5)

        output = (
            my_polygon.covers_point(outside)
        )

        """ 

        0         1         4     5    8   9
        x ------- x         x --- x    x - x
        |         |         |  *  |  # |   |
        |         x ------- x     x -- x   |
        |         2         3     6    7   |
        |                                  |
        x ----------------- x ------- x -- x
        13, -1              12        11   10

        """

        assert (
            my_polygon.covers_point(inside) and
            not my_polygon.covers_point(outside)
        )