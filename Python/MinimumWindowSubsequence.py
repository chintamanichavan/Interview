class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # Two-pointer: scan s1 advancing j through s2; when all of s2 is matched ending at i,
        # walk left re-matching s2 backwards to find the tightest start, record the window, then
        # restart matching from that start. Leftmost-shortest wins. O(|s1| * |s2|) worst case.
        m, n = len(s1), len(s2)
        i = j = 0
        start, best = -1, m + 1
        while i < m:
            if s1[i] == s2[j]:
                j += 1
                if j == n:
                    right = i
                    j -= 1
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1
                    i += 1  # i now points at the window's left end
                    if right - i + 1 < best:
                        best = right - i + 1
                        start = i
                    j = 0
            i += 1
        return "" if start == -1 else s1[start : start + best]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("abcdebdde", "bde"))  # bcde
    print(s.minWindow("abc", "ac"))  # abc
    print(s.minWindow("abcde", "xyz"))  # (empty)
