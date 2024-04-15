# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #in order dfs
        def recursive(root, value):
            #if root is None just return 0
            if not root:
                return 0
            #value is your previous value * 10 + your current value, because
            #1 -> 3 = 13 which  is 1 * 10 + 3
            val = value * 10 + root.val
            #if leaf node, return itself
            if not root.left and not root.right:
                return val
            #otherwise, go left and go right
            left_sum = recursive(root.left, val)
            right_sum = recursive(root.right, val)
            #add left and right together
            return left_sum + right_sum

        return recursive(root, 0)

