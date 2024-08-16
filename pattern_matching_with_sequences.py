def analyze_data(data):
    match data:
        case [x, y] if x == y:  # Guard clause: matches if both elements are equal
            print(f"Pair of identical elements: {x} and {y}")
        case [_, _, 3, *_]:  # Matches sequences where the third element is 3
            print(f"Sequence where the third element is 3: {data}")
        case [x, [y, z]]:  # Nested sequence matching
            print(f"Outer element: {x}, Inner elements: y={y}, z={z}")
        case [x, *rest] if len(rest) > 2:  # Guard clause: matches if there are more than 2 additional elements
            print(f"Starts with {x} and has more than two additional elements: {rest}")
        case _:
            print("No specific pattern matched")

# Test cases
analyze_data([5, 5])          # Matches the guard clause for identical elements
analyze_data([1, 2, 3, 4, 5]) # Matches the pattern where the third element is 3
analyze_data([10, [20, 30]])  # Matches the nested sequence pattern
analyze_data([1, 2, 3, 4])    # Matches the guard clause for more than two additional elements
analyze_data([8, 9])          # Does not match any specific pattern
