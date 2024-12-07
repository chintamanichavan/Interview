class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


def main():
    # Initialize the linked lists
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    # Create a Solution object
    solution = Solution()
    # Merge the linked lists
    merged_list = solution.mergeTwoLists(l1, l2)

    # Print the merged linked list
    cur = merged_list
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next


if __name__ == "__main__":
    main()
