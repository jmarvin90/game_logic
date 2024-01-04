import pytest

from geometry.polygon import Polygon
from geometry.point import Point

@pytest.fixture
def point_set_with_redundant_points():
    """ 

    0         1         2         3
    x ------- x ------- x ------- x
    |                               \
    |                                \
    |                                 \
    x ----------------- x ------- x -- x
    7, -1               6         5    4

    """
    return (
        Point(1, 5), 
        Point(3, 5), # excluded from output 
        Point(5, 5), # excluded from output
        Point(7, 5),
        Point(9, 1),
        Point(7, 1), # excluded from output
        Point(5, 1), # excluded from output
        Point(1, 1)
    )

@pytest.fixture
def points_for_complex_poly():
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
    return (
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


def test_remove_redundant_points(point_set_with_redundant_points):
    output = Polygon.remove_redundant_points(*point_set_with_redundant_points)
    # TODO: the assertion
    assert len(output) == 4

def test_edges_from_points(point_set_with_redundant_points):
    output = Polygon.edges_from_points(*point_set_with_redundant_points)
    # TODO: make this assertion more specific (e.g. specific edges)
    assert len(output) == 4

def test_covers_point(points_for_complex_poly):
    my_polygon = Polygon()
    my_polygon.edges = my_polygon.edges_from_points(*points_for_complex_poly)

    inside = Point(8, 4)
    outside = Point(12, 5)

    assert (
        my_polygon.covers_point(inside) and
        not my_polygon.covers_point(outside)
    )