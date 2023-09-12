def generate_pascals_triangle(num_rows):
    if num_rows <= 0:
        return []
    
    triangle = []
    
    for i in range(num_rows):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

# Example usage:
num_rows = 5
pascals_triangle = generate_pascals_triangle(num_rows)
for row in pascals_triangle:
    print(row)
