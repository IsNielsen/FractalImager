import colour
from math import ceil


class Pastels:
    """
    A lot of this is pulled directly from erik's lecture notes,
    however the ordering of colors has been changed as its only
    using primary colours.
    math.ceil is used to equally split the range of colors while
    allowing for extra to avoid an out of index error.
    """
    def __init__(self, count):
        partial_range = ceil(count / 5) + 5
        red = colour.Color('pink')
        yel = colour.Color('yellow')
        blu = colour.Color('blue')
        blk = colour.Color('black')

        self.palette = []

        for color in red.range_to(blk, partial_range):
            self.palette.append(color.hex_l)

        for color in list(blk.range_to(yel, partial_range))[1:]:
            self.palette.append(color.hex_l)

        for color in list(yel.range_to(blk, partial_range))[1:]:
            self.palette.append(color.hex_l)

        for color in list(blk.range_to(blu, partial_range))[1:]:
            self.palette.append(color.hex_l)

        for color in list(blu.range_to(blk, partial_range))[1:]:
            self.palette.append(color.hex_l)


    def getColor(self, index):
        return self.palette[index]
