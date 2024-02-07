class Solution:
    def frequencySort(self, s: str) -> str:
        
        from collections import Counter

        # Count the frequency of each character
        freq_map = Counter(s)

        # Sort characters by frequency and then lexicographically
        sorted_chars = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))

        # Build the result string
        result = ''.join(char * freq for char, freq in sorted_chars)

        return result
