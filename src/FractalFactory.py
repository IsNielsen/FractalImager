from Phoenix import PhoenixFractal
from Mandelbrot import MandelbrotFractal

def makeFractal(fractalInfo):
    if fractalInfo is None:
        return MandelbrotFractal(defaultFrac)
    if fractalInfo["type"] is "phoenix":
        return PhoenixFractal(fractalInfo)
    if fractalInfo["type"] is "mandelbrot":
        return MandelbrotFractal(fractalInfo)


defaultFrac = {
    'type': 'mandelbrot',
    'pixels': 256,
    'centerx': 0.0,
    'centery': 0.0,
    'axislength': 3.0,
    'iterations': 256
}
