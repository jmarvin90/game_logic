import pytest

from src.map.searchmap.searchmap import SearchMap
from src.geometry.point import Point
from src.geometry.edge import Edge

@pytest.fixture
def test_search_map() -> SearchMap:
    return SearchMap(
        map=0, 
        map_height_px=32, 
        map_width_px=128, 
        search_radius_px=7.5,
        scale_factor=1
    )

def test_print_search_map(test_search_map: SearchMap):
    # test_search_map.reveal_radius(Point(0, 0))
    # test_search_map.reveal_radius(Point(512, 64))
    test_search_map.reveal_radius(Point(0, 0))
    # test_search_map.reveal(Point(0, 0))
    # test_search_map.reveal(Point(64, 64))
    # test_search_map.reveal(Point(127, 127))
    print(test_search_map)
    assert False