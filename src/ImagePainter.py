from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys


STATUS_BAR_WIDTH = 34
class ImagePainter:
    def __init__(self, fractal, palette, fractal_info):
        self.fractal = fractal
        self.name = fractal_info["type"]
        self.iterations = fractal_info["iterations"]
        self.palette = palette
        self.fractal_info = fractal_info
        self.size = fractal_info["pixels"]
        self.pixels = fractal_info["pixels"]

    def statusbar(self, rows):
        portion = (self.size - rows) / self.size
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
        img = PhotoImage(width=self.pixels, height=self.pixels)
        canvas = Canvas(win, width=self.size, height=self.size, bg='#00FF00')
        canvas.create_image((self.size / 2.0, self.size / 2.0), image=img, state="normal")
        canvas.pack()

        centerx = self.fractal_info["centerx"]
        centery = self.fractal_info["centery"]
        axislength = self.fractal_info["axislength"]

        minx = centerx - (axislength / 2.0)
        miny = centery - (axislength / 2.0)
        maxx = centerx + (axislength / 2.0)

        pixelsize = axislength / self.pixels

        for row in range(self.size, 0, -1):
            cc = []
            for col in range(self.size):
                x = minx + col * pixelsize
                y = miny + row * pixelsize

                # cc.append(self.palette.getColor(self.fractal.count(complex(x, y))))
                color = self.palette.getColor(self.fractal.count(complex(x, y)))
                cc.append(color)

            img.put('{' + ' '.join(cc) + '}', to=(0, self.size - row))
            win.update()  # display a row of pixels
            print(self.statusbar(row), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{self.name}.png")
        print(f"Wrote picture {self.name}.png", file=sys.stderr)

        print("Close the image window to exit the program", file=sys.stderr)

        # tkinter.mainloop keeps GUI open
        mainloop()
