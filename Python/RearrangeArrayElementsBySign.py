class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearranges the elements of an array such that:
        - Every consecutive pair of integers have opposite signs.
        - For all integers with the same sign, the order in which they were present in nums is preserved.
        - The rearranged array begins with a positive integer.

        Args:
            nums: A 0-indexed integer array of even length consisting of an equal number of positive and negative integers.

        Returns:
            The rearranged array.
        """

        pos = []  # Stores positive integers
        neg = []  # Stores negative integers

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        # Alternate positive and negative integers, starting with positive
        result = []
        i, j = 0, 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        # Add any remaining elements
        result.extend(pos[i:])
        result.extend(neg[j:])

        return result
