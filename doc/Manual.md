# Fractal Visualizer User Manual

*The following is an basic manual outline written by chatgpt, with added clarification when needed and input/output blocks based on ones given by Prof. Falor:*

## Overview:

The Fractal Renderer is a command-line tool designed to generate and save images of various fractals. 
This manual provides an overview of how to use the main.py script, including information on displaying choices, 
handling invalid arguments, and saving images.

## Usage

To correctly use this program, you mush be in the cs1440-assn4 directory. The command format is as follows:

```bash
python src/main_old.py [FRACTAL_NAME]
```

Correct usage will display a fractal image, save the image as a png to the current directory, and print the following:

```bash
$ python src/main_old.py peacock
Rendering peacock fractal
[100% =================================]
Done in 5.361 seconds!
Saved image to file peacock.png
Close the image window to exit the program

```

When no argument is supplied to main.py, the available fractal choices are displayed to the user. 
To execute the script without specifying a fractal, use the following command:

```bash
$ python src/main_old.py
```

The output will prompt the user to provide the name of a fractal as an argument, displaying the available choices.

```bash
Please provide the name of a fractal as an argument
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish
```

## Handling Invalid Arguments

If an invalid fractal name is provided as an argument, the script will report an error and display the usage message with the available choices. For example:

```bash
$ python src/main_old.py mustache
ERROR: mustache is not a valid fractal
Please choose one of the following:
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish
```

## Case Sensitivity

The Fractal Renderer only accepts lower-case arguments. If a capitalized fractal name is provided, it will be rejected with an error message and the available choices will be displayed.

```bash
$ python src/main_old.py Mandelbrot
ERROR: Mandelbrot is not a valid fractal
Please choose one of the following:
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish

```

## Extra Arguments

Any extra arguments provided after the fractal name will be ignored. For example:

```bash
$ python src/main_old.py mandelbrot extra arguments
Rendering mandelbrot fractal
[100% =================================]
Done in 3.152 seconds!
Saved image to file mandelbrot.png
Close the image window to exit the program
```

## Image Saving

The generated images are saved in the current working directory with filenames following the pattern: 
fractal_name.png. Existing images with the same filename will be silently overwritten.

Feel free to explore the diverse fractal options and create stunning images with the Fractal Renderer!

