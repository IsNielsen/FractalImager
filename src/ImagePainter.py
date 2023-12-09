import sys
from time import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from FractalFactory import FractalFactory
from PaletteFactory import PaletteFactory
from FractalParser import FractalParser


class ImagePainter:
    def __init__(self, fractal_factory, palette_factory, fractal_parser):
        self.fractal_factory = fractal_factory
        self.palette_factory = palette_factory
        self.fractal_parser = fractal_parser
