import pytest

from geometry.point import Point
from geometry.edge import Edge

class TestEdge:
    def test_y_intercept(self):
        point_a = Point(1, 2)
        point_b = Point(2, 4)
        point_c = Point(500, 1000)

        control = Point(500, 999)

        short_edge = Edge(point_a, point_b)
        mid_edge = Edge(point_a, point_c)
        control_edge = Edge(point_a, control)

        assert (
            short_edge.y_intercept == mid_edge.y_intercept == 0 and
            short_edge.y_intercept != control_edge.y_intercept
        )

    def test_diag_distance(self):
        """"""
        point_a = Point(1, 1)
        point_b = Point(3, 3)
        assert Edge(point_a, point_b).diagonal_distance == 2

    def test_length(self):
        """"""
        point_a = Point(5, 5)
        point_b = Point(3, 3)
        assert Edge(point_a, point_b).length == pytest.approx(2.82842712474619)

    def test_is_vertical(self):
        """"""
        point_a = Point(1, 1)
        point_b = Point(1, 1_000)
        point_c = Point(2, 1_000)

        vertical = Edge(point_a, point_b)
        nearly_vertical = Edge(point_a, point_c)

        assert (
            vertical.is_vertical and not
            nearly_vertical.is_vertical
        )

    def test_is_horizontal(self):
        """"""
        point_a = Point(1, 1)
        point_b = Point(1_000, 1)
        point_c = Point(1_000, 2)

        horizontal = Edge(point_a, point_b)
        nearly_horizontal = Edge(point_a, point_c)

        assert (
            horizontal.is_horizontal and not
            nearly_horizontal.is_horizontal
        )

    def test_gradient(self):
        """"""
        point_a = Point(1, 1)
        point_b = Point(5, 5)
        point_c = Point(900, 900)
        point_d = Point(900, 901)

        short_edge = Edge(point_a, point_b)
        long_edge = Edge(point_a, point_c)
        skewed_edge = Edge(point_a, point_d)

        assert (
            short_edge.gradient == 1 and
            short_edge.gradient == long_edge.gradient and
            long_edge.gradient != skewed_edge.gradient
        )

    def test_centre(self):
        """"""
        point_a = Point(0, 0)
        point_b = Point(100, 100)
        my_edge = Edge(point_a, point_b)
        output = my_edge.centre
        assert output == Point(50, 50)

    def test_parallel(self):
        """"""
        point_a = Point(5, 5)
        point_b = Point(995, 995)

        point_c = Point(994, 994)
        point_d = Point(1_094, 1_094)

        point_e = Point(1_094, 1_095)

        edge_a = Edge(point_a, point_b)
        edge_b = Edge(point_c, point_d)
        skewed_edge = Edge(point_c, point_e)

        assert(
            edge_a.is_parallel_to(edge_b) and not
            edge_a.is_parallel_to(skewed_edge)
        )

    def test_contains(self):
        point_a = Point(1, 1)
        point_b = Point(3, 3)
        edge = Edge(point_a, point_b)
        control = Point(5, 5)

        assert (
            point_a in edge and 
            point_b in edge and 
            control not in edge
        )

    def test_equals(self):
        point_a = Point(1, 1)
        point_b = Point(3, 3)
        point_c = Point(5, 5)

        edge_1 = Edge(point_a, point_b)
        edge_2 = Edge(point_b, point_a)
        control = Edge(point_a, point_c)

        assert (
            edge_1 == edge_2 and
            not edge_1 == control
        )

    def test_interpolate(self):
        """"""
        # TODO: write this test
        assert True

    def test_intermediary_points(self):
        """"""
        # TODO: write this test
        assert True

    def test_orientation(self):
        """Check clockwise, counter-clock, vertical."""
        point_a = Point(5, 5)
        point_b = Point(5, 10)

        point_l = Point(1, 10)
        point_r = Point(10, 10)
        point_t = Point(5, 15)

        assert (
            Edge.orientation(point_a, point_b, point_l) == -1 and
            Edge.orientation(point_a, point_b, point_r) == 1 and
            Edge.orientation(point_a, point_b, point_t) == 0
        )

    def test_intersects(self):
        """"""
        point_a = Point(1, 1)
        point_b = Point(5, 5)

        point_c = Point(5, 1)
        point_d = Point(1, 5)

        point_e = Point(2, 2)
        point_f = Point(6, 6)

        edge_1 = Edge(point_a, point_b)
        edge_2 = Edge(point_c, point_d)
        edge_3 = Edge(point_e, point_f)

        assert(
            edge_1.intersects(edge_2) and
            not edge_1.intersects(edge_3)
        )

    def test_points_are_collinear(self):
        """Test collinearity check."""
        point_a = Point(1, 1)
        point_b = Point(5, 2)
        point_c = Point(9, 3)
        point_d = Point(13, 4)

        control = Point(4, 14)

        assert (
            Edge.points_are_collinear(point_a, point_b, point_c, point_d) and 
            not Edge.points_are_collinear(point_a, point_b, point_c, control)
        )
        