#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            
            if not node.left and not node.right:
                res = [0] * (distance + 1)
                res[1] = 1
                return res
            
            left_counts = dfs(node.left)
            right_counts = dfs(node.right)
            
            # Count good leaf pairs
            for i in range(1, distance + 1):
                for j in range(1, distance + 1):
                    if i + j <= distance:
                        result[0] += left_counts[i] * right_counts[j]
            
            # Merge distances
            new_counts = [0] * (distance + 1)
            for i in range(1, distance):
                new_counts[i + 1] = left_counts[i] + right_counts[i]
            
            return new_counts
        
        result = [0]
        dfs(root)
        return result[0]

# Example test cases
root1 = TreeNode(1)
root1.left = TreeNode(2, None, TreeNode(4))
root1.right = TreeNode(3)
distance1 = 3

root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(4), TreeNode(5))
root2.right = TreeNode(3, TreeNode(6), TreeNode(7))
distance2 = 3

root3 = TreeNode(7)
root3.left = TreeNode(1, TreeNode(6))
root3.right = TreeNode(4, TreeNode(5), TreeNode(3, None, TreeNode(2)))
distance3 = 3

solution = Solution()
print(solution.countPairs(root1, distance1))  # Output: 1
print(solution.countPairs(root2, distance2))  # Output: 2
print(solution.countPairs(root3, distance3))  # Output: 1

        
# @lc code=end

