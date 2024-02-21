class Solution(object):
    def finalString(self, s):
        d = s.count("i")
        if not d: return s
        res = [""] * (len(s) - d)
        st, end, d = 0, len(res) - 1, 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'i': d ^= 1
            elif d: res[end], end = s[i], end - 1
            else: res[st], st = s[i], st + 1

        return "".join(res)
