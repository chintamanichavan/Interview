#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        current_sum = 0
        node = head.next  # Skipping the initial zero

        while node:
            if node.val == 0:
                current.next = ListNode(current_sum)
                current = current.next
                current_sum = 0
            else:
                current_sum += node.val
            node = node.next

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list (for easy verification)
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

