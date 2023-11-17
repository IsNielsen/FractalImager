import Palette
import Mandelbrot
import Phoenix
from tkinter import Tk, Canvas, PhotoImage, mainloop


def draw_fractal(frac_type, fractal_info):
    # Create windo
    # Create canvas
    # Pack canvas
    # print stuff
    # start timer
    if frac_type == 'mandelbrot':
        Mandelbrot.find_iteration(canvas, size)

    if frac_type == 'phoenix':
        Phoenix.find_iteration(canvas, size)

    # end timer and print stuff
    # window.mainloop()

