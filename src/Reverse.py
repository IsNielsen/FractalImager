import colour
from math import ceil


class ReversePalette:
    def __init__(self, count):
        cya = colour.Color('cyan')
        blu = colour.Color('blue')
        red = colour.Color('red')
        mag = colour.Color('magenta')

        size = ceil(count/2)

        self.firstpal = []
        self.secondpal = []

        for color in red.range_to(mag, size):
            self.firstpal.append(color.hex_l)

        for color in list(blu.range_to(cya, size)):
            self.secondpal.append(color.hex_l)
            