#!/usr/bin/env python3
# Mandelbrot Set Visualizer

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import sys
from time import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh

# These are the imports that I usually import
import turtle
import os
import os.path
import sys
import math




# This color palette contains 100 color steps.
palette = ['#E1D89F', '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',
           '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',
           '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',
           '#ACD788', '#A8D786', '#A4D685', '#A0D684', '#9CD582', '#98D481',
           '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',
           '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',
           '#71CD85', '#70CC87', '#6ECB8A', '#6DCB8C', '#6CCA8F', '#6BCA91',
           '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',
           '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',
           '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',
           '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',
           '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',
           '#4876B4', '#4771B2', '#476CB1', '#4668AF', '#4663AE', '#465EAC',
           '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',
           '#4543A2', '#4843A1', '#4B429F', '#4E429E', '#51419C', '#54419B',
           '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94', '#633F92',
           '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B', '#6F3C8A',
           '#713C88', '#733B87', '#753B85', '#763A84', '#783A83', '#793981',
           '#7A3980', '#7C387E', '#7D387D']


MAX_ITERATIONS = 115
z = 0
seven = 7.0
TWO = 2

tkPhotoImage = None

mainWindowObject = False



def PixelColorOrIndex(c, palette):
    """
    Return the color of the current pixel within the Mandelbrot set
    - OR -
    Return the INDEX of the color of the pixel within the Mandelbrot set
    The INDEX corresponds to the iteration count of the for loop.
    """
    z = complex(0, 0)  # z0

    global MAX_ITERATIONS
    global iter

    if palette is not None:
        for iter, color in enumerate(palette):
            z = z * z + c
            if abs(z) > 2:
                return color
    else:
        for iter in range(MAX_ITERATIONS):
            z = z * z + c
            if abs(z) > 2:
                return iter

    return palette[iter] if palette is not None and iter < len(palette) else iter



def paint(fractals, imagename, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    global tkPhotoImage

    fractal = fractals[imagename]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=tkPhotoImage, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512

    total_pixels = 512 * 512  # 262144
    # Loop through pixels
    for row in range(512, 0, -1):
        colors = []
        for col in range(512):
            x = minx + col * pixelsize
            y = miny + row * pixelsize

            # Choose color based on the fractal
            if imagename in ['leaf']:
                idx = PixelColorOrIndex(complex(x, y), None)
                color = palette[idx]
            else:
                color = PixelColorOrIndex(complex(x, y), palette)

            colors.append(color)
            y = miny + row * pixelsize  # Prepare for the next loop
            x = minx + col * pixelsize  # Prepare for the next loop

        tkPhotoImage.put('{' + ' '.join(colors) + '}', to=(0, 512 - row))
        window.update()  # Display a row of pixels

        portion = 512 - row / 512  # Prepare for the next loop
        print(pixelsWrittenSoFar(row, 512), end='\r', file=sys.stderr)  # '\r' returns the cursor to the leftmost column


def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))




# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
images = {
        'mandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'mandelbrot-zoomed': {
            'centerX': -1.0,
            'centerY': 0.0,
            'axisLen': 1.0,
            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'centerX': -0.748,
            'centerY': -0.102,
            'axisLen': 0.008,
            },

        'elephants': {
            'centerX':  0.3015,
            'centerY':  -0.0200,
            'axisLen':  0.03,
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },

        'starfish': {
            'centerX': -0.463595023481762,
            'centerY': 0.598380871135558,
            'axisLen': 0.00128413675654471,
            },
        }


def mbrot_main(image):
    global tkPhotoImage
    global window

    print("Rendering {} fractal".format(image), file=sys.stderr)
    start = time()
    window = Tk()

    tkPhotoImage = PhotoImage(width=512, height=512)
    paint(images, image, window)

    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    tkPhotoImage.write(f"{image}.png")
    print(f"Saved image to file {image}.png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
