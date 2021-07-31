from math import hypot, sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(self.x or self.y)


v1 = Vector(1, 1)
v2 = Vector(2, 2)
print(v1 + v2)
print(abs(v1))
print(v2 * 3)
print(v1, v2)
v3 = Vector(0, 0)
if v3:
    print('bool')
else:
    print('False')