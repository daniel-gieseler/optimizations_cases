"""Module that is never imported or called - should NOT appear in report."""


def orphan_function(x):
    unused_var = 42  # F841 unused variable
    if x == None:  # E711 comparison to None
        pass
    return x * 2


def another_orphan():
    y = 1
    z = 2
    return y  # z is unused
