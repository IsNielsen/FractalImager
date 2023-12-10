from SafeConvert import safe_convert

class PhoenixFractal:
    def __init__(self, fractal_info):
        # check required info
        required = ["cimag", "creal", "pimag", "preal"]
        for key in required:
            if key not in fractal_info:
                raise NotImplementedError(f"Missing key: {key}")
            fractal_info[key] = safe_convert(fractal_info[key], float)
        # Phoenix Constant
        self.phoenix = complex(fractal_info["preal"], fractal_info["pimag"])
        # Julia Constant
        self.c = complex(fractal_info["creal"], fractal_info["cimag"])
        # Other fractal info
        self.center = complex(fractal_info["centery"], fractal_info["centerx"])
        self.axis_length = fractal_info["axislength"]
        self.pixels = fractal_info["pixels"]
        self.iterations = fractal_info["iterations"]

        self.z = 0 + 0j

    def count(self, z):
        """
        Return the iteration count of the current complex number
        within the Phoenix fractal in the palette array
        """

        z = (z - self.center)
        z = complex(z.imag, z.real)
        z_prev = 0 + 0j

        # Loop over the range of palette/iterations
        for i in range(self.iterations):
            z_save = z
            z = z * z + self.c + (self.phoenix * z_prev)
            if abs(z) > 2:
                return i
            z_prev = z_save  # Set the prevZ value for the next iteration
        return self.iterations - 1
