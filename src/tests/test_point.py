import pytest

from geometry.point import Point

@pytest.fixture
def a():
    return Point(2, 2)

@pytest.fixture
def a_dup():
    return Point(2, 2)

@pytest.fixture
def b():
    return Point(5, 5)

@pytest.fixture
def c():
    return Point(7, 7)

# TODO: arrange the tests into a sensible order
# TODO: make sure all the tests have sensible docstrings and comments
# TODO: add necessary fixtures
def test_add(a, b, c):
    assert a + b == c

def test_sub(a, b, c):
    assert c - b == a

def test_eq(a, a_dup, b):
    assert a == a_dup and a != b

def test_scaled():
    # TODO: write this test
    assert True

def test_inverse():
    # TODO: write this test
    assert True

def test_binary_index():
    # TODO: write this test
    assert True

def test_binary_grid():
    # TODO: write this test
    assert True

def test_distanct_to(a, c):
    assert a.distance_to(c) == pytest.approx(7.0710678118654755)

def test_points_in_rad():
    # TODO: write this test
    assert True

def test_is_in_bounds():
    # TODO: write this test
    assert True