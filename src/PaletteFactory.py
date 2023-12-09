from Reverse import ReversePalette
from primarytoblack import PrimaryToBlack


def makePalette(itercount, name="primary"):
    if name is not implemented:
        raise NotImplementedError(f"The palette {name} has not been defined")
    # for whatever palette is requested
    if name == "reverse":
        return ReversePalette(itercount)
    if name == "primary":
        return PrimaryToBlack(itercount)

    # Default
    # return PrimaryToBlack(itercount)
