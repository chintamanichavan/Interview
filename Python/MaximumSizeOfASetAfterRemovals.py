class Solution:
    def maximumSetSize(self, v1, v2):
        s1 = set(v1)
        s2 = set(v2)
        n, m = len(v1), len(v2)
        x, y = len(s1), len(s2)
        ans = min(n // 2, x)
        rem = x - ans
        c = 0
        for i in s2:
            if i not in s1:
                c += 1
            elif rem > 0:
                c += 1
                rem -= 1
            if c >= m // 2:
                break
        return ans + c