import pytest

from geometry.point import Point
from geometry.edge import Edge

class TestEdge:
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

    def test_interpolate(self):
        """"""
        # TODO - write this test
        assert True

    def test_intermediary_points(self):
        """"""
        # TODO - write this test
        assert True

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
            edge_1.intersects(edge_2) and not
            edge_1.intersects(edge_3)
        )



    

    