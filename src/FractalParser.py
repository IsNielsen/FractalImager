from SafeConvert import safe_convert
def parseFractal(file_path):
    fractal_info = {}

    file = open(file_path, 'r')
    for line in file:
        # Continue to next line if a comment or blankline
        if line.startswith('#') or not line.strip():
            continue

        line = line.lower()
        try:
            key, val = line.split(":", 1)
        except ValueError:
            raise RuntimeError(f"Can't process line: {line}")

        fractal_info[key.strip()] = val.strip()

    testFractalInfo(fractal_info)

    return fractal_info

def testFractalInfo(fractal_info):
    required = ['type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations']
    for key in required:
        if key not in fractal_info:
            raise RuntimeError(f"Missing key: {key}")

        if key in ["centerx", "centery", "axislength"]:
            fractal_info[key] = safe_convert(fractal_info[key], float)
        if key in ["pixels", "iterations"]:
            fractal_info[key] = safe_convert(fractal_info[key], int)




