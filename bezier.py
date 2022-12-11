def _linear(points, t, change=0):
    return points[0 + change].lerp(points[1 + change], t)

def _quadratic(points, t, change=0):
    v1 = _linear(points, t, change=change)
    v2 = _linear(points, t, change=change + 1)

    return v1.lerp(v2, t)

def _cubic(points, t, change=0):
    v1 = _quadratic(points, t, change=change)
    v2 = _quadratic(points, t, change=change + 1)

    return v1.lerp(v2, t)

def _quartic(points, t, change=0):
    v1 = _cubic(points, t, change=change)
    v2 = _cubic(points, t, change=change + 1)

    return v1.lerp(v2, t)

def _quintic(points, t, change=0):
    v1 = _quartic(points, t, change=change)
    v2 = _quartic(points, t, change=change + 1)

    return v1.lerp(v2, t)

def _sextic(points, t, change=0):
    v1 = _quintic(points, t, change=change)
    v2 = _quintic(points, t, change=change + 1)

    return v1.lerp(v2, t)

_functions = [
    _linear,
    _quadratic,
    _cubic,
    _quartic,
    _quintic,
    _sextic
]

def getPoint(points, t):
    idx = len(points) - 2

    if (idx < 0) or (idx > len(_functions) - 1):
        raise IndexError('Index too high!')

    return _functions[idx](points, t)
