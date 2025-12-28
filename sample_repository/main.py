"""Main entry point - calls functions from module_a and module_b."""

from module_a import func_a
from module_b import func_b


def main_function(x: int) -> int:
    """This is the entry point we'll analyze."""
    result_a = func_a(x)
    result_b = func_b(x * 2)
    return result_a + result_b
