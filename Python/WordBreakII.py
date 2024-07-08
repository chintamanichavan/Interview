from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(index):
            if index in memo:
                return memo[index]

            if index == len(s):
                return [""]

            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    for sentence in backtrack(end):
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[index] = sentences
            return sentences

        return backtrack(0)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and​⬤
