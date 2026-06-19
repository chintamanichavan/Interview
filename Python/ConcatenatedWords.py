from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # A word qualifies if it splits into >= 2 words from the set. Word-break DP per word:
        # dp[i] = word[:i] is formable from set words. Forbidding the full-word match (j==0 and
        # i==n) guarantees every piece is strictly shorter, so reaching dp[n] needs >= 2 pieces.
        word_set = set(words)

        def can_form(word: str) -> bool:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j] or (j == 0 and i == n):
                        continue
                    if word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]

        return [w for w in words if w and can_form(w)]


if __name__ == "__main__":
    s = Solution()
    print(
        s.findAllConcatenatedWordsInADict(
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ]
        )
    )
    # ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']
    print(s.findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]))  # ['catdog']
    print(s.findAllConcatenatedWordsInADict(["a", "b", "ab", "abc"]))  # ['ab']
