from typing import ListNode

def mergeTwoLists1(l1, l2):
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

l1 = [1,2,4]
l2 = [1,3,4]
mergeTwoLists1(l1,l2)