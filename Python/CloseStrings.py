class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        from collections import Counter

        # Check if both words have the same set of characters
        if set(word1) != set(word2):
            return False

        # Compare the sorted frequency counts of characters in both words
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
