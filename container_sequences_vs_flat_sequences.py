# Container sequence: can hold different types
container_list = [1, 'two', 3.0, [4, 5], ('six', 7)]
print(f"Container sequence (list): {container_list}")

# Flat sequence: holds items of one type
flat_string = "hello"
print(f"Flat sequence (string): {flat_string}")

# Demonstrating nested container sequence
container_dict = {'numbers': [1, 2, 3], 'letters': ('a', 'b', 'c')}
print(f"Container sequence (dict): {container_dict}")

# Container sequence: tuple
container_tuple = (1, 'two', 3.0)
print(f"Container sequence (tuple): {container_tuple}")

# Flat sequence: bytes
flat_bytes = b'hello'
print(f"Flat sequence (bytes): {flat_bytes}")

# Accessing elements in container sequence
print(f"Accessing list element: {container_list[3]}")  # Output: [4, 5]
print(f"Accessing dict element: {container_dict['letters']}")  # Output: ('a', 'b', 'c')

# Accessing elements in flat sequence
print(f"Accessing string element: {flat_string[1]}")  # Output: 'e'
print(f"Accessing bytes element: {flat_bytes[1]}")  # Output: 101 (ASCII of 'e')
