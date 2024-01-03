def groupThePeople(groupSizes):
    # Create a dictionary to store groups
    groups = {}
    result = []
    
    # Iterate through the groupSizes array
    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = [i]
        else:
            groups[size].append(i)
        
        # If the group is full, add it to the result and reset it
        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []
    
    return result

# Example usage:
groupSizes1 = [3, 3, 3, 3, 3, 1, 3]
print(groupThePeople(groupSizes1))  # Output: [[0, 1, 2], [3, 4, 6], [5]]

groupSizes2 = [2, 1, 3, 3, 3, 2]
print(groupThePeople(groupSizes2))  # Output: [[0, 5], [1], [2, 3, 4]]
