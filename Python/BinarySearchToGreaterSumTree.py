class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def reverse_inorder(node):
            if not node:
                return
            # Traverse the right subtree
            reverse_inorder(node.right)
            # Update the current node's value
            self.sum += node.val
            node.val = self.sum
            # Traverse the left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
