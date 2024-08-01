# List comprehension for squares
squares_listcomp = [x**2 for x in range(10)]
print(f"List comprehension (squares): {squares_listcomp}")

# Map function for squares
squares_map = list(map(lambda x: x**2, range(10)))
print(f"Map function (squares): {squares_map}")

# List comprehension with condition (even numbers)
evens_listcomp = [x for x in range(10) if x % 2 == 0]
print(f"List comprehension (evens): {evens_listcomp}")

# Filter function for even numbers
evens_filter = list(filter(lambda x: x % 2 == 0, range(10)))
print(f"Filter function (evens): {evens_filter}")

# Combined map and filter with list comprehension (even squares)
even_squares_listcomp = [x**2 for x in range(10) if x % 2 == 0]
print(f"List comprehension (even squares): {even_squares_listcomp}")

# Combined map and filter
even_squares_map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
print(f"Map and filter function (even squares): {even_squares_map_filter}")
