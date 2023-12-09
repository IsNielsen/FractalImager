from FractalFactory import makeFractal
from PaletteFactory import makePalette
from FractalParser import parseFractal
from ImagePainter import ImagePainter
import sys
from FractalFactory import defaultFrac


def main():

    if len(sys.argv) > 1:
        #file = sys.argv[1]
        fractal_info = parseFractal(sys.argv[1])
    else:
        fractal_info = defaultFrac
    if len(sys.argv) > 2:
        palette_name = sys.argv[2]
    else:
        palette_name = None

    # Instantiate factories
    fractal = makeFractal(fractal_info)
    palette = makePalette(fractal_info, palette_name)

    image_painter = ImagePainter(fractal, palette, fractal_info)

    image_painter.paint()

if __name__ == "__main__":
    main()

