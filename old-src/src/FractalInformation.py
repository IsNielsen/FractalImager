#!/usr/bin/env python3

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

fractals = {
    'mandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLen': 2.5,
        'fractalType': 'mandelbrot'
    },

    'mandelbrot-zoomed': {
        'centerX': -1.0,
        'centerY': 0.0,
        'axisLen': 1.0,
        'fractalType': 'mandelbrot'
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLen': 0.004978179931102462,
        'fractalType': 'mandelbrot'
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
        'fractalType': 'mandelbrot'
    },

    'seahorse': {
        'centerX': -0.748,
        'centerY': -0.102,
        'axisLen': 0.008,
        'fractalType': 'mandelbrot'
    },

    'elephants': {
        'centerX': 0.3015,
        'centerY': -0.0200,
        'axisLen': 0.03,
        'fractalType': 'mandelbrot'
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLen': 0.000051248888,
        'fractalType': 'mandelbrot'
    },

    'starfish': {
        'centerX': -0.463595023481762,
        'centerY': 0.598380871135558,
        'axisLen': 0.00128413675654471,
        'fractalType': 'mandelbrot'
    },

    # The full Phoenix set ##########################
    'phoenix': {
        'centerX': 0.0,
        'centerY': 0.0,
        'axisLen': 3.25,
        'fractalType': 'phoenix'
    },

    # This one looks like a peacock's tail to me
    'peacock': {
        'centerX': -0.363287878200906,
        'centerY': 0.381197981824009,
        'axisLen': 0.0840187115019564,
        'fractalType': 'phoenix'
    },

    # Two or more monkeys having a scuffle
    'monkey-knife-fight': {
        'centerX': -0.945542168674699,
        'centerY': 0.232234726688103,
        'axisLen': 0.136626506024096,
        'fractalType': 'phoenix'
    },

    # This one makes me hungry to look at
    'shrimp-cocktail': {
        'centerX': 0.529156626506024,
        'centerY': -0.3516077170418,
        'axisLen': 0.221204819277108,
        'fractalType': 'phoenix'
    },
}

def print_frac_list():
    all_fracs = ""
    for key in fractals:
        all_fracs += key + '\n'
    # print(all_fracs)
    return all_fracs
