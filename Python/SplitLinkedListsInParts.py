class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitLinkedList(head, k):
    # Step 1: Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Calculate the size of each part and the number of extra nodes
    part_size = length // k
    extra_nodes = length % k
    
    result = []
    current = head
    
    for i in range(k):
        # Determine the size of the current part
        size = part_size + (1 if i < extra_nodes else 0)
        
        # Create a new part with its own head
        part_head = current
        for j in range(size - 1):
            if current:
                current = current.next
        
        # If there are more nodes, detach the next part
        if current:
            temp = current.next
            current.next = None
            current = temp
        
        # Add the head of the current part to the result
        result.append(part_head)
    
    return result

# Helper function to convert a list of ListNode into a list of lists
def convertToLists(heads):
    result = []
    for head in heads:
        current = head
        part = []
        while current:
            part.append(current.val)
            current = current.next
        result.append(part)
    return result

def main():
    head1 = ListNode(1, ListNode(2, ListNode(3)))
    print(convertToLists(splitLinkedList(head1, 5)))  # [[1], [2], [3], [], []]

    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    print(convertToLists(splitLinkedList(head2, 3)))  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]


if __name__ == '__main__':
    main()

# review 2024-07-27

# review 2025-08-04

# review 2025-11-21

# review 2026-02-27
