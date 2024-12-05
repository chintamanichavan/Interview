class Solution():
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for c, w in zip(pattern, words):
            if c in p2w and p2w[c] != w:
                return False
            if w in w2p and w2p[w] != c:
                return False

            p2w[c] = w
            w2p[w] = c

        return True


def main():
    pattern = "abba"
    s = "dog cat cat dog"
    s1 = Solution()
    res = s1.wordPattern(pattern,s)
    print(res)

if __name__ == '__main__':
    main()
