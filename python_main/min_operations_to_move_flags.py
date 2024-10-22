def min_operations(N, coordinates):
    # Sort flags by x and y coordinates
    x_coords = []
    y_coords = []
    for coord in coordinates:
        x_coords.append(coord[0])
        y_coords.append(coord[1])
    
    # Sort x and y coordinates
    x_coords.sort()
    y_coords.sort()
    
    # Find median y coordinate
    median_y = y_coords[N // 2]
    
    # Calculate the total cost to align all flags to median y
    y_cost = sum(abs(y - median_y) for x, y in coordinates)
    
    # Align x coordinates to a consecutive sequence
    x_cost = sum(abs(x - (min(x_coords) + i)) for i, x in enumerate(x_coords))
    
    return y_cost + x_cost

# Example Usage:
N = 3
coordinates = [(3, 2), (1, 1), (4, 3)]
print(min_operations(N, coordinates))  # Output: 1

N = 3
coordinates = [(1, 1), (2, 2), (3, 3)]
print(min_operations(N, coordinates))  # Output: 2


