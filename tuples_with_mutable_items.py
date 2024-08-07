# Tuple containing a list (mutable item)
my_tuple = ([1, 2, 3], "immutable string")

# Display original tuple
print(f"Original tuple: {my_tuple}")

# Modify the mutable list inside the tuple
my_tuple[0].append(4)

# Display modified tuple
print(f"Modified tuple: {my_tuple}")

# Tuple remains the same, but the list inside it has changed
try:
    my_tuple[0] = [1, 2, 3, 4]
except TypeError as e:
    print(f"Error: {e}")

# Immutability of tuple itself vs mutability of contained items
print(f"Final tuple: {my_tuple}")
