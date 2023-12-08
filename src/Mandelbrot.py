class MandelbrotFractal:
    def __init__(self, fractal_info):

        # Other fractal info
        self.center = complex(fractal_info["centery"], fractal_info["centery"])
        self.axis_length = fractal_info["axislength"]
        self.pixels = fractal_info["pixels"]
        self.iterations = fractal_info["iterations"]

    def count(self, c):
        """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Mandelbrot set (bounded by `end`)
        """
        z = self.center  # z0
        for i in range(self.iterations):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i
        return self.iterations - 1
