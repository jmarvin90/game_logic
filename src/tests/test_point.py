import pytest

from geometry.point import Point

class TestPoint:
    def test_add(self):
        """Adding two points together.

        A + B = C, where A.x + B.x == C.x, etc.
        """
        point_a = Point(3, 3)
        point_b = Point(5, 5)
        control = Point(8, 8)
        assert point_a + point_b == control

    def test_sub(self):
        """Subtracting two points."""
        point_a = Point(5, 5)
        point_b = Point(3, 3)
        control = Point(2, 2)
        assert point_a - point_b == control

    def test_eq(self):
        """Checking equality for points with same coordinates."""
        point_a = Point(3, 3)
        point_b = Point(3, 3)
        point_c = Point(7, 7)
        assert point_a == point_b and point_a != point_c

    def test_cross(self):
        """Cross product."""
        # TODO - write this test
        assert True

    def test_scaled(self):
        """Scaled."""
        # TODO - write this test
        assert True

    def test_inverse(self):
        """Scaled."""
        # TODO - write this test
        assert True

    def test_orientation(self):
        """Check clockwise, counter-clock, vertical."""
        point_a = Point(5, 5)
        point_b = Point(5, 10)

        point_l = Point(1, 10)
        point_r = Point(10, 10)
        point_t = Point(5, 15)

        assert (
            Point.orientation(point_a, point_b, point_l) == -1 and
            Point.orientation(point_a, point_b, point_r) == 1 and
            Point.orientation(point_a, point_b, point_t) == 0
        )

    def test_binary_index(self):
        """Binary index."""
        # TODO - write this test
        assert True

    def test_binary_grid(self):
        """Binary grid."""
        # TODO - write this test
        assert True

    def test_distanct_to(self):
        """Distance between two points."""
        point_a = Point(1, 1)
        point_b = Point(3, 3)
        assert point_a.distance_to(point_b) == pytest.approx(2.8284271247461903)
    
    def test_points_in_rad(self):
        """Test for points in radius."""
        # TODO - write this test
        assert True

    def test_is_in_bounds(self):
        """Test if point is in bounds."""
        # TODO - write this test
        assert True

