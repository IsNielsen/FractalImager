import colour
from math import ceil


class BlackAndWhite:
    """
    A lot of this is pulled directly from erik's lecture notes,
    however the ordering of colors has been changed as its only
    using primary colours.
    math.ceil is used to equally split the range of colors while
    allowing for extra to avoid an out of index error.
    """
    def __init__(self, count):
        partial_range = ceil(count / 2) +4
        wht = colour.Color('white')
        blk = colour.Color('black')

        self.palette = []

        for color in blk.range_to(wht, partial_range):
            self.palette.append(color.hex_l)

        for color in list(wht.range_to(blk, partial_range))[1:]:
            self.palette.append(color.hex_l)




    def getColor(self, index):
        return self.palette[index]
