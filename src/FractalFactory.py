from Phoenix import PhoenixFractal
from Mandelbrot import MandelbrotFractal
from SafeConvert import safe_convert


def makeFractal(fractal_info):
    if fractal_info is None:
        return MandelbrotFractal(defaultFrac)

    if fractal_info["type"] == "phoenix":
        required = ["cimag", "creal", "pimag", "preal"]
        for key in required:
            if key not in fractal_info:
                raise RuntimeError(f"Missing key: {key}")
            fractal_info[key] = safe_convert(fractal_info[key], float)
        return PhoenixFractal(fractal_info)

    if fractal_info["type"] == "mandelbrot":
        return MandelbrotFractal(fractal_info)


defaultFrac = {
    'type': 'mandelbrot',
    'pixels': 256,
    'centerx': 0.0,
    'centery': 0.0,
    'axislength': 3.0,
    'iterations': 256
}
