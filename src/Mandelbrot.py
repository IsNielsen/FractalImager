def mandelbrot_iteration_count(complex, size):
    z = 0

    for i in range(size):
        z = z * z + complex
        if abs(z) > 2:
            return i
    return i