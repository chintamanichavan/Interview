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


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])))
    # ['cat sand dog', 'cats and dog']
    print(sorted(sol.wordBreak("pineapplepenapple",
                               ["apple", "pen", "applepen", "pine", "pineapple"])))
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # []


# review 2024-10-24

# review 2026-01-17
