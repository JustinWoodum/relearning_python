class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

# Demonstration
v = Vector2D(3, 4)
print(repr(v))  # Output: Vector2D(x=3, y=4)
