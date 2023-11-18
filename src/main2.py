import sys
import FractalInformation as fractal_info
from ImagePainter import draw_fractal

if len(sys.argv) != 2:
    print("Please provide the name of a fractal as an argument")
    fractal_info.print_frac_list()
    sys.exit()

fractal_name = sys.argv[1]

if fractal_name not in fractal_info.fractals:
    print(f"ERROR: {fractal_name} is not a valid fractal")
    print("Please choose one of the following:")
    fractal_info.print_frac_list()
    sys.exit()

fractal_data = fractal_info.fractals[fractal_name]
draw_fractal(fractal_data)