#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, root, value, path):
        if not root:
            return False
        if root.val == value:
            return True
        path.append('L')
        if self.find_path(root.left, value, path):
            return True
        path.pop()
        path.append('R')
        if self.find_path(root.right, value, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        if not root:
            return ""

        path_to_start = []
        path_to_dest = []

        self.find_path(root, startValue, path_to_start)
        self.find_path(root, destValue, path_to_dest)

        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        directions = ['U'] * (len(path_to_start) - i) + path_to_dest[i:]
        return ''.join(directions)
        
# @lc code=end

