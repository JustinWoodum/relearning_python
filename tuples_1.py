# Define a tuple
fruits = ("apple", "banana", "cherry")

# Access elements
first_fruit = fruits[0]
second_fruit = fruits[1]

# Iterate through the tuple
for fruit in fruits:
    print(fruit)

# Tuples are immutable
# fruits[0] = "orange" # This will raise an error

# Tuple unpacking
(a, b, c) = fruits

# Print unpacked values
print(a)
print(b)
print(c)

# Nested tuple
nested_tuple = (("a", "b"), ("c", "d"))

# Access nested elements
first_nested = nested_tuple[0][1]
second_nested = nested_tuple[1][0]

print(first_nested)
print(second_nested)