class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 10**9 + 7
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        count = 0

        for move in range(1, maxMove + 1):
            for r in range(m):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            dp[move][r][c] += dp[move - 1][nr][nc]
                            dp[move][r][c] %= MOD
                        else:
                            count += dp[move - 1][r][c]
                            count %= MOD

        return count
