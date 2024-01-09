from map.bitmap.bitmap import BitMap
from map.bitmap.colour_table import ColourTableEntry

class MonochromeBitMap(BitMap):
    def __init__(self, image_file_path: str):
        super().__init__(image_file_path)

    def query_pixel_colour(self, x: int, y: int) -> ColourTableEntry:
        """Return a colour table entry for a specified pixel."""
        # Create a bitmask to fetch the bit for the pixel; then return the 
        # colour table entry for the bit value
        target_byte_index = x // 8
        target_row_index = y
        target_bit_position =  x % 8
        query_bitmask = 128 >> target_bit_position

        # The byte containing our pixel ([y, x])
        byte = self.get_pixel_array()[target_row_index][target_byte_index]

        # Moves the single set bit to the 'first' position
        # bit = (byte & query_bitmask) >> (7 - target_bit_position)
        
        # Achieves the same as above, though possibly more simply
        bit = 1 if byte & query_bitmask else 0

        # The colour table entry for the bit value
        return self.colour_table[bit]

        


