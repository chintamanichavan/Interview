class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        na=ord('a')
        qu=deque([(root,chr(na+root.val))])
        res=""
        while qu:
            node,val=qu.pop()
            if not node.left and not node.right:
                    if res=="":
                        res=val
                    else:
                        res=min(res,val)
            else:
                if node.left:
                    qu.append((node.left,chr(na+node.left.val)+val))
                if node.right:
                    qu.append((node.right,chr(na+node.right.val)+val))
        return res
