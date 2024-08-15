# Basic tuple unpacking
point = (1, 2)
x, y = point
print(f"Unpacked tuple: x={x}, y={y}")

# Unpacking with lists
numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers
print(f"a={a}, b={b}, rest={rest}")

# Ignoring certain values during unpacking
_, _, c, d, _ = numbers
print(f"Selected unpacking: c={c}, d={d}")

# Nested unpacking
nested_tuple = (1, (2, 3), 4)
e, (f, g), h = nested_tuple
print(f"Nested unpacking: e={e}, f={f}, g={g}, h={h}")

# Unpacking for swapping variables
i, j = 10, 20
i, j = j, i
print(f"Swapped values: i={i}, j={j}")

# Unpacking with functions
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(f"Unpacked function return: x={x}, y={y}")

# Unpacking with ** for dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
def print_person(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

print_person(**person)
