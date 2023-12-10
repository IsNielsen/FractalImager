"""
couresy of Chatgpt
"""
class BurningShipFractal:
    def __init__(self, fractal_info):
        self.iterations = fractal_info["iterations"]
        self.pixels = fractal_info["pixels"]

    def count(self, c):
        """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Burning Ship fractal set.
        """
        z = complex(0, 0)
        for i in range(self.iterations - 1, -1, -1):
            z = complex(abs(z.real), abs(z.imag))**2 - c
            if abs(z) > 2.0:
                return i
        return 0
