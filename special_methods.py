class MyList:
    def __init__(self, initial_list):
        self.items = initial_list
    
    def __str__(self):
        return f"MyList with items: {self.items}"
    
    def __repr__(self):
        return f"MyList({self.items})"
    
    def __add__(self, other):
        return MyList(self.items + other.items)
    
    def __len__(self):
        return len(self.items)

# Demonstration
list1 = MyList([1, 2, 3])
list2 = MyList([4, 5, 6])

# Using __str__ method
print(list1)  # Output: MyList with items: [1, 2, 3]

# Using __repr__ method
print(repr(list1))  # Output: MyList([1, 2, 3])

# Using __add__ method
list3 = list1 + list2
print(list3)  # Output: MyList with items: [1, 2, 3, 4, 5, 6]

# Using __len__ method
print(len(list3))  # Output: 6
