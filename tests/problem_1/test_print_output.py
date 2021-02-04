# ASSIGNMENT: HW 00
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output

FILENAME = 'hello.py'
POINTS = 3

def test_print_output():
    return _test_output(FILENAME,
                        r"""Hello World!""",
                        input_values=None)


