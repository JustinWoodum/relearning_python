# Boolean types
bool_true = True
bool_false = False

print(f"Boolean True: {bool_true}")
print(f"Boolean False: {bool_false}")

# Other types as booleans
# Numbers
zero = 0
non_zero = 42

print(f"Boolean value of 0: {bool(zero)}")  # Output: False
print(f"Boolean value of 42: {bool(non_zero)}")  # Output: True

# Strings
empty_string = ""
non_empty_string = "Hello"

print(f"Boolean value of empty string: {bool(empty_string)}")  # Output: False
print(f"Boolean value of 'Hello': {bool(non_empty_string)}")  # Output: True

# Lists
empty_list = []
non_empty_list = [1, 2, 3]

print(f"Boolean value of empty list: {bool(empty_list)}")  # Output: False
print(f"Boolean value of [1, 2, 3]: {bool(non_empty_list)}")  # Output: True

# None
none_value = None

print(f"Boolean value of None: {bool(none_value)}")  # Output: False
