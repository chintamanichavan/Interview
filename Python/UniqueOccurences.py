class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        freq = Counter(arr)
        freq_counts = set(freq.values())
        return len(freq_counts) == len(freq)

# review 2026-05-08
