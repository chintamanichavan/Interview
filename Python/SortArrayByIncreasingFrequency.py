#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, nums):
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Create a list of buckets where index represents the frequency
        max_freq = max(freq.values())
        buckets = defaultdict(list)
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Sort each bucket in decreasing order
        for key in buckets:
            buckets[key].sort(reverse=True)
        
        # Construct the result based on the buckets
        result = []
        for i in range(1, max_freq + 1):
            if i in buckets:
                for num in buckets[i]:
                    result.extend([num] * i)
        
        return result
        
# @lc code=end

