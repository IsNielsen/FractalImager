def mandelbrot_iteration_count(c, size):
    """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Mandelbrot set (bounded by `end`)
        """
    z = complex(0, 0)  # z0
    for i in range(size):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2.0:
            return i
    return size - 1
