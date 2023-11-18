def phoenix_iteration_count(c):
    z = complex(0, 0)
    MAX_ITERATIONS = 102

    for iter in range(MAX_ITERATIONS):
        z = z * z + c
        if abs(z) > 2:
            return iter
    return iter
