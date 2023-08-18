class Solution():
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]  # return if string s can be segmented into words in the wordDicts


def main():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    res = sol.wordBreak(s,wordDict)
    print(res)

if __name__ == '__main__':
    main()
