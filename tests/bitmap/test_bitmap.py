import pytest

from src.map.bitmap.bitmap import BitMap
from src.map.bitmap.monochrome_bitmap import MonochromeBitMap

@pytest.fixture
def monochrome_bitmap():
    return MonochromeBitMap(
        image_file_path='tests/bitmap/test_files/1bpp-321x240.bmp'
    )

@pytest.fixture
def colour_bitmap():
    return BitMap(
        image_file_path='tests/bitmap/test_files/bmp_24.bmp'
    )

def test_bmp_header(monochrome_bitmap):
    assert monochrome_bitmap.file_header == "BM"

def test_bits_per_pixel(monochrome_bitmap):
    assert monochrome_bitmap.bits_per_pixel == 1

def test_n_colours_in_palette(monochrome_bitmap):
    assert monochrome_bitmap.n_colours_in_palette == 2

def test_monochrome_colour_table(monochrome_bitmap):
    assert (
        monochrome_bitmap.colour_table[0].is_black and
        monochrome_bitmap.colour_table[1].is_white
    )

def test_get_image_data_row_width(monochrome_bitmap):
    assert monochrome_bitmap.image_data_row_width_bytes == 44

def test_get_image_data_padding_bits(monochrome_bitmap):
    assert monochrome_bitmap.image_data_row_padding_bits == 31

def test_query_pixel_colour(monochrome_bitmap):

    # All these pixels should be white (the vertical in the 'T')
    whites = [
        monochrome_bitmap.query_pixel_colour(8, i).is_white for i in range(4, 10)
    ]

    # All these pixels should be black (the horizontal at the top of the image)
    blacks = [
        monochrome_bitmap.query_pixel_colour(i, 0).is_black for i in range(0, 10)
    ]

    # If we're right about all the pixels, the test will pass
    assert all([*whites, *blacks])