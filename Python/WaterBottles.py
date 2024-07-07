#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            # Exchange empty bottles for full ones
            new_full_bottles = empty_bottles // numExchange
            total_drunk += new_full_bottles
            # Calculate the remaining empty bottles after the exchange
            empty_bottles = empty_bottles % numExchange + new_full_bottles
        
        return total_drunk        
# @lc code=end

