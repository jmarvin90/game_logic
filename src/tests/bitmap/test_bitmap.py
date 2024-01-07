import pytest

from map.bitmap.bitmap import BitMap

@pytest.fixture
def monochrome_bitmap():
    return BitMap(
        image_file_path='src/tests/bitmap/test_files/1bpp-321x240.bmp'
    )

def test_bmp_header(monochrome_bitmap):
    assert monochrome_bitmap.file_header == "BM"

def test_n_colours_in_palette(monochrome_bitmap):
    assert monochrome_bitmap.n_colours_in_palette == 2

def test_colour_table(monochrome_bitmap):
    assert (
        monochrome_bitmap.colour_table[0].is_black == True and
        monochrome_bitmap.colour_table[1].is_white == True
    )