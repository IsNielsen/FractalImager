import unittest
from Reverse import ReversePalette
from pastels import Pastels
from blackandwhite import BlackAndWhite

class TestPalettes(unittest.TestCase):
    """
    These tests are to make sure that the created palettes will never get an
    out of index error. When an iteration count is passes into the palette,
    the palette needs to output a palette with a length greater than or equal to
    the iteration.
    """

    def test_reverse_palette(self):
        iterations = 10
        reverse_palette = ReversePalette(iterations)
        self.assertGreaterEqual(len(reverse_palette.firstpal), iterations // 2)
        self.assertGreaterEqual(len(reverse_palette.secondpal), iterations // 2)

    def test_pastels_palette(self):
        iterations = 15
        pastels_palette = Pastels(iterations)
        self.assertGreaterEqual(len(pastels_palette.palette), iterations)

    def test_black_and_white_palette(self):
        iterations = 8
        bw_palette = BlackAndWhite(iterations)
        self.assertGreaterEqual(len(bw_palette.palette), iterations)


if __name__ == '__main__':
    unittest.main()
