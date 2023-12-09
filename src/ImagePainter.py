from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys

IMAGE_SIZE = 512
STATUS_BAR_WIDTH = 34
class ImagePainter:
    def __init__(self, fractal, palette, fractal_info):
        self.fractal = fractal
        self.name = fractal_info["type"]
        self.iterations = fractal_info["iterations"]
        self.palette = palette
        self.fractal_info = fractal_info

    def statusbar(self, rows, cols):
        portion = (IMAGE_SIZE - rows) / IMAGE_SIZE
        pixels = (IMAGE_SIZE - rows) * IMAGE_SIZE
        status_percent = '{:>4.0%}'.format(portion)
        status_bar = '=' * int(STATUS_BAR_WIDTH * portion)
        status_bar = '{:<33}'.format(status_bar)
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))

    def paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas"""

        print(f"Rendering {self.name} fractal")
        # Note the time of when we started so we can measure performance improvements
        before = time.time()

        # Set up the GUI so that we can display the fractal image on the screen
        win = Tk()
        img = PhotoImage(width=IMAGE_SIZE, height=IMAGE_SIZE)
        canvas = Canvas(win, width=IMAGE_SIZE, height=IMAGE_SIZE, bg='#000000')
        canvas.create_image((IMAGE_SIZE/2.0, IMAGE_SIZE/2.0), image=img, state="normal")
        canvas.pack()

        minx = self.fractal_info['centerx'] - (self.fractal_info['axislength'] / 2.0)
        maxx = self.fractal_info['centerx'] + (self.fractal_info['axislength'] / 2.0)
        miny = self.fractal_info['centery'] - (self.fractal_info['axislength'] / 2.0)

        # At this scale, how much length and height on the
        # imaginary plane does one pixel take?
        pixelsize = abs(maxx - minx) / IMAGE_SIZE

        max_iter = self.iterations
        for row in range(IMAGE_SIZE, 0, -1):
            cc = []
            for col in range(IMAGE_SIZE):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                cc.append(self.palette.getColor(self.fractal.count(complex(x, y))))
            img.put('{' + ' '.join(cc) + '}', to=(0, IMAGE_SIZE-row))
            win.update()  # display a row of pixels
            print(self.statusbar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{self.name}.png")
        print(f"Wrote picture {self.name}.png", file=sys.stderr)

        print("Close the image window to exit the program", file=sys.stderr)

        # tkinter.mainloop keeps GUI open
        mainloop()
