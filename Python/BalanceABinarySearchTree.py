
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform inorder traversal and collect values in a list
        def inorder_traversal(node):
            nodes = []
            def inorder(node):
                if node:
                    inorder(node.left)
                    nodes.append(node.val)
                    inorder(node.right)
            inorder(node)
            return nodes

        # Helper function to build balanced BST from sorted node values
        def build_balanced_bst(nodes, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nodes[mid])
            root.left = build_balanced_bst(nodes, start, mid - 1)
            root.right = build_balanced_bst(nodes, mid + 1, end)
            return root

        # Main function to balance BST
        nodes = inorder_traversal(root)
        return build_balanced_bst(nodes, 0, len(nodes) - 1)
