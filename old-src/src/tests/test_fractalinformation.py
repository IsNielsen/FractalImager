import unittest
from FractalInformation import print_frac_list, fractals


class TestFractalInformation(unittest.TestCase):
    def test_print_frac_list(self):
        self.assertEqual(print_frac_list(), 'mandelbrot\nmandelbrot-zoomed\nspiral0\nspiral1\nseahorse\nelephants'
                                            '\nleaf\nstarfish\nphoenix\npeacock\nmonkey-knife-fight\nshrimp-cocktail\n')


if __name__ == '__main__':
    unittest.main()
