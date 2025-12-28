"""Manually concatenated: only code reachable from main_function."""

import json
import math
import numpy as np

# from constants.py (BASE_FACTOR + MULTIPLIER, not DEFAULT_OFFSET)
BASE_FACTOR = 6
MULTIPLIER = BASE_FACTOR * 7


# from helpers.py (only scale_value, not unused_helper)
def scale_value(x: float, factor: float) -> float:
    """Called by ClassC.compute()."""
    return x * factor


# from module_c.py
class ClassC:
    """A simple class to demonstrate class tracking in call graph."""

    def __init__(self, value: int):
        self.value = value

    def compute(self) -> float:
        return scale_value(math.sqrt(self.value), MULTIPLIER)


# from module_a.py (func_a + _helper, not unused_function)
def _helper(arr) -> int:
    """Same-file helper called by func_a."""
    return int(np.sum(arr))


def func_a(x: int) -> int:
    """Called by main_function."""
    arr = np.array([x, x + 1, x + 2])
    return _helper(arr)


# from module_b.py
def func_b(x: int) -> int:
    """Called by main_function, uses ClassC."""
    obj = ClassC(x)
    data = json.dumps({"value": obj.compute()})
    return len(data)


# from main.py
def main_function(x: int) -> int:
    """This is the entry point we'll analyze."""
    result_a = func_a(x)
    result_b = func_b(x * 2)
    return result_a + result_b
