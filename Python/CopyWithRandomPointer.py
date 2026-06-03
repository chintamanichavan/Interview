from typing import List, Optional


class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Interweave each copy right after its original: A -> A' -> B -> B' -> ...
        node = head
        while node:
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next

        # Wire the copies' random pointers from the originals'.
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        # Detangle the interleaved list back into original + copy.
        old_list = head
        new_list = head.next
        head_new = new_list
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next

        return head_new


def build(data: List[list]) -> Optional[Node]:
    # data[i] = [val, random_index_or_None]; nodes are linked in order.
    nodes = [Node(val) for val, _ in data]
    for i, (_, r) in enumerate(data):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def serialize(head: Optional[Node]) -> List[list]:
    index = {}
    order = []
    node = head
    while node:
        index[id(node)] = len(order)
        order.append(node)
        node = node.next
    return [[n.val, index[id(n.random)] if n.random else None] for n in order]


def main():
    data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    s = Solution()
    print(serialize(s.copyRandomList(build(data))))
    # [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]


if __name__ == '__main__':
    main()


# review 2026-01-10
