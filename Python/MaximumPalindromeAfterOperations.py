class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt, res = Counter([ch for w in words for ch in w]), 0
        pairs = sum(char_cnt // 2 for char_cnt in cnt.values())
        for sz in sorted([len(w) for w in words]):
            pairs -= sz // 2
            res += pairs >= 0
        return res