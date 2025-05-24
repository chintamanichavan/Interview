class Solution:
    
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # Initialize dp array
        dp = [[0] * (n + 1) for _ in range(5)]
        
        # Base case
        for i in range(5):
            dp[i][1] = 1
        
        # Fill dp array
        for j in range(2, n + 1):
            # 'a' -> 'e'
            dp[0][j] = dp[1][j-1] % MOD
            # 'e' -> 'a' or 'i'
            dp[1][j] = (dp[0][j-1] + dp[2][j-1]) % MOD
            # 'i' -> 'a' or 'e' or 'o' or 'u'
            dp[2][j] = (dp[0][j-1] + dp[1][j-1] + dp[3][j-1] + dp[4][j-1]) % MOD
            # 'o' -> 'i' or 'u'
            dp[3][j] = (dp[2][j-1] + dp[4][j-1]) % MOD
            # 'u' -> 'a'
            dp[4][j] = dp[0][j-1] % MOD
        
        return sum(dp[i][n] for i in range(5)) % MOD
