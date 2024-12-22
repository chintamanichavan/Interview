class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def kthSmallest(self, root, k):
        res = []

        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res[k-1]

def main():
    # Construct the binary search tree from the list
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    k = 1
    s = Solution()
    res = s.kthSmallest(root, k)
    print(res)

if __name__ == '__main__':
    main()
