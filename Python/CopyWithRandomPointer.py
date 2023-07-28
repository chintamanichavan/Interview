class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        node = head
        while node:
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next

        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        old_list = head
        new_list = head.next
        head_old = old_list
        head_new = new_list
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next

        return head_new

def main():
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    s = Solution()
    res = s.copyRandomList(head)
    print(res)

if __name__ == '__main__':
    main()
