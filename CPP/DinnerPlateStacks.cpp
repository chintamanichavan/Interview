#include <iostream>
#include <queue>
#include <string>
#include <vector>

class DinnerPlates {
public:
    explicit DinnerPlates(int capacity) : cap(capacity) {}

    void push(int val) {
        // Drop stale indices: out of range or already full.
        while (!avail.empty() &&
               (avail.top() >= (int)stacks.size() || (int)stacks[avail.top()].size() >= cap)) {
            avail.pop();
        }
        if (avail.empty()) {
            avail.push((int)stacks.size());
            stacks.emplace_back();
        }
        int i = avail.top();
        stacks[i].push_back(val);
        if ((int)stacks[i].size() >= cap) avail.pop();
    }

    int pop() {
        while (!stacks.empty() && stacks.back().empty()) stacks.pop_back();
        if (stacks.empty()) return -1;
        return popAtStack((int)stacks.size() - 1);
    }

    int popAtStack(int index) {
        if (index >= (int)stacks.size() || stacks[index].empty()) return -1;
        avail.push(index);
        int v = stacks[index].back();
        stacks[index].pop_back();
        return v;
    }

private:
    int cap;
    std::vector<std::vector<int>> stacks;
    std::priority_queue<int, std::vector<int>, std::greater<int>> avail;  // min-heap of indices
};

int main() {
    std::vector<std::string> ops = {"DinnerPlates", "push", "push", "push", "push", "push",
        "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"};
    std::vector<int> args = {2, 1, 2, 3, 4, 5, 0, 20, 21, 0, 2, 0, 0, 0, 0, 0};

    DinnerPlates* d = nullptr;
    std::string out = "[";
    for (size_t i = 0; i < ops.size(); ++i) {
        if (i) out += ", ";
        const std::string& op = ops[i];
        if (op == "DinnerPlates") {
            delete d;
            d = new DinnerPlates(args[i]);
            out += "null";
        } else if (op == "push") {
            d->push(args[i]);
            out += "null";
        } else if (op == "pop") {
            out += std::to_string(d->pop());
        } else {  // popAtStack
            out += std::to_string(d->popAtStack(args[i]));
        }
    }
    out += "]";
    std::cout << out << "\n";
    delete d;
    return 0;
}
