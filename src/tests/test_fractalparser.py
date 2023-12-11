import unittest
from unittest.mock import patch
from FractalParser import parseFractal, testFractalInfo, safe_convert

class TestFractalParser(unittest.TestCase):
    def test_parseFractal(self):
        test = parseFractal("tests/mandelbrot_test.frac")

        self.assertIsInstance(test, dict)
        self.assertEqual(len(test), 6)
        self.assertEqual(test['type'], 'mandelbrot')
        self.assertEqual(test['pixels'], 640)
        self.assertEqual(test['centerx'], 0.0)
        self.assertEqual(test['centery'], 0.0)
        self.assertEqual(test['axislength'], 4.0)
        self.assertEqual(test['iterations'], 100)
    def test_parseFractal_invalid_frac(self):
        with self.assertRaises(RuntimeError):
            parseFractal("tests/invalid_test.frac")
    def test_parseFractal_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            parseFractal("tests/non_existant_test.frac")
    def test_testFractalInfo(self):
        test = {
            'type': 'default',
            'pixels': 640,
            'centerx': 0.0,
            'centery': 0.0,
            'axislength': 3.0,
            'iterations': 512
        }
        testFractalInfo(test)

    def test_testFractalInfo_missing_key(self):
        test = {
            'pixels': 640,
            'centerx': 0.0,
            'centery': 0.0,
            'axislength': 3.0,
            'iterations': 512
        }
        with self.assertRaises(RuntimeError):
            testFractalInfo(test)


if __name__ == '__main__':
    unittest.main()
