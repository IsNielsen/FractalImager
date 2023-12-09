from Reverse import ReversePalette
from primarytoblack import PrimaryToBlack


def makePalette(itercount, name="default"):
    # if name is not implemented:
    #     raise NotImplementedError(f"Invalid palette requested")

    # for whatever palette is requested
    if name == "reverse":
        return ReversePalette(itercount)
    if name == "primary":
        return PrimaryToBlack(itercount)
    if name == "default":
        print("PaletteFactory: Creating default color palette")
        return PrimaryToBlack(itercount)

    # Else: invalid palette
    raise NotImplementedError(f"Invalid palette requested")

