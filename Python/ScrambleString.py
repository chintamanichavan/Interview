from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Recursion on substrings with memo. For every split point i, s1 is a scramble of s2
        # if either (no swap) the left i chars and right n-i chars both match, or (swap) s1's
        # left i matches s2's right i and s1's right n-i matches s2's left n-i.
        # Anagram pre-check prunes hopeless branches. O(n^4) states*work; n <= 30.
        @lru_cache(maxsize=None)
        def solve(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    return True
                if solve(a[:i], b[n - i:]) and solve(a[i:], b[:n - i]):
                    return True
            return False

        return solve(s1, s2)


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("great", "rgeat"))  # True
    print(s.isScramble("abcde", "caebd"))  # False
    print(s.isScramble("a", "a"))          # True
    print(s.isScramble("abc", "bca"))      # True
