# CS 1440 Assignment 4: Refactoring & Design Patterns - Running Unit Tests

The starter code contains 6 **non-trivial** test cases, all of which pass (the 15 tests in `src/tests/test_assertions.py` are trivial, and are provided as examples).  You will increase the number of passing tests as you progress in the project.


## Running all test suites

*   You may run the unit tests through PyCharm or the shell.
*   To execute the tests from your shell, run `src/run_tests.py`.  This script is a convenient way to execute all of the tests in one go.  It produces a lot of output:

```
$ python src/run_tests.py
test_colorOfThePixel (tests.test_mandelbrot.TestMandelbrot)
Mandelbrot fractal configuration and algorithm output the expected colors at key locations ... ok
test_palleteLength (tests.test_mandelbrot.TestMandelbrot)
Palette contains the expected number of colors ... ok
test_pixelsWrittenSoFar (tests.test_mandelbrot.TestMandelbrot)
Progress bar produces correct output ... ok
test_colorOfThePixel (tests.test_phoenix.TestPhoenix)
Phoenix fractal configuration and algorithm output the expected colors at key locations ... ok
test_dictionaryGetter (tests.test_phoenix.TestPhoenix)
Names of fractals in the configuration dictionary are as expected ... ok
test_gradientLength (tests.test_phoenix.TestPhoenix)
Color palette contains the expected number of colors ... ok
...
----------------------------------------------------------------------
Ran 21 tests in 0.001s

OK
```

The interpretation of this output is explained below.



## Running a single test suite

You may also execute an individual unit test suite.  Do this when you are focusing on just one part of the project and don't want to wade through unnecessary output.

The command to run a single suite is different than `run_tests.py`.

1.  First, change into the `src/` directory 
2.  Then run this command, substituting the name of your desired test for `tests/test_mandelbrot.py`
    *   ```bash
        $ cd src
        $ python -m unittest tests/test_mandelbrot.py
        ...
        ----------------------------------------------------------------------
        Ran 3 tests in 0.000s

        OK
        ```



## Interpreting Test Results

A progress report is printed as tests are run.  When tests are unsuccessful, more text is printed to help you understand what exactly went wrong.  When many tests fail, you are presented with a lot of confusing text!

The starter code contains 6 test cases, all of which already pass.  As you work on the project you will cause some tests to *fail*, which means the tests don't see the expected results.  Another test result is *error*, which means that the code being tested crashed.  The dispositions of tests are summarized in this table:

Result | Meaning
-------|--------
`ok`   | The test passed
`FAIL` | The expected result was not seen
`ERROR`| The code under test crashed


### A Passing Test `ok`

When a test passes you are shown the name of the test method, the full name of the module it belongs to, and its docstring followed by `ok`

```
test_palleteLength (tests.test_mandelbrot.TestMandelbrot)
Palette contains the expected number of colors ... ok
```

### A Failing Test `FAIL`

A test that fails indicates that the code under test ran without crashing but did not yield the expected result.  After all tests have been run, a summary of the failure is printed which displays the line of the test file that failed and an explanation of the problem.  In this example, the function `getColorFromPalette` was not expected to return the string `"#FFE5B2"`:

```
======================================================================
FAIL: test_colorOfThePixel (tests.test_phoenix.TestPhoenix)
Phoenix fractal configuration and algorithm output the expected colors at key locations
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/tests/test_phoenix.py", line 24, in test_colorOfThePixel
    self.assertEqual(getColorFromPalette(complex(-0.406, -0.837)), '#F1B7B1')
AssertionError: '#FFE5B2' != '#F1B7B1'
- #FFE5B2
+ #F1B7B1
```


### A Crashing Test `ERROR`

The third way a test can conclude is by unexpectedly crashing (this means that there **is** a way to test a function that is *supposed* to crash; read the code in `src/tests/test_assertions.py` if you are curious).  In this example an index that is too large for the list `j` is used, causing the tested method to crash.  The line of the unit test where the crash happened is shown, and below that you can see the line from which the crash originated, leading you right to the bug:

```
======================================================================
ERROR: test_dictionaryGetter (tests.test_phoenix.TestPhoenix)
Names of fractals in the configuration dictionary are as expected
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/tests/test_phoenix.py", line 29, in test_dictionaryGetter
    self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(f, 'absent'))
  File "src/phoenix_fractal.py", line 92, in getFractalConfigurationDataFromFractalRepositoryDictionary
    return dictionary[name]
KeyError: 'absent'
```



## Unit Test Examples in `src/tests/test_assertions.py`

Use the examples given in the starter code as a guide to creating new test cases.  The test in `src/tests/test_assertions.py` are trivial, meaning that they do not say anything useful about your application.  Nevertheless, they are useful as demonstrations of the different assertions that you can use.

Before you make your final submission, edit `src/run_tests.py` and remove the references to this test file.  Just look for and delete the two `TODO` lines:

```python
from tests import test_assertions  # TODO: delete from the final submission

...

tests.append(test_assertions.TestAssertions)  # TODO: delete from the final submission
```
