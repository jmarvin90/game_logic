import pytest

from src.geometry.point import Point
from src.geometry.edge import Edge

@pytest.fixture
def short_diagonal_edge():
    return Edge(Point(2, 4), Point(8, 16))

@pytest.fixture
def short_diagonal_edge_duplicate():
    return Edge(Point(2, 4), Point(8, 16))

@pytest.fixture
def short_diagonal_edge_inverted():
    return Edge(Point(8, 16), Point(2, 4))

@pytest.fixture
def short_diagonal_edge_cross():
    return Edge(Point(2, 16), Point(8, 4))

@pytest.fixture
def long_diagonal_edge():
    return Edge(Point(2, 4), Point(500, 1_000))

@pytest.fixture
def long_diagonal_edge_skewed():
    return Edge(Point(2, 4), Point(500, 999))

@pytest.fixture
def vertical_edge():
    return Edge(Point(1, 1), Point(1, 1_000))

@pytest.fixture
def parallel_vertical_edge():
    return Edge(Point(2, 1), Point(2, 1_000))

@pytest.fixture
def vertical_edge_skewed():
    return Edge(Point(1, 1), Point(2, 1_000))

@pytest.fixture
def horizontal_edge():
    return Edge(Point(1, 1), Point(1_000, 1))

@pytest.fixture
def horizontal_edge_skewed():
    return Edge(Point(1, 1), Point(1_000, 2))


# TODO: arrange the tests into a sensible order
def test_y_intercept(
    short_diagonal_edge,
    long_diagonal_edge,
    long_diagonal_edge_skewed
):
    assert (
        short_diagonal_edge.y_intercept == long_diagonal_edge.y_intercept == 0 and
        short_diagonal_edge.y_intercept != long_diagonal_edge_skewed.y_intercept
    )

def test_diag_distance(short_diagonal_edge):
    assert short_diagonal_edge.diagonal_distance == 12

def test_length(short_diagonal_edge):
    assert short_diagonal_edge.length == pytest.approx(13.416407864998739)

def test_is_vertical(vertical_edge, vertical_edge_skewed):
    assert (
        vertical_edge.is_vertical and not
        vertical_edge_skewed.is_vertical
    )

def test_is_horizontal(horizontal_edge, horizontal_edge_skewed):
    assert (
        horizontal_edge.is_horizontal and not
        horizontal_edge_skewed.is_horizontal
    )

def test_gradient(
    short_diagonal_edge,
    long_diagonal_edge,
    long_diagonal_edge_skewed
):
    assert (
        short_diagonal_edge.gradient == 2 and
        short_diagonal_edge.gradient == long_diagonal_edge.gradient and
        long_diagonal_edge.gradient != long_diagonal_edge_skewed.gradient
    )

def test_centre(short_diagonal_edge, short_diagonal_edge_inverted):
    control = Point(5,10)
    print(short_diagonal_edge.centre)
    assert (
        short_diagonal_edge.centre == short_diagonal_edge.centre == control
    )

def test_parallel(
    vertical_edge, 
    parallel_vertical_edge, 
    vertical_edge_skewed
):
    assert(
        vertical_edge.is_parallel_to(parallel_vertical_edge) and 
        not vertical_edge_skewed.is_parallel_to(parallel_vertical_edge)
    )

def test_contains(short_diagonal_edge):
    origin = Point(2, 4)
    termination = Point(8, 16)
    control = Point(2, 1)

    assert (
        origin in short_diagonal_edge and 
        termination in short_diagonal_edge and 
        control not in short_diagonal_edge
    )

def test_equals(
    short_diagonal_edge,
    short_diagonal_edge_duplicate,
    short_diagonal_edge_inverted,
    long_diagonal_edge
):
    assert (
        short_diagonal_edge == short_diagonal_edge_duplicate and
        short_diagonal_edge == short_diagonal_edge_inverted and
        short_diagonal_edge != long_diagonal_edge
    )

def test_interpolate():
    # TODO: write this test
    assert True

def test_intermediary_points():
    # TODO: write this test
    assert True

def test_orientation(
    short_diagonal_edge,
    short_diagonal_edge_cross,
    vertical_edge
):
    assert (
        # Diagonal l->r, then horizontal l
        Edge.orientation(
            short_diagonal_edge.origin, 
            short_diagonal_edge.termination,
            short_diagonal_edge_cross.origin
        ) == -1 and
        # Diagonal l->r, then vertical d
        Edge.orientation(
            short_diagonal_edge.origin, 
            short_diagonal_edge.termination,
            short_diagonal_edge_cross.termination
        ) == 1 and
        # Vertical start to finish
        Edge.orientation(
            vertical_edge.origin, 
            vertical_edge.centre, 
            vertical_edge.termination
        ) == 0
    )

def test_intersects(
    short_diagonal_edge, 
    short_diagonal_edge_cross, 
    vertical_edge
):
    assert(
        short_diagonal_edge.intersects(short_diagonal_edge_cross) and
        not short_diagonal_edge.intersects(vertical_edge)
    )

def test_points_are_collinear(
    short_diagonal_edge,
    long_diagonal_edge,
    long_diagonal_edge_skewed
):
    assert (
        Edge.points_are_collinear(
            short_diagonal_edge.origin, 
            short_diagonal_edge.termination, 
            long_diagonal_edge.termination
        ) and not
        Edge.points_are_collinear(
            short_diagonal_edge.origin,
            short_diagonal_edge.termination,
            long_diagonal_edge_skewed.termination
        )
    )
        