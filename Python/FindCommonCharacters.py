
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the first word's character counts
        common_count = Counter(words[0])

        # Intersect the counts with each subsequent word's character counts
        for word in words[1:]:
            common_count &= Counter(word)

        # Expand the characters into a list with the correct counts
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result
