class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        # DP memoization table
        dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c1, c2):
            # If out of bounds, return 0
            if r < 0 or r >= rows or c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0

            # If already computed, return the value
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]

            # Calculate cherries picked up by both robots
            cherries = grid[r][c1]
            if c1 != c2:
                cherries += grid[r][c2]

            # If not the last row, explore all possible moves for both robots
            if r != rows - 1:
                maxCherries = 0
                for newC1 in [c1, c1 - 1, c1 + 1]:
                    for newC2 in [c2, c2 - 1, c2 + 1]:
                        maxCherries = max(maxCherries, dfs(r + 1, newC1, newC2))
                cherries += maxCherries

            # Store the result in the DP table
            dp[r][c1][c2] = cherries
            return cherries

        # Start the DFS from the top row, with both robots at their initial positions
        return dfs(0, 0, cols - 1)
