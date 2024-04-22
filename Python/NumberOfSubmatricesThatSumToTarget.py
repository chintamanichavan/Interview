class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        rows, cols = len(matrix), len(matrix[0])
        # Calculate prefix sum for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        count = 0
        # Iterate over pairs of columns
        for c1 in range(cols):
            for c2 in range(c1, cols):
                sums = {0: 1}
                cur_sum = 0
                # Calculate the cumulative sum for the submatrix and count submatrices summing to target
                for r in range(rows):
                    cur_sum += matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    count += sums.get(cur_sum - target, 0)
                    sums[cur_sum] = sums.get(cur_sum, 0) + 1

        return count
