class Solution():

    # Optimal DP solution
    def climbStairs(n):
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

def main():
    n = 3
    s = Solution()
    res = s.climbStairs(n)
    print(res)

if __name__ == '__main__':
    main()
