import sys
from time import time
from Palette import give_color, palette_size
from Mandelbrot import mandelbrot_iteration_count
from Phoenix import phoenix_iteration_count
from tkinter import Tk, Canvas, PhotoImage, mainloop


def draw_fractal(frac_data):
    window = Tk()
    tkImage = PhotoImage(width=512, height=512)

    # Extract data from the fractal_data dictionary
    min_x = frac_data['centerX'] - (frac_data['axisLen'] / 2.0)
    min_y = frac_data['centerY'] - (frac_data['axisLen'] / 2.0)
    max_x = frac_data['centerX'] + (frac_data['axisLen'] / 2.0)
    max_y = frac_data['centerY'] + (frac_data['axisLen'] / 2.0)

    pixel_size = abs(max_x - min_x) / 512

    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=tkImage, state="normal")

    print("Rendering %s fractal" % frac_data['fractalType'], file=sys.stderr)
    start = time()


    for row in range(512, 0, -1):
        colors = []
        for col in range(512):
            x = min_x + col * pixel_size
            y = min_y + row * pixel_size

            color = get_color(complex(x, y), frac_data['fractalType'])
            colors.append(color)

        tkImage.put('{' + ' '.join(colors) + '}', (0, 512 - row))
        window.update()
        status_bar(row, 512)



    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    tkImage.write(f"{frac_data['fractalType']}1.png")
    print("Saved image to file " + frac_data['fractalType'] + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()


def get_color(complex, fractype):
    if fractype == 'mandelbrot':
        i = mandelbrot_iteration_count(complex, palette_size('M'))
        return give_color('M', i)

    if fractype == 'phoenix':
        i = phoenix_iteration_count(complex, palette_size('P'))
        return give_color('P', i)

def status_bar(rows, size):
    # Print a status bar on the console
    fraction_done = (size - rows) / size
    print(f"[{'=' * int(34 * fraction_done):<33}]",
          f"{fraction_done:>4.0%}",
          end="\r", file=sys.stderr)
