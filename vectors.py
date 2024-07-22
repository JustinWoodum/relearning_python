import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

# Demonstration
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# Vector addition
v3 = v1 + v2
print(f"Vector addition: {v1} + {v2} = {v3}")  # Output: Vector2D(4, 6)

# Vector absolute value (magnitude)
v1_magnitude = abs(v1)
print(f"Absolute value (magnitude) of {v1} = {v1_magnitude}")  # Output: 5.0

# Scalar multiplication
v4 = v1 * 3
print(f"Scalar multiplication: {v1} * 3 = {v4}")  # Output: Vector2D(9, 12)
