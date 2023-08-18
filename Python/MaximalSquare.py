class Solution():
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        dp = [[0] * N for _ in range(M)]
        maxSide = 0

        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide


def main():
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    s = Solution()
    res = s.maximalSquare(matrix)
    print(res)

if __name__ == '__main__':
    main()
