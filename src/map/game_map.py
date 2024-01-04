from typing import List
import struct

class GameMap:
    def __init__(self, map_path: str):
        self.map_path = map_path

    def get_pixel_array(self) -> List[int]:
        pass

with open('src/map/bmp_24.bmp', 'rb') as bmp:
    print(bmp.read(2).decode())
    print(bmp.read(4).decode())
    # print('Type:', bmp.read(2).decode())
    # print('Size: %s' % struct.unpack('I', bmp.read(4)))
    # print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
    # print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
    # print('Offset: %s' % struct.unpack('I', bmp.read(4)))

    # print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
    # print('Width: %s' % struct.unpack('I', bmp.read(4)))
    # print('Height: %s' % struct.unpack('I', bmp.read(4)))
    # print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
    # print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
    # print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
    # print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
    # print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
    # print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
    # print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
    # print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))