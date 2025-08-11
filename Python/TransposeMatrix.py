class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Transpose the matrix
        return [list(row) for row in zip(*matrix)]

# review 2024-08-31

# review 2025-08-10
