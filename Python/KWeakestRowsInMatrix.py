class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        # Create a list of tuples (count of soldiers, row index)
        soldiers_count = [(sum(row), i) for i, row in enumerate(mat)]
        
        # Sort the list of tuples by the count of soldiers
        soldiers_count.sort()
        
        # Take the first k elements and extract their row indices
        result = [row_idx for _, row_idx in soldiers_count[:k]]
        
        return result

# Example usage:
mat1 = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k1 = 3
print(kWeakestRows(mat1, k1))  # Output: [2, 0, 3]

mat2 = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]
k2 = 2
print(kWeakestRows(mat2, k2))  # Output: [0, 2]
