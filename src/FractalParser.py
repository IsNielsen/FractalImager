def parseFractal(file_path):
    fractal_info = {}

    file = open(file_path, 'r')
    for line in file:
        # Continue to next line if a comment or blankline
        if line.startswith('#') or not line:
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

        if key in ["centerx", "centery", "axisLength"]:
            fractal_info[key] = safe_convert(fractal_info[key], float)
        if key in ["pixels", "iterations"]:
            fractal_info[key] = safe_convert(fractal_info[key], int)


def safe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' without crashing.

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or None if the conversion is not possible
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None
