# List comprehension for Cartesian product
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_listcomp = [(x, y) for x in list1 for y in list2]
print(f"List comprehension (Cartesian product): {cartesian_listcomp}")
