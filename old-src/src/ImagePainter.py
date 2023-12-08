import sys
from time import time
from Palette import give_color, give_size
from Mandelbrot import mandelbrot_iteration_count
from Phoenix import phoenix_iteration_count
from tkinter import Tk, Canvas, PhotoImage, mainloop


def draw_fractal(frac_name, frac_data, size):
    window = Tk()
    tkImage = PhotoImage(width=size, height=size)

    # Extract data from the fractal_data dictionary
    min_x = frac_data['centerX'] - (frac_data['axisLen'] / 2.0)
    min_y = frac_data['centerY'] - (frac_data['axisLen'] / 2.0)
    max_x = frac_data['centerX'] + (frac_data['axisLen'] / 2.0)

    pixel_size = abs(max_x - min_x) / size

    canvas = Canvas(window, width=size, height=size, bg='#000000')
    canvas.pack()
    canvas.create_image((size/2, size/2), image=tkImage, state="normal")

    print("Rendering %s fractal" % frac_name, file=sys.stderr)
    start = time()

    for row in range(size, 0, -1):
        colors = []
        for col in range(size):
            x = min_x + col * pixel_size
            y = min_y + row * pixel_size

            color = fractals_color(complex(x, y), frac_data['fractalType'])
            colors.append(color)

        tkImage.put('{' + ' '.join(colors) + '}', (0, size - row))
        window.update()
        print(status_bar(row, size), end="\r", file=sys.stderr)


    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    tkImage.write(f"{frac_name}.png")
    print("Saved image to file " + frac_name + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()


def fractals_color(complexNum, fractype):
    if fractype == 'mandelbrot':
        i = mandelbrot_iteration_count(complexNum, give_size('M'))
        return give_color('M', i)

    if fractype == 'phoenix':
        i = phoenix_iteration_count(complexNum, give_size('P'))
        return give_color('P', i)


def status_bar(rows_left, size):
    # Print a status bar on the console
    frac_done = (size - rows_left) / size
    bar_len = 34
    total_len = int(bar_len * frac_done)
    remain_len = bar_len - total_len - 1

    return f"[{frac_done * 100:3.0f}% {'=' * total_len}{' ' * remain_len}]"
