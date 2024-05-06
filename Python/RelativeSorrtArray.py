
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        # Create a count map for arr1
        count_map = Counter(arr1)

        # Initialize the result list
        result = []

        # Add elements from arr2 to the result list
        for num in arr2:
            result.extend([num] * count_map[num])
            del count_map[num]

        # Sort and add remaining elements
        remaining_elements = sorted(count_map.elements())
        result.extend(remaining_elements)

        return result
