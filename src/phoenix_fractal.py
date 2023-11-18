#!/usr/bin/env python3
# Phoenix Fractal Visualizer - a variation of the Julia Fractal

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


# These are the imports that I usually import
import turtle
import sys


# these ones are the ones that i'm using in this program
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time


SPC = chr(0o40)  # Why doesn't anybody write octal numbers anymore...
size = 0o1000


def getColorFromPalette(z):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """
    # Constants
    c = complex(0.5667, 0.0)
    phoenix = complex(-0.5, 0.0)

    # Initialize variables
    z_flipped = complex(z.imag, z.real)
    z_prev = 0 + 0j
    z = z_flipped

    # Loop over the range of colors in the palette
    for i in range(102):
        z_save = z  # Save the current Z value before overwriting it
        # Compute the new Z value from the current and previous Zs
        z = z * z + c + (phoenix * z_prev)
        z_prev = z_save  # Set the prevZ value for the next iteration

        # If the absolute value of Z is greater or equal to 2, return that color
        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded

    return grad[101]  # Else this is a bounded sequence


Save_As_Picture = True
tkPhotoImage = None


def makePictureOfFractal(fractal, tk_window, tk_photo_image, bg_color, size):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is square (size x size) pixels."""

    # Compute the minimum and maximum coordinates of the picture
    min_coord = (fractal['centerX'] - (fractal['axisLength'] / 2.0),
                 fractal['centerY'] - (fractal['axisLength'] / 2.0))
    max_coord = (fractal['centerX'] + (fractal['axisLength'] / 2.0),
                 fractal['centerY'] + (fractal['axisLength'] / 2.0))

    # Create the canvas object
    canvas = Canvas(tk_window, width=size, height=size, bg=bg_color)
    canvas.pack()

    # Create the TK PhotoImage object
    canvas.create_image((size/2, size/2), image=tk_photo_image, state="normal")

    # Calculate the pixel size in the complex plane
    pixel_size = abs(max_coord[0] - min_coord[0]) / size

    # Draw the pixels on the canvas
    for row in range(size, 0, -1):
        colors = []
        for col in range(size):
            x_val = min_coord[0] + col * pixel_size
            y_val = min_coord[1] + row * pixel_size
            color = getColorFromPalette(complex(x_val, y_val))
            colors.append(color)

        pixel_data = '{' + ' '.join(colors) + '}'
        tk_photo_image.put(pixel_data, (0, size - row))
        tk_window.update()

        # Print a status bar on the console
        fraction_done = (size - row) / size
        print(f"[{fraction_done:>4.0%}"
              + f' {SPC}'
              + f"{'=' * int(34 * fraction_done):<33}]",
              end="\r", file=sys.stderr)


# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
grad = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
        '#ffeea2', '#fff09f', '#fff39c', '#fff699', '#fff996', '#fffc92',
        '#ffff8f', '#fbff8c', '#f8ff89', '#f4ff86', '#f0ff83', '#ebff80',
        '#e7ff7d', '#e2ff79', '#deff76', '#d8ff73', '#d3ff70', '#ceff6d',
        '#c8ff6a', '#c2ff67', '#bcff63', '#b6ff60', '#b0ff5d', '#a9ff5a',
        '#a3ff57', '#9cff54', '#94ff51', '#8dff4d', '#86ff4a', '#7eff47',
        '#76ff44', '#6eff41', '#66ff3e', '#5dff3b', '#54ff37', '#4cff34',
        '#43ff31', '#39ff2e', '#30ff2b', '#28ff29', '#25ff2d', '#21ff31',
        '#1eff34', '#1bff39', '#18ff3d', '#15ff41', '#12ff46', '#0fff4b',
        '#0cff50', '#08ff55', '#05ff5b', '#02ff60', '#00fe66', '#00fb6d',
        '#00f873', '#00f579', '#00f17f', '#00ee84', '#00eb8a', '#00e88f',
        '#00e594', '#00e299', '#00df9e', '#00dba2', '#00d8a6', '#00d5aa',
        '#00d2ae', '#00cfb2', '#00ccb6', '#00c9b9', '#00c5bc', '#00c2bf',
        '#00bdbf', '#00b4bc', '#00abb9', '#00a3b6', '#009bb3', '#0092af',
        '#008bac', '#0083a9', '#007ba6', '#0074a3', '#006da0', '#00669d',
        '#005f9a', '#005996', '#005293', '#004c90', '#00468d', '#00418a',
        '#003b87', '#003684', '#003080', '#002b7d', '#00277a', '#002277']

# Patrick T. 11/22/2022
# The program was crashing from IndexError because the color palette had too
# few colors.  Boy, was the customer mad about that!  I added some extra black
# pixels at the end to stop it crashing until somebody solves the actual
# problem.  PLEASE DELETE THIS CODE AFTER THE BUG GETS FIXED!!!
class Black:
    BLACK = '#FFFFFF'

grad += [Black.BLACK] * 6  # six pixels should be enough


# This dictionary contains the different views of the Phoenix set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
f = {
        # The full Phoneix set
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }


# This is how you write colors for computers
WHITE = '#ffffff'  # white
RED = '#ff0000'  # red
BLUE = '#00ff00'  # blue
GREEN = '#0000ff'  # green
BLACK = '#000000'  # black
ORANGE = '#ffa50'  # orange
TOMATO = '#ff6347'  # tomato (a shade of red)
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
REBECCA_PURPLE = '#663399'  # Rebecca Purple
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
GREY0 = '#000000'  # gray 0 - basically the same as black
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
GREY74 = '#bdbdbd'  # gray 74 - almost white
GRAY99 = '#fcfcfc'  # gray 99 - almost white


def phoenix_main(i):
    """The main entry-point for the Phoenix fractal generator"""
    global tkPhotoImage
    global size

    print("Rendering %s fractal" % i, file=sys.stderr)
    start = time()
    window = Tk()

    tkPhotoImage = PhotoImage(width=size, height=size)
    makePictureOfFractal(f[i], window, tkPhotoImage, GREY0, size)

    print(f"\nDone in {time() - start:.3f} seconds!", file=sys.stderr)

    tkPhotoImage.write(f"{i}.png")
    print("Saved image to file " + i + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()



