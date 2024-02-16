class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # Count the frequencies
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        # Remove k elements
        for num, count in sorted_freq:
            if k >= count:
                k -= count
                del freq[num]
            else:
                break

        # Return the number of remaining unique elements
        return len(freq)
