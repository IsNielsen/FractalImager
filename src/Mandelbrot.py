def mandelbrot_iteration_count(c):
    z = 0
    MAX_ITERATIONS = 115

    for iter in range(MAX_ITERATIONS):
        z = z * z + c
        if abs(z) > 2:
            return iter
    return iter