import sys
from time import time
from Palette import give_color, palette_size
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

            color = get_color(complex(x, y), frac_data['fractalType'])
            colors.append(color)

        tkImage.put('{' + ' '.join(colors) + '}', (0, size - row))
        window.update()
        status_bar(row, size)

    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    tkImage.write(f"{frac_name}.png")
    print("Saved image to file " + frac_name + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()


def get_color(complexNum, fractype):
    if fractype == 'mandelbrot':
        i = mandelbrot_iteration_count(complexNum, palette_size('M'))
        return give_color('M', i)

    if fractype == 'phoenix':
        i = phoenix_iteration_count(complexNum, palette_size('P'))
        return give_color('P', i)

def status_bar(rows, size):
    # Print a status bar on the console
    fraction_done = (size - rows) / size
    print(f"[{'=' * int(34 * fraction_done):<33}]",
          f"{fraction_done:>4.0%}",
          end="\r", file=sys.stderr)
