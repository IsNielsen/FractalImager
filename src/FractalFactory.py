from Phoenix import PhoenixFractal
from Mandelbrot import MandelbrotFractal
from MandelbrotCubed import MandelbrotCubed


def makeFractal(fractal_info):
    if fractal_info is None:
        return MandelbrotFractal(defaultFrac)

    if fractal_info["type"] == "phoenix":

        return PhoenixFractal(fractal_info)

    if fractal_info["type"] == "mandelbrot":
        return MandelbrotFractal(fractal_info)

    if fractal_info["type"] == "mandelbrot3":
        return MandelbrotCubed(fractal_info)


defaultFrac = {
    'type': 'mandelbrot',
    'pixels': 256,
    'centerx': 0.0,
    'centery': 0.0,
    'axislength': 3.0,
    'iterations': 256
}
