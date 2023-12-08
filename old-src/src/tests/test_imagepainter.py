import unittest
from ImagePainter import draw_fractal, fractals_color, status_bar

class TestImagePainter(unittest.TestCase):
    def test_status_bar(self):
        """Progress bar produces correct output"""
        self.assertEqual(status_bar(1, 600), '[100% =================================]')
        self.assertEqual(status_bar(7, 7), '[  0%                                  ]')
        self.assertEqual(status_bar(150, 300), '[ 50% =================                ]')
        self.assertEqual(status_bar(256, 512), '[ 50% =================                ]')
        self.assertEqual(status_bar(600, 500), '[-20%                                        ]')
        self.assertEqual(status_bar(666, 1000), '[ 33% ===========                      ]')


if __name__ == '__main__':
    unittest.main()
