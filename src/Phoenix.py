class PhoenixFractal:
    def __init__(self, fractal_info):
        # Julia Constant
        if "creal" not in fractal_info:
            raise NotImplementedError("Missing 'creal' parameter in .frac file")
        if "cimag" not in fractal_info:
            raise NotImplementedError("Missing 'cimag' parameter in .frac file")
        self.c = complex(fractal_info["creal"], fractal_info["cimag"])

        # Phoenix Constant
        if "preal" not in fractal_info:
            raise NotImplementedError("Missing 'preal' parameter in .frac file")
        if "pimag" not in fractal_info:
            raise NotImplementedError("Missing 'pimag' parameter in .frac file")

        self.phoenix = complex(fractal_info["preal"], fractal_info["pimag"])

        # Other fractal info
        self.center = complex(fractal_info["centery"], fractal_info["centery"])
        self.axis_length = fractal_info["axislength"]
        self.pixels = fractal_info["pixels"]
        self.iterations = fractal_info["iterations"]

        self.z = 0 + 0j

    def count(self, z):
        """
        Return the iteration count of the current complex number
        within the Phoenix fractal in the palette array
        """

        z = (z - self.center) / (self.axis_length / 2)
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
