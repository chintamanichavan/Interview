class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def reverse_linked_list(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def partition(self, head, x):
        left_dummy = ListNode()
        right_dummy = ListNode()
        left_tail = left_dummy
        right_tail = right_dummy

        curr = head
        while curr:
            if curr.val < x:
                left_tail.next = curr
                left_tail = curr
            else:
                right_tail.next = curr
                right_tail = curr
            curr = curr.next

        right_tail.next = None
        left_tail.next = self.reverse_linked_list(right_dummy.next)

        return left_dummy.next

    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

# Test cases
def main():
    # Test case 1: Input: head = [1,4,3,2,5,2], x = 3
    head1 = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)
    node5 = ListNode(2)
    head1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    x1 = 3
    s = Solution()
    print("Original Linked List 1:")
    s.print_linked_list(head1)

    new_head1 = s.partition(head1, x1)

    print("Linked List 1 after Partition:")
    s.print_linked_list(new_head1)

    # Test case 2: Input: head = [2,1], x = 2
    head2 = ListNode(2)
    node6 = ListNode(1)
    head2.next = node6
    x2 = 2

    print("\nOriginal Linked List 2:")
    s.print_linked_list(head2)

    new_head2 = s.partition(head2, x2)

    print("Linked List 2 after Partition:")
    s.print_linked_list(new_head2)

# Test case
if __name__ == "__main__":
    main()
