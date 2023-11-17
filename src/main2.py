import sys
import FractalInformation as Dict
import ImagePainter

if len(sys.argv) < 2:
    pass
if sys.argv[1] not in Dict.fractals:
    pass

# Take dict info and pass it into method from imagepainter.