class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
            
        m, n = len(grid), len(grid[0])
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * (ones_row[i] + ones_col[j]) - m - n

        return diff
