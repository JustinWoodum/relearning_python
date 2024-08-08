# Create a list and a tuple
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)

# List-specific methods
my_list.append(5)
print(f"List after append: {my_list}")

my_list.extend([6, 7])
print(f"List after extend: {my_list}")

my_list.insert(2, 'inserted')
print(f"List after insert: {my_list}")

my_list.remove('inserted')
print(f"List after remove: {my_list}")

popped = my_list.pop()
print(f"List after pop: {my_list}, popped element: {popped}")

my_list.reverse()
print(f"List after reverse: {my_list}")

my_list.sort()
print(f"List after sort: {my_list}")

# Tuple-specific methods (tuples are immutable, so fewer methods)
count = my_tuple.count(2)
print(f"Tuple count of 2: {count}")

index = my_tuple.index(3)
print(f"Index of 3 in tuple: {index}")

# Common methods and attributes
# Length
print(f"Length of list: {len(my_list)}")
print(f"Length of tuple: {len(my_tuple)}")

# Membership test
print(f"Is 3 in list? {'yes' if 3 in my_list else 'no'}")
print(f"Is 3 in tuple? {'yes' if 3 in my_tuple else 'no'}")

# Iteration
print("Iterating over list:")
for item in my_list:
    print(item)

print("Iterating over tuple:")
for item in my_tuple:
    print(item)

# Access by index
print(f"Element at index 1 in list: {my_list[1]}")
print(f"Element at index 1 in tuple: {my_tuple[1]}")

# Slicing
print(f"Slicing list [1:3]: {my_list[1:3]}")
print(f"Slicing tuple [1:3]: {my_tuple[1:3]}")

# Attempting to use list-specific methods on a tuple (will raise AttributeError)
try:
    my_tuple.append(5)
except AttributeError as e:
    print(f"Error: {e}")

try:
    my_tuple.sort()
except AttributeError as e:
    print(f"Error: {e}")
