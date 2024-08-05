import array

# Generator expression for a tuple of squares
squares_tuple = tuple(x**2 for x in range(10))
print(f"Generator expression (tuple of squares): {squares_tuple}")

# Generator expression for an array of squares
squares_array = array.array('i', (x**2 for x in range(10)))
print(f"Generator expression (array of squares): {squares_array}")

# Generator expression for Cartesian product
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = ((x, y) for x in list1 for y in list2)
print(f"Generator expression (Cartesian product): {list(cartesian_product)}")
