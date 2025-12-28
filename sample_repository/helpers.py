"""Helper functions used by classes."""


def scale_value(x: float, factor: float) -> float:
    """Called by ClassC.compute()."""
    return x * factor


def unused_helper(x: float) -> float:
    """Never called - should NOT appear in call graph."""
    return x / 2
