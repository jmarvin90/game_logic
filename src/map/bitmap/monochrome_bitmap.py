from src.map.bitmap.bitmap import BitMap
from src.map.bitmap.colour_table import ColourTableEntry

class MonochromeBitMap(BitMap):

    def query_pixel_value(self, x: int, y: int) -> int:
        # Identify where our pixel will be in the image data
        target_byte_index = x // 8
        target_bit_position =  x % 8

        # Create a bitmask based on the target bit position
        query_bitmask = 128 >> target_bit_position

        # Fetch the byte containing our pixel ([y, x])
        byte = self.get_pixel_array()[y][target_byte_index]

        # Moves the single set bit to the 'first' position
        # bit = (byte & query_bitmask) >> (7 - target_bit_position)
        
        # Achieves the same as above, though possibly more simply
        bit = 1 if byte & query_bitmask else 0

        return bit

    
    def query_pixel_colour(self, x: int, y: int) -> ColourTableEntry:
        """Return a colour table entry for a specified pixel."""
        bit_value = self.query_pixel_value(x, y)

        # The colour table entry for the bit value
        return self.colour_table[bit_value]

        


