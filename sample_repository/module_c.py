"""Module C - contains ClassC used by func_b."""

import math
from constants import MULTIPLIER
from helpers import scale_value


class ClassC:
    """A simple class to demonstrate class tracking in call graph."""

    def __init__(self, value: int):
        self.value = value

    def compute(self) -> float:
        return scale_value(math.sqrt(self.value), MULTIPLIER)
