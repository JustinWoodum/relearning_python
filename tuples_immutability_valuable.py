# Defining a tuple to represent a record of a point
point1 = (3, 4)
point2 = (5, 6)

# Displaying points
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")

# Attempting to modify the tuple will raise an error
try:
    point1[0] = 7
except TypeError as e:
    print(f"Error: {e}")

# Tuples as immutable records in a list
points = [(1, 2), (3, 4), (5, 6)]
print(f"Points list: {points}")

# Ensuring immutability - you can't change the points
for point in points:
    try:
        point[0] = 0
    except TypeError as e:
        print(f"Error: {e}")

# Tuples can be used to ensure data integrity
def calculate_distance(point_a, point_b):
    return ((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)**0.5

# Calculate distance between two points
distance = calculate_distance(point1, point2)
print(f"Distance between {point1} and {point2}: {distance}")

# Using tuples as keys in a dictionary to represent connections
connections = {
    (1, 2): "A to B",
    (3, 4): "B to C",
    (5, 6): "C to D"
}
print(f"Connections dictionary: {connections}")

# Ensuring tuples are not modified
try:
    connections[(1, 2)][0] = 'X'
except TypeError as e:
    print(f"Error: {e}")
