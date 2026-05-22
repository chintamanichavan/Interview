#include <initializer_list>
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v = 0, ListNode* n = nullptr) : val(v), next(n) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* nxt = head->next;
        head->next = swapPairs(nxt->next);
        nxt->next = head;
        return nxt;
    }
};

ListNode* build(std::initializer_list<int> vals) {
    ListNode dummy;
    ListNode* cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}

void print(ListNode* h) {
    std::cout << "[";
    bool first = true;
    while (h) {
        if (!first) std::cout << ", ";
        std::cout << h->val;
        first = false;
        h = h->next;
    }
    std::cout << "]\n";
}

void freeList(ListNode* h) {
    while (h) {
        ListNode* n = h->next;
        delete h;
        h = n;
    }
}

int main() {
    Solution s;
    for (auto vals : std::vector<std::vector<int>>{ {1, 2, 3, 4}, {}, {1}, {1, 2, 3} }) {
        ListNode dummy;
        ListNode* cur = &dummy;
        for (int v : vals) { cur->next = new ListNode(v); cur = cur->next; }
        ListNode* result = s.swapPairs(dummy.next);
        print(result);
        freeList(result);
    }
    return 0;
}
