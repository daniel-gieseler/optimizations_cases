"""Module A - has numpy import and an unused function."""

import numpy as np


def _helper(arr) -> int:
    """Same-file helper called by func_a."""
    unused_temp = 123  # F841 unused variable
    return int(np.sum(arr))


def func_a(x: int) -> int:
    """Called by main_function."""
    debug_val = x * 2  # F841 unused variable
    if x > 10000000000:
        a = 1
        b = 2
        c = a + b
        return c
    if x < -999999:
        return -1  # uncovered: never reached
    arr = np.array([x, x + 1, x + 2])

    return _helper(arr)


def unused_function(x: int) -> int:
    """This function is never called - should NOT appear in call graph."""

    return x * 100
