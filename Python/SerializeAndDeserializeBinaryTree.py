from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Level-order (BFS) encoding: each node emits its value, each missing child emits '#'.
    # Decoding replays the queue, attaching children as their tokens are consumed.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append("#")
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if tokens[i] != "#":
                node.left = TreeNode(int(tokens[i]))
                q.append(node.left)
            i += 1
            if tokens[i] != "#":
                node.right = TreeNode(int(tokens[i]))
                q.append(node.right)
            i += 1
        return root


def to_list(root):
    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        out.append(node.val if node else None)
        if node:
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    c = Codec()
    # [1,2,3,null,null,4,5]
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = c.serialize(root)
    print(data)
    print(to_list(c.deserialize(data)))  # [1, 2, 3, None, None, 4, 5]
    print(repr(c.serialize(c.deserialize(c.serialize(None)))))  # ''
    single = TreeNode(7)
    print(to_list(c.deserialize(c.serialize(single))))  # [7]
