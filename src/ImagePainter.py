from Palette import give_color, palette_size
from Mandelbrot import mandelbrot_iteration_count
from Phoenix import phoenix_iteration_count
from tkinter import Tk, Canvas, PhotoImage, mainloop


def draw_fractal(frac_data):
    window = Tk()

    # Extract data from the fractal_data dictionary
    min_coord = (frac_data['centerX'] - (frac_data['axisLength'] / 2.0),
                 frac_data['centerY'] - (frac_data['axisLength'] / 2.0))
    max_coord = (frac_data['centerX'] + (frac_data['axisLength'] / 2.0),
                 frac_data['centerY'] + (frac_data['axisLength'] / 2.0))

    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=tkPhotoImage, state="normal")

    print("Rendering %s fractal" % i, file=sys.stderr)
    start = time()

    pixel_size = abs(max_coord[0] - min_coord[0]) / 512

    for row in range(512, 0, -1):
        colors = []
        for col in range(512):
            x_coord = min_coord[0] + col * pixel_size
            y_coord = min_coord[1] + row * pixel_size
            colors.append(give_color())

    if frac_type == 'mandelbrot':
        Mandelbrot.find_iteration(x_coord, y_coord, palette_size('M'))

    if frac_type == 'phoenix':
        Phoenix.find_iteration(x_coord, y_coord, palette_size('P'))

    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    frac_image.write(f"{i}.png")
    print("Saved image to file " + i + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

