import unittest
from Palette import phoenixPalette
from Palette import mandelbrotPalette
from Palette import give_color, give_size

class TestPalette(unittest.TestCase):

    def test_give_color_mandelbrot(self):
        color = give_color('M', 5)
        self.assertEqual(color, '#DBDE98')

    def test_give_color_phoenix(self):
        color = give_color('P', 9)
        self.assertEqual(color, '#fff699')

    def test_give_color_invalid_palette(self):
        with self.assertRaises(ValueError):
            give_color('InvalidPalette', 0)

    def test_give_size_mandelbrot(self):
        size = give_size('M')
        self.assertEqual(size, len(mandelbrotPalette))

    def test_give_size_phoenix(self):
        size = give_size('P')
        self.assertEqual(size, len(phoenixPalette))

    def test_give_size_invalid_palette(self):
        with self.assertRaises(ValueError):
            give_size('InvalidPalette')

if __name__ == '__main__':
    unittest.main()