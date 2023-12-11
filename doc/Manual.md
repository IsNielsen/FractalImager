# Fractal Visualizer User Manual

*The following is an basic manual outline by chatgpt, with all the information about the program written by a human*

## Overview:

The Fractal Renderer is a command-line tool designed to generate and save images of various fractals. 
This manual provides an overview of how to use the main.py script, including information on displaying choices, 
color palettes, handling invalid arguments, and saving images.

## Usage

[NOTE]: *This Manual assumes that your current working directory is just above `src/`*

```bash
python [FILEPATH]/main.py [FRACTALPATH].frac [PalettePath].py
```

A list of fractals and palettes can be found below.

Correct usage will display a fractal image, save the image as a `.png` to the current directory, and print the following:

```bash
$ python src/main.py data/phoenix.frac pastels
[100% =================================]
Done in 1.750 seconds!
Wrote image phoenix.png
Close the image window to exit the program

```

When no argument is supplied to main.py, a default fractal will be printed using a default palette:

```bash
$ python src/main.py
```

This will print a default mandelbrot fractal and the output will look like this:

```bash
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palette
[100% =================================]
Done in 6.111 seconds!
Wrote image default.png
Close the image window to exit the program
```

The program reads the first argument after the main.py call as a fractal, so it will not print a default fractal with a specified palete.
However the user can request a fractal and not specify a palette, which will return the default palette. Doing this will look like the following:

```bash
$ python src/main.py data/phoenix.frac
PaletteFactory: Creating default color palette
[100% =================================]
Done in 1.388 seconds!
Wrote image phoenix.png
Close the image window to exit the program
```

## Handling Invalid Fractals

If an invalid fractal path is given, the program will crash with a FileNotFoundError. For example:

```bash
$ python src/main.py data/notvalid.frac
...
...
FileNotFoundError: [Errno 2] No such file or directory: 'data/notvalid.frac'
```

## Invalid Palettes

If an invalid palette is requested, the program will crash with an NotImplementedError:

```bash
$ python src/main.py data/phoenix.frac nonexistant
...
...
NotImplementedError: Invalid palette requested

```

## Extra Arguments

Any extra arguments provided after fractal and palette will be ignored. For example:

```bash
$ python src/main.py data/phoenix.frac pastels extra ignored
[100% =================================]
Done in 1.373 seconds!
Wrote image phoenix.png
Close the image window to exit the program

```

## Image Saving

The generated images are saved in the current working directory with filenames following the pattern: 
fractal_name.png. Existing images with the same filename in current working directory will be silently overwritten.

Feel free to explore the diverse fractal options and create stunning images with the Fractal Renderer!

# List of valid Fractals and Palettes:

## Fractals

These are the fractals that can currently be used, however in the `data/` folder there are more `.frac` files.
To use these, a new fractal type will have to be implemented.

This list will will just have the fractal names and not the file paths. Assuming the users current working directory is above `src/`
and `data/`, the file path to use them will be `data/[FRACTALNAME].frac/`.

-   Mandelbrot Fractals:
    -   8-points
    -   branches@0064
    -   branches@0128
    -   branches@0256
    -   branches@0512
    -   branches@1024
    -   coral
    -   elephants
    -   enhance
    -   leaf
    -   mandelbrot
    -   mandelbrot-zoomed
    -   minibrot
    -   rabbit-hole
    -   seahorse
    -   spiral-jetty
    -   spiral0
    -   spiral1
    -   spiral1@0256
    -   spiral1@0512
    -   spiral1@1024
    -   starfish
    -   tip0
    -   tip1
    -   tip2
    -   tip3
    -   tip4
    -   wholly-squid

-   Higher Powers of Mandelbrot
    -   mandel-pow3

-   Phoenix Fractals:
    -	feathers
    -   monkey-knife-fight
    -   oriental-dragons
    -   phoenix
    -   shrimp-cocktail

-   Burning Ship Fractals:
    -   burningship
    -   burningship-prow
    -   burningship-stern

## Palettes

When choosing a palette, type it as shown in all lowercase.

-	pastels
-	blackandwhite
-	reverse	




## 
##

#### Thank you for reading this! Have fun drawing fractals!
