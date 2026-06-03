from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, currentSum, path):
            if not node:
                return

            currentSum += node.val
            path.append(node.val)

            # Record the path only at a leaf whose root-to-leaf sum hits the target.
            if not node.left and not node.right and currentSum == targetSum:
                result.append(list(path))
            else:
                dfs(node.left, currentSum, path)
                dfs(node.right, currentSum, path)

            path.pop()  # backtrack

        dfs(root, 0, [])
        return result


def main():
    # [5,4,8,11,null,13,4,7,2,null,null,5,1], target 22
    root = TreeNode(5,
                    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    s = Solution()
    print(s.pathSum(root, 22))  # [[5, 4, 11, 2], [5, 8, 4, 5]]
    print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))  # []


if __name__ == '__main__':
    main()


# review 2025-07-21

# review 2025-10-21
