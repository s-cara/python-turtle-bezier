from math import sqrt

def _checkType(*args, types):
    for obj in args:
        t = type(obj)

        found = False

        for v in types:
            if t == v:
                found = True

        if not found:
            raise TypeError('Invalid type passed')

class Vector2:
    '''
    Class representing a two-dimensional vector.

    Supports addition, subtraction, multiplication, negation and string conversion.

    Methods:
        distanceTo: (Vector2) -> int | float
            Returns the distance between the instance and another point.

    Properties:
        x: int | float
        y: int | float
    '''

    def __init__(self, x: int | float, y: int | float):
        _checkType(x, y, types=[int, float])

        self.x = x  
        self.y = y

    def __add__(self, other):
        _checkType(other, types=[Vector2])

        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        _checkType(other, types=[Vector2])

        return self.__add__(-other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, other):
        _checkType(other, types=[int, float])

        return Vector2(self.x * other, self.y * other)

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'

    def distanceTo(self, other):
        _checkType(other, types=[Vector2])

        # (x -> y)
        return sqrt((abs(self.x - other.x) ** 2) + (abs(self.y - other.y) ** 2))

    def lerp(self, other, t):
        _checkType(other, types=[Vector2])
        _checkType(t, types=[int, float])

        return self + (other - self) * t

class Vector3:
    '''
    Class representing a three-dimensional vector.

    Supports addition, subtraction, negation and string conversion.

    Methods:
        distanceTo: (Vector3) -> int | float
            Returns the distance between the instance and another point.

    Properties:
        x: int | float
        y: int | float
        z: int | float
    '''

    def __init__(self, x: int | float, y: int | float, z: int | float):
        _checkType(x, y, z, types=[int, float])

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        _checkType(other, types=[Vector3])

        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        _checkType(other, types=[Vector3])
        
        return self.__add__(-other)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        _checkType(other, types=[int, float])

        return Vector3(self.x * other, self.y * other, self.z * other)

    def __repr__(self):
        return f'Vector3({self.x}, {self.y}, {self.z})'

    def distanceTo(self, other):
        _checkType(other, types=[Vector3])

        # ((x -> z) -> y)
        return sqrt((sqrt((abs(self.x - other.x) ** 2) + (abs(self.z - other.z) ** 2)) ** 2) + (abs(self.y - other.y) ** 2))

    def lerp(self, other, t):
        _checkType(other, types=[Vector3])
        _checkType(t, types=[int, float])

        return self + (other - self) * t
