from __future__ import annotations
from functools import cached_property
from typing import List
import struct

from map.bitmap.colour_table import ColourTableEntry

class BitMap:
    """Type enabling the reading of basic (e.g. 1-bpp) bitmap images."""
    def __init__(self, image_file_path: str):
        self.image_file_path = image_file_path

        with open(image_file_path, 'rb') as bmp:
            self.raw = bmp.read()

        self.dib_header_start = 14

    @cached_property
    def bmp_header(self) -> bytes:
        """Return the bitmap header (exactly 14 bytes)."""
        return self.raw[:14]

    @cached_property
    def image_data_offset(self) -> int:
        """Return the starting starting address (offset) of image data."""
        return int.from_bytes(self.bmp_header[-4:], byteorder='little')

    @cached_property
    def dib_header_size_bytes(self) -> int:
        """Return the DIB header size (specified in bytes 14-18)."""
        return int.from_bytes(self.raw[14:18], byteorder='little')

    @cached_property
    def dib_header_end(self) -> int:
        return self.dib_header_start + self.dib_header_size_bytes

    @cached_property
    def dib_header(self) -> bytes:
        """Return the DIB header (starting at byte 14; variable length."""
        # DIB header starts at byte 14; length is in dib_header_size_bytes."""
        return self.raw[self.dib_header_start:self.dib_header_end]

    @cached_property
    def n_colours_in_palette(self) -> int:
        """Return the number of colours in the palette from DIB header."""
        return int.from_bytes(self.dib_header[32:36], byteorder='little')

    @cached_property
    def colour_table(self):
        """Return a list of entries from the colour table."""
        output = []

        # Colour table bytes are between the end of the DIB header and the start 
        # of the pixel data
        colour_table_bytes = self.raw[
            self.dib_header_end:self.image_data_offset
        ]

        # The number of entries in the table should be specified in the DIB 
        # header (e.g. n_colours_in_palette); each colour in the table will 
        # have a four bytes entry (b,g,r,padding)
        for colour in range(self.n_colours_in_palette):
            output.append(
                ColourTableEntry(colour_table_bytes[colour*4:(colour+1)*4])
            )

        return output

    @cached_property
    def file_header(self) -> str:
        """The BMP header."""
        # The first two bytes of the file
        return self.bmp_header[:2].decode()

    @cached_property
    def file_size_in_bytes(self) -> int:
        """Return the total file size, in bytes."""
        return int.from_bytes(self.bmp_header[2:4], byteorder='little')

    @cached_property
    def image_width_px(self) -> int:
        """Return the width of the image in pixels."""
        return int.from_bytes(self.dib_header[4:8], byteorder='little')

    @cached_property
    def image_height_px(self) -> int:
        """Return the height of the image in pixels."""
        return int.from_bytes(self.dib_header[8:12], byteorder='little')

    @cached_property
    def bits_per_pixel(self) -> int:
        """Return the number of bits used to per pixel in the pixel array."""
        return int.from_bytes(self.dib_header[14:16], byteorder='little')

    @cached_property
    def n_colours_in_palette(self) -> int:
        """Return the total number of colours in the image (and colour table)."""
        return int.from_bytes(self.dib_header[32:36], byteorder='little')

    def get_pixel_array(self) -> list:
        """"""
        pixel_array_bytes = self.raw[
            self.image_data_offset:self.image_data_offset+self.image_width_px
        ]

        return pixel_array_bytes