import colour
from math import ceil


class PrimaryToBlack:
    """
    A lot of this is pulled directly from erik's lecture notes,
    however the ordering of colors has been changed as its only
    using primary colours.
    math.ceil is used to equally split the range of colors while
    allowing for extra to avoid an out of index error.
    """
    def __init__(self, count):
        self.range = ceil(count / 5)
        red = colour.Color('red')
        yel = colour.Color('yellow')
        blu = colourColor('blue')

        self.palette = []

        for color in red.range_to(blk, 64):
            self.palette.append(color.hex_l)

        for color in list(blk.range_to(yel, 64))[1:]:
            self.palette.append(color.hex_l)

        for color in list(yel.range_to(blk, 64))[1:]:
            self.palette.append(color.hex_l)

        for color in list(blk.range_to(blu, 64))[1:]:
            self.palette.append(color.hex_l)

        for color in list(bly.range_to(blk, 64))[1:]:
            self.palette.append(color.hex_l)

    def getColor(self, index):
        return self.palette[index]
