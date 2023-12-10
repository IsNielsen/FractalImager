from Phoenix import PhoenixFractal
from Mandelbrot import MandelbrotFractal
from MandelbrotCubed import MandelbrotCubed
from burningship import BurningShipFractal


def makeFractal(fractal_info):
    if fractal_info["type"] == "default":
        print("FractalFactory: Creating default fractal")
        return MandelbrotFractal(defaultFrac)

    if fractal_info["type"] == "phoenix":

        return PhoenixFractal(fractal_info)

    if fractal_info["type"] == "mandelbrot":
        return MandelbrotFractal(fractal_info)

    if fractal_info["type"] == "mandelbrot3":
        return MandelbrotCubed(fractal_info)

    if fractal_info["type"] == "burningship":
        return BurningShipFractal(fractal_info)

defaultFrac = {
    'type': 'default',
    'pixels': 640,
    'centerx': 0.0,
    'centery': 0.0,
    'axislength': 3.0,
    'iterations': 512
}

# defaultFrac = {
#     'type': 'mandelbrot',
#     'pixels': 640,
#     'centerx': 0.0,
#     'centery': 0.0,
#     'axislength': 3.0,
#     'iterations': 512
# }
# type: mandelbrot
# pixels: 640
# centerx: -1.0
# centery: 0.0
# axislength: 1.0
# iterations: 256
