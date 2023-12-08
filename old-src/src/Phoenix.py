def phoenix_iteration_count(z, size):
    """
        Return the iteration count of the current complex number
        within the Phoenix fractal in the palette array
    """
    # Julia Constant
    c = complex(0.5667, 0.0)

    # Phoenix Constant
    phoenix = complex(-0.5, 0.0)

    # Initialize variables
    z = complex(z.imag, z.real)
    z_prev = 0 + 0j

    # Loop over the range of colors in the palette
    for i in range(size):
        z_save = z
        z = z * z + c + (phoenix * z_prev)
        if abs(z) > 2:
            return i
        z_prev = z_save  # Set the prevZ value for the next iteration
    return size - 1
