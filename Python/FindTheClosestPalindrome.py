class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # The closest palindrome comes from one of a few candidates: mirror the left half of n,
        # and the left half +/- 1 mirrored (handles carries/borrows like 999->1001, 100->99),
        # plus the all-9s and 10..0-1 boundaries for length changes. Pick the closest, ties to
        # the smaller value.
        length = len(n)
        num = int(n)
        candidates = set()
        # length-changing boundaries: 99..9 (one shorter) and 100..01 (one longer)
        candidates.add(10 ** (length - 1) - 1)
        candidates.add(10**length + 1)

        prefix = int(n[: (length + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)
            if length % 2 == 0:
                cand = s + s[::-1]
            else:
                cand = s + s[-2::-1]
            candidates.add(int(cand))

        candidates.discard(num)  # must be a different number
        best = None
        for c in candidates:
            if c < 0:
                continue
            if (
                best is None
                or abs(c - num) < abs(best - num)
                or (abs(c - num) == abs(best - num) and c < best)
            ):
                best = c
        return str(best)


if __name__ == "__main__":
    s = Solution()
    print(s.nearestPalindromic("123"))  # 121
    print(s.nearestPalindromic("1"))  # 0
    print(s.nearestPalindromic("10"))  # 9
    print(s.nearestPalindromic("1000"))  # 999
    print(s.nearestPalindromic("999"))  # 1001
