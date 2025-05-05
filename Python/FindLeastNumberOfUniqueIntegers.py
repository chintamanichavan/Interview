class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        """
        Finds the least number of unique integers after removing exactly k elements from the array.

        Args:
            arr: A list of integers.
            k: The number of elements to remove.

        Returns:
            The least number of unique integers after removing k elements.
        """

        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1): 
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key
        return remaining