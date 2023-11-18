import sys
import FractalInformation as fractalInfo
from ImagePainter import draw_fractal

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    fractalInfo.print_frac_list()
    sys.exit()

fractal_name = sys.argv[1]

if fractal_name not in fractalInfo.fractals:
    print(f"ERROR: {fractal_name} is not a valid fractal")
    print("Please choose one of the following:")
    fractalInfo.print_frac_list()
    sys.exit()

fractal_data = fractalInfo.fractals[fractal_name]
draw_fractal(fractal_name, fractal_data, 512)
