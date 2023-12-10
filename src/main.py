from FractalFactory import makeFractal
from PaletteFactory import makePalette
from FractalParser import parseFractal
from ImagePainter import ImagePainter
from FractalFactory import defaultFrac
import sys
from pathlib import Path


def main():
    if len(sys.argv) > 1:
        fractal_info = parseFractal(sys.argv[1])
        fractal_name = Path(sys.argv[1]).stem

    else:
        fractal_info = defaultFrac
        fractal_name = "default"
    if len(sys.argv) > 2:
        palette_name = sys.argv[2]
    else:
        palette_name = None


    # Instantiate factories
    fractal = makeFractal(fractal_info)
    palette = makePalette(fractal_info, palette_name)

    image_painter = ImagePainter(fractal, palette, fractal_info, fractal_name)

    image_painter.paint()



if __name__ == "__main__":
    main()

