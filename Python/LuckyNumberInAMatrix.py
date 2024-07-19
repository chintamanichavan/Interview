#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Find the minimum elements in each row along with their column indices
        min_in_rows = [(min(row), row.index(min(row))) for row in matrix]
        
        # Initialize the list to hold the lucky numbers
        lucky_nums = []
        
        # Check if the minimum element in a row is the maximum in its column
        for min_val, col_idx in min_in_rows:
            if all(min_val >= matrix[i][col_idx] for i in range(len(matrix))):
                lucky_nums.append(min_val)
        
        return lucky_nums

# Example usage:
# sol = Solution()
# print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))  # Output: [15]
# print(sol.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))  # Output: [12]
# print(sol.luckyNumbers([[7,8],[1,2]]))  # Output: [7]
        
# @lc code=end

