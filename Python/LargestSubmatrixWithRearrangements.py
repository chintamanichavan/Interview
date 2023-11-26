class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
 
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        # Step 1: Histogram Construction
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        max_area = 0

        # Step 2 and 3: Sorting Rows and Max Area Calculation
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                max_area = max(max_area, matrix[i][j] * (j + 1))

        return max_area
