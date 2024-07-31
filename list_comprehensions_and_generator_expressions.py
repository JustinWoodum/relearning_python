# List comprehension
squares_list = [x**2 for x in range(10)]
print(f"List comprehension (squares of 0-9): {squares_list}")

# Generator expression
squares_generator = (x**2 for x in range(10))
print(f"Generator expression (squares of 0-9): {list(squares_generator)}")

# List comprehension with condition
even_squares_list = [x**2 for x in range(10) if x % 2 == 0]
print(f"List comprehension with condition (even squares of 0-9): {even_squares_list}")

# Generator expression with condition
even_squares_generator = (x**2 for x in range(10) if x % 2 == 0)
print(f"Generator expression with condition (even squares of 0-9): {list(even_squares_generator)}")

# Using list comprehension for string manipulation
words = ['hello', 'world', 'python']
capitalized_words = [word.capitalize() for word in words]
print(f"List comprehension for string manipulation (capitalize words): {capitalized_words}")

# Using generator expression for string manipulation
capitalized_words_gen = (word.capitalize() for word in words)
print(f"Generator expression for string manipulation (capitalize words): {list(capitalized_words_gen)}")
