from functools import cached_property

class ColourTableEntry:
    def __init__(self, inbytes):
        """Eentry derived from bytes (4) from a bitmap colour table."""
        self.inbytes = inbytes

    def __str__(self):
        return str(self.rgb)

    @cached_property
    def red(self) -> int:
        """Red value contained in third byte."""
        return int.from_bytes(self.inbytes[2:3], byteorder='little')

    @cached_property
    def green(self) -> int:
        """Green value contained in second byte."""
        return int.from_bytes(self.inbytes[1:2], byteorder='little')

    @cached_property
    def blue(self) -> int:
        """Blue value contained in first byte."""
        return int.from_bytes(self.inbytes[0:1], byteorder='little')

    @cached_property
    def rgb(self) -> tuple:
        """Return red, green, blue as tuple."""
        return (
            self.red, self.green, self.blue
        )

    @cached_property
    def is_white(self) -> bool:
        """Boolean check for table entry indicating white."""
        # return self.rgb == (255, 255, 255)    <- this works; is likely slower
        return self.inbytes == b'\xff\xff\xff\x00' # assumes white == b'\xff\'

    @cached_property
    def is_black(self) -> bool:
        """Boolean check for table entry indicating black."""
        # return self.rgb == (0, 0, 0)          <- this works; is likely slower
        return self.inbytes == b'\x00\x00\x00\x00' # assumes black == b'\x00\'