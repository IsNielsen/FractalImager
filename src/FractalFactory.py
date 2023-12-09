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
    'pixels': 640,
    'axislength': 4.0,
    'iterations': 100,
    'min': {
        'x': -2.0,
        'y': -2.0
    },
    'max': {
        'x': 2.0,
        'y': 2.0
    },
    'pixelsize': 0.00625,
    'imagename': 'mandelbrot.png'
}
