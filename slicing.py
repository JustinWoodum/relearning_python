# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Slicing from index 2 to 5
slice1 = numbers[2:6]
print(f"Slicing [2:6]: {slice1}")

# Slicing with a step
slice2 = numbers[::2]
print(f"Slicing with step [::2]: {slice2}")

# Slicing with negative indices
slice3 = numbers[-5:]
print(f"Slicing last 5 elements [-5:]: {slice3}")

# Reversing the list using slicing
reversed_list = numbers[::-1]
print(f"Reversed list [::-1]: {reversed_list}")

# String slicing
text = "Hello, World!"
print(f"Original string: '{text}'")

# Slicing from index 7 to end
slice4 = text[7:]
print(f"Slicing [7:]: '{slice4}'")

# Slicing with negative indices
slice5 = text[-6:-1]
print(f"Slicing with negative indices [-6:-1]: '{slice5}'")

# Tuple slicing
tuple_data = (10, 20, 30, 40, 50)
print(f"Original tuple: {tuple_data}")

# Slicing from index 1 to 3
slice6 = tuple_data[1:4]
print(f"Slicing [1:4]: {slice6}")

# Slicing with a step
slice7 = tuple_data[::2]
print(f"Slicing with step [::2]: {slice7}")
