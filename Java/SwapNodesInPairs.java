import java.util.ArrayList;
import java.util.List;

public class SwapNodesInPairs {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int v) { this.val = v; }
    }

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode nxt = head.next;
        head.next = swapPairs(nxt.next);
        nxt.next = head;
        return nxt;
    }

    static ListNode build(int... vals) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : vals) {
            cur.next = new ListNode(v);
            cur = cur.next;
        }
        return dummy.next;
    }

    static List<Integer> toList(ListNode h) {
        List<Integer> out = new ArrayList<>();
        while (h != null) { out.add(h.val); h = h.next; }
        return out;
    }

    public static void main(String[] args) {
        SwapNodesInPairs s = new SwapNodesInPairs();
        System.out.println(toList(s.swapPairs(build(1, 2, 3, 4)))); // [2, 1, 4, 3]
        System.out.println(toList(s.swapPairs(build())));           // []
        System.out.println(toList(s.swapPairs(build(1))));          // [1]
        System.out.println(toList(s.swapPairs(build(1, 2, 3))));    // [2, 1, 3]
    }
}
