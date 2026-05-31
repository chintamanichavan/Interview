class Solution:
    def numDecodings(self, s: str) -> int:
        # DP with two helpers: one(c) = ways to decode the single char c (1, 9, or 0);
        # two(c1, c2) = ways to decode the pair as a single 10..26 letter.
        # dp[i] = one(s[i-1]) * dp[i-1] + two(s[i-2], s[i-1]) * dp[i-2]. Rolling two scalars.
        MOD = 10**9 + 7

        def one(c: str) -> int:
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1

        def two(c1: str, c2: str) -> int:
            if c1 == '1':
                return 9 if c2 == '*' else 1   # 11..19, or 1X for any digit X (10..19 all valid)
            if c1 == '2':
                if c2 == '*':
                    return 6                    # 21..26
                return 1 if '0' <= c2 <= '6' else 0
            if c1 == '*':
                if c2 == '*':
                    return 15                   # 11..19 + 21..26
                if '0' <= c2 <= '6':
                    return 2                    # 1c2 (10..16) and 2c2 (20..26)
                return 1                        # only 1c2 (17..19)
            return 0

        n = len(s)
        prev2, prev1 = 1, one(s[0])
        for i in range(1, n):
            cur = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % MOD
            prev2, prev1 = prev1, cur
        return prev1 % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("*"))   # 9
    print(s.numDecodings("1*"))  # 18
    print(s.numDecodings("2*"))  # 15
    print(s.numDecodings("0"))   # 0
    print(s.numDecodings("**"))  # 96
    print(s.numDecodings("*1"))  # 11
