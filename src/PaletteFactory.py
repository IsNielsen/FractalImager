from Reverse import ReversePalette
from pastels import Pastels


def makePalette(fractal_info, name):
    # if name is not implemented:
    #     raise NotImplementedError(f"Invalid palette requested")

    # for whatever palette is requested
    if name == "reverse":
        return ReversePalette(fractal_info["iterations"])
    if name == "primary":
        return Pastels(fractal_info["iterations"])
    if name is None:
        print("PaletteFactory: Creating default color palette")
        return Pastels(fractal_info["iterations"])

    # Else: invalid palette
    raise NotImplementedError(f"Invalid palette requested")

