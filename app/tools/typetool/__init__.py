_TUPLABLE_TYPE = (str, list, tuple, dict, set)
_NUMERIC_TYPE = (int, float, complex)
_BOOLEAN_TYPE = (bool,)


def tuplify(obj):
    _type = type(obj)

    if _type in _TUPLABLE_TYPE:
        return tuple(obj)

    if _type in (_NUMERIC_TYPE + _BOOLEAN_TYPE):
        return obj,

    raise ValueError(f"Cannot convert to tuple - {obj}")
