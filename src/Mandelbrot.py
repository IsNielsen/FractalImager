def mandelbrot_iteration_count(complex, size):
    z = 0

    for iter in range(size):
        z = z * z + complex
        if abs(z) > 2:
            return iter
    return iter