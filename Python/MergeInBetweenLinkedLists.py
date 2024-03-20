# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # Step 1: Find the a-th node and the node before it
        a_prev = None
        curr = list1
        for _ in range(a):
            a_prev = curr
            curr = curr.next

        # Step 2: Find the b-th node and the node after it
        for _ in range(b - a + 1):
            curr = curr.next
        b_next = curr

        # Step 3: Connect a_prev to list2's head
        a_prev.next = list2

        # Step 4: Find list2's tail
        while list2.next:
            list2 = list2.next

        # Step 5: Connect list2's tail to b_next
        list2.next = b_next

        return list1
