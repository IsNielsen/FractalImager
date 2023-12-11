"""
By running this file with src as current working directory, a series of unittests
is run to test the functionality of the program.
"""

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


import unittest

from tests import test_palettefactory, test_fractalparser


suite = unittest.TestSuite()
tests = [test_palettefactory.TestPalettes, test_fractalparser.TestFractalParser]

for test in tests:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
unittest.TextTestRunner(verbosity=2).run(suite)
