from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nxt = head.next
        head.next = self.swapPairs(nxt.next)
        nxt.next = head
        return nxt


def build(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == '__main__':
    s = Solution()
    print(to_list(s.swapPairs(build([1, 2, 3, 4]))))  # [2, 1, 4, 3]
    print(to_list(s.swapPairs(build([]))))            # []
    print(to_list(s.swapPairs(build([1]))))           # [1]
    print(to_list(s.swapPairs(build([1, 2, 3]))))     # [2, 1, 3]
