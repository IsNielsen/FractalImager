def phoenix_iteration_count(compNum, size):
    """
        Return the iteration count of the current complex number
        within the Phoenix fractal in the palette array
    """
    # Constants
    c = complex(0.5667, 0.0)
    phoenix = complex(-0.5, 0.0)

    # Initialize variables
    z_flipped = complex(compNum.imag, compNum.real)
    z_prev = 0 + 0j
    z = z_flipped

    # Loop over the range of colors in the palette
    for i in range(size):
        z, z_prev = z * z + c + (phoenix * z_prev), z  # Update Z and prevZ simultaneously

        # If the absolute value of Z is greater or equal to 2, return the iteration count
        if abs(z) > 2:
            return i  # The sequence is unbounded

    return size - 1  # Else this is a bounded sequence, return the maximum iteration count
