"""Module B - imports json and uses ClassC."""

import json
from module_c import ClassC


def func_b(x: int) -> int:
    """Called by main_function, uses ClassC."""
    if x == None:  # E711 - auto-fixable to 'x is None'
        pass
    obj = ClassC(x)
    data = json.dumps({"value": obj.compute()})
    return len(data)
