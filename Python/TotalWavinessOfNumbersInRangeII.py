from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Waviness = # interior digits that are a strict local peak or valley. By linearity,
        # total over a range = count of (number, middle-position) pairs forming a peak/valley.
        # Digit DP left-to-right: placing digit d after two real digits (prev2, prev1) decides
        # whether prev1 is a peak/valley via the triple (prev2, prev1, d). prev = -1 means "no
        # real digit yet" (leading-zero region or not enough digits to form a neighbor).
        def F(n: int) -> int:
            if n < 0:
                return 0
            s = [int(c) for c in str(n)]
            L = len(s)

            @lru_cache(maxsize=None)
            def dp(pos: int, started: bool, prev2: int, prev1: int, tight: bool):
                # returns (count_of_completions, total_waviness_events_from_here_on)
                if pos == L:
                    return (1, 0)
                limit = s[pos] if tight else 9
                cnt = tot = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    if not started and d == 0:
                        nstarted, np2, np1, event = False, -1, -1, 0
                    else:
                        nstarted = True
                        event = 0
                        if prev1 != -1 and prev2 != -1 and (
                            (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d)
                        ):
                            event = 1
                        np2, np1 = prev1, d
                    sc, st = dp(pos + 1, nstarted, np2, np1, ntight)
                    cnt += sc
                    tot += st + event * sc
                return (cnt, tot)

            res = dp(0, False, -1, -1, True)[1]
            dp.cache_clear()
            return res

        return F(num2) - F(num1 - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.totalWaviness(120, 130))    # 3
    print(s.totalWaviness(198, 202))    # 3
    print(s.totalWaviness(4848, 4848))  # 2
    print(s.totalWaviness(1, 1000))     # larger sanity case
