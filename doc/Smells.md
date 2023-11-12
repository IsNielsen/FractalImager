# CS 1440 Assignment 4.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ``
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank



## 10 Code Smells

If you find a code smell that is not on this list, please add it to your report.

0.  **Magic** numbers
    *   These are literal values used in critical places without any context or meaning
    *   "Does the `256` right here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
    *   *Note, this does not apply to global `CONSTANTS`!*
2.  **Poorly-named** identifiers
    *   Variable names should strike a good balance between brevity and descriptiveness
    *   Short variable names are okay in some situations:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
3.  **Bad** Comments
    *   Comments are condiments for code; a small amount can enhance a meal, but too much ruins it
    *   Strive to write clear, self-documenting code that speaks for itself; when a line needs an explanatory comment to be understood, it indicates that identifier names were poorly chosen
    *   Delete obsolete remarks that no longer accurately describe the situation
    *   The same goes for blocks of commented-out code that serve no purpose and clutter up the file
    *   Programmers sometimes vent their frustration with snarky or vulgar comments; these add no value, are unprofessional and embarrassing, and only serve to demoralize maintainers
4.  **Too many** arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but never used
5.  Function/Method that is **too long**
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself these questions
        *   "Does one function really need to do all of this work?"
        *   "Could I split this into smaller, more focused pieces?"
6.  **Redundant** code
    *   A repeated statement which doesn't have an effect the second time
    *   Ask yourself whether it makes any difference to be run more than once
    *   ```python
        i = 7
        print(i)
        i = 7
        ```
7.  Decision tree that is **too complex**
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Can all branches even be reached?
    *   Has every branch been tested?
8.  **Spaghetti** code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  **Dead** code
    *   Modules that are imported but not used
    *   Variables that are declared but not used
    *   Lines that are *never* run because they are placed in an impossible-to-reach location
        *   Code that appears after a `return` statement
            *   ```python
                return value
                value += 1
                ```
        *   Blocks of code guarded by an impossible-to-satisfy logical test
            *   ```python
                two_bee = True
                if two_bee and not two_bee:
                    print("If can you see this message, it is time to get a new CPU")
                ```
            *   ```python
                counter = 100
                while counter < 0:
                    print(f"T minus {counter}...")
                    counter -= 1
                ```
    *   Functions that are defined but never called *may* or *may not* be dead code
        *   In **Code Libraries** it is normal to define functions that are not meant to be used in the library itself
            *   It is okay to keep these functions
        *   As an **Application** evolves, calls to some of its functions may be removed until only the function's definition remains
            *   Some programmers may keep these functions "just in case" they are needed again
            *   We don't do this at DuckieCorp because we have Git; if we ever need to recover that function, we can find it in the repo's history


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 28, 30]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first
    *   ```python
        import mbrot_fractal
        import phoenix_fractal as phoenix
        import mbrot_fractal
        ```
    *   Remove the second `import` statement



## Code Smells Report

0.  Magic Numbers at `src/mbrot_fractal.py` [lines 237, 239, 243, etc]
    *   The number `512` is used a lot
    *   ```python
	canvas = Canvas(window, width=512, height=512, bg='#000000')
	
	canvas.create_image((256, 256), image=img, state="normal")
	
	pixelsize = abs(maxx - minx) / 512
	```
    *   The number is the dimensions (in pixels) of the tk window. Replace with var `pixels = 512`.

1.  Global variable at `src/mbrot_fractal.py` [line 165]
    *   Calls a global`TWO` which is also redundant as `TWO: int = 2`
    *   ```python
	global TWO
	```
    *   It can be deleted and replaced with an integer `2`

2.  Poorly-named identifiers at `pheonix_fractal.py` [line 128]
    *   all the variables in the function are single characters with no context  for what they are.
    *   ```python
	def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
	```
    *   Most of them aren't used at all, so delete those. Then rename the rest (ex: `f` refers to what part of the dictionary is being used)

3.  Bad Comment at `main.py` [lines 80-110]
    *   As beautiful as it is, the "art" is going to get in the way if any code needs to be changed in these lines
    *   ```python
    print("ERROR:", sys.argv[1], "is not a valid fractal")    #
    print("Please choose one of the following:")             ###
    quit = False                                           #######
    next = ''                                              #######
    iter = 0                                                #####
    while not quit:                             #     ## ########### ###
        next = PHOENX[iter]                      ### #################### ## #
        print("\t%s" % next)                      ###########################
                                              # ############################
        if PHOENX[iter] == 'shrimp-cocktail': ################################
            break                            ####################################
                            #    ## #       ###################################
        else:               ##########     ######################################
            iter += 1     ##############   ####################################
                     ########################################################
              ######################################## CODE IS ART #########
                     ########################################################
    exit = None          ############################## (c) 2023 #############
    i = 0                 ##############   #####################################
    i = 0                   ##########     ####################################
    fractal = ''            #    ## #       ####################################
                                             #################################
    while not exit:                          ################################
        print("\t" + MBROTS[i])               #  ############################
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #
                                              #             #####
                i = i + 1                                  #######
                exit = PHOENX[iter] =='shrimp-cocktail'    #######
                i -= 1 #need to back off, else index error   ###
                exit = exit and MBROTS[i]  == 'starfish'      #	
	```
    *   Move the artwork to the bottom of the file so it doesnt get in the way but can still be apreaciated.

4.  Too many arguments at `phoenix_fractal.py` [line 128]
    *   Most of the arguments are never used.
    *   ```python
	def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
	```
    *   `i, e, g, a, b` are never used, so they are probably ok to delete. `s` references a global, which is a different problem.

5.  TOOOOO Long at `phoenix_fractal.py` [lines 128-214]
    *   Huge function. Even has a TODO saying its way too long:
    *   ```python
	# Its almost 100 lines, so Ill just copy where it admits to being long:
	# TODO: Sometimes I wonder whether some of my functions are trying to do
    	#       too many different things... this is the correct part of the
    	#       program to create a GUI window, right?
	```
    *   This can be split into multiple parts. A lot of the code is redundent anyway, so that will shorten it too.

6.  Redundant code at `pheonix_fractal.py` [lines 159-161]
    *   The same line of code repeated 3 times because "Larry" did it.
    *   ```python
	tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
    	tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
    	tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
	```
    *   It only needs to pack once, delete the other 2.

7.  Too Complex at `mbrot_fractal.py` [lines 168-185]
    *   Too many nested if/ifelse that I don't want to look at it.
    *	```
	    if abs(z) > TWO:
                z = float(TWO)
                import builtins
                len = builtins.len
                if iter >= len(palette):
                    iter = len(palette) - 1
                return palette[iter]
            elif abs(z) < TWO:
                continue
            elif abs(z) > seven:
                print("You should never see this message in production", file=sys.stderr)
                continue
                break
            elif abs(z) < 0:
                print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)
                sys.exit(1)
            else:
                pass
	```
    *   Do the bad cases first, exiting (`if abs(z) > 7 or abs(z) < 0:`) then do the good cases, else pass.

8.  Spaghetti at `file` [lines 275-285]
    *   The code keeps updating variabls is strange ways, then returns a string by turning the vars into lists and then joining them?
    *   ```python
	def pixelsWrittenSoFar(rows, cols):
    	portion = (512 - rows) / 512
    	pixels = (512 - rows) * 512
    	status_percent = '{:>4.0%}'.format(portion)
    	status_bar_width = 34
    	status_bar = '=' * int(status_bar_width * portion)
    	status_bar = '{:<33}'.format(status_bar)
    	# print(f"{pixels} pixels have been output so far")
    	# return pixels
    	# return '[' + status_percent + ' ' + status_bar + ']'
    	return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
	```
    *   It will probably be easier to delete and rewrite it than understand it.

9.  Dead Code at `main.py` [line 72]
    *   Line of code after `break` is never reached
    *   ```python
	break
	sys.exit(True)
	```
    *   Delete the line after the break
