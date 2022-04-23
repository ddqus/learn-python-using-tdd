"""
v0.0.1
"""

_COLLECTION_TYPE = (list, tuple, dict, set)
_NUMERIC_TYPE = (int, float, complex)
_BOOLEAN_TYPE = (bool,)


def tuplify(obj):
    if _is_collection_type(obj):
        return tuple(obj)

    if _is_tuplify_type(obj):
        return obj,

    raise ValueError(f"Cannot convert to tuple - {obj}")


def _is_collection_type(obj):
    return type(obj) in _COLLECTION_TYPE


def _is_tuplify_type(obj):
    return type(obj) in (_NUMERIC_TYPE + _BOOLEAN_TYPE + (str,))
