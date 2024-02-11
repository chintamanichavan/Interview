class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        from collections import Counter
        # Count character occurrences
        count = Counter(s)

        # Find the index of the first unique character
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx

        return -1
