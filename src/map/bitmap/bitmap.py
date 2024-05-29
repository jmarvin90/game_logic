from __future__ import annotations
from typing import List
from functools import cached_property

from map.bitmap.colour_table import ColourTableEntry

class BitMap:
    """Type enabling the reading of basic (e.g. 1-bpp) bitmap images."""
    def __init__(self, image_file_path: str):
        self.image_file_path = image_file_path

        with open(image_file_path, 'rb') as bmp:
            self.raw = bmp.read()

        # DIB header start position is fixed at 14
        self.dib_header_start = 14

    @cached_property
    def bmp_header(self) -> bytes:
        """Return the bitmap header (exactly 14 bytes)."""
        return self.raw[:self.dib_header_start]

    @cached_property
    def file_header(self) -> str:
        """The BMP header."""
        # The first two bytes of the file / bmp header (same thing)
        return self.bmp_header[:2].decode()

    @cached_property
    def file_size_in_bytes(self) -> int:
        """Return the total file size, in bytes."""
        # Bytes 2-4 of the file / bmp header (same thing)
        return int.from_bytes(self.bmp_header[2:4], byteorder='little')

    @cached_property
    def dib_header_size_bytes(self) -> int:
        """Return the DIB header size (specified in bytes 14-18 of the file)."""
        return int.from_bytes(self.raw[14:18], byteorder='little')

    @cached_property
    def dib_header_end(self) -> int:
        """Return the header end calculated by start byte + size in bytes."""
        return self.dib_header_start + self.dib_header_size_bytes

    @cached_property
    def dib_header(self) -> bytes:
        """Return the DIB header (starting at byte 14; variable length)."""
        # DIB header starts at byte 14; length is in dib_header_size_bytes."""
        return self.raw[self.dib_header_start:self.dib_header_end]

    @cached_property
    def image_data_offset(self) -> int:
        """Return the starting starting address (offset) of image data."""
        # Last four bytes of the BMP header
        return int.from_bytes(self.bmp_header[-4:], byteorder='little')

    @cached_property
    def image_height_px(self) -> int:
        """Return the height of the image in pixels."""
        return int.from_bytes(self.dib_header[8:12], byteorder='little')

    @cached_property
    def image_width_px(self) -> int:
        """Return the width of the image in pixels."""
        return int.from_bytes(self.dib_header[4:8], byteorder='little')

    @cached_property
    def bits_per_pixel(self) -> int:
        """Return the number of bits used to per pixel in the pixel array."""
        return int.from_bytes(self.dib_header[14:16], byteorder='little')

    @cached_property
    def image_data_bits_per_row(self) -> int:
        """Return the length of the rows containing pixel data."""
        return self.bits_per_pixel * self.image_width_px

    @cached_property
    def image_data_row_width_bytes(self) -> int:
        """Return the length of the rows containing pixel data."""
        return int(((self.image_data_bits_per_row + 31) / 32) * 4)

    @cached_property
    def image_data_end(self) -> int:
        """Return the address representing the end of the image data."""
        # There is a row for each pixel in the images' height
        return (
            self.image_data_offset + 
            (self.image_data_row_width_bytes * self.image_height_px)
        )

    @cached_property
    def image_data_row_padding_bits(self) -> int:
        """Return the number of bits for the end-of-row padding."""
        return (
            (self.image_data_row_width_bytes * 8) - 
            self.image_data_bits_per_row
        )

    @cached_property
    def n_colours_in_palette(self) -> int:
        """Return the number of colours in the palette from DIB header."""
        # Found in bytes 32-36 of the dib header (not of the file!)
        return int.from_bytes(self.dib_header[32:36], byteorder='little')

    @cached_property
    def colour_table(self) -> List[ColourTableEntry]:
        """Return a list of entries from the colour table."""

        # Colour table bytes are between the end of the DIB header and the start 
        # of the pixel data
        colour_table_bytes = self.raw[
            self.dib_header_end:self.image_data_offset
        ]

        # The number of entries in the table should be specified in the DIB 
        # header (e.g. n_colours_in_palette); each colour in the table will 
        # have a four bytes entry (b,g,r,padding)
        return [
            ColourTableEntry(
                colour_table_bytes[colour*4:(colour+1)*4]
            ) for colour in range(self.n_colours_in_palette)
        ]

    def get_pixel_array(self) -> List[bytearray]:
        """Return a list of byte arrays representing pixel rows in the image."""
        # TODO: I'm not sure if this is implemented nicely; or whether there's
        # some alternative way to e.g. get a series of bits instead
        pixel_array = []

        # BMP image data is most often stored 'upside down', so we loop the data
        # in reverse - row by row
        for pixel in reversed(range(self.image_height_px)):
            start = (
                self.image_data_offset + (
                    self.image_data_row_width_bytes * pixel
                )
            )

            pixel_array.append(
                self.raw[
                    start:
                    start+self.image_data_row_width_bytes
                ]
            )

        return pixel_array