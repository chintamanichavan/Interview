#include <iostream>
#include <queue>
#include <vector>

class Solution {
public:
    bool canReach(std::vector<int>& arr, int start) {
        int n = arr.size();
        std::vector<bool> seen(n, false);
        std::queue<int> q;
        q.push(start);
        seen[start] = true;
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            if (arr[i] == 0) return true;
            for (int j : {i + arr[i], i - arr[i]}) {
                if (j >= 0 && j < n && !seen[j]) {
                    seen[j] = true;
                    q.push(j);
                }
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    std::vector<int> a1 = {4, 2, 3, 0, 3, 1, 2};
    std::vector<int> a2 = {3, 0, 2, 1, 2};
    std::cout << std::boolalpha;
    std::cout << s.canReach(a1, 5) << "\n"; // true
    std::cout << s.canReach(a1, 0) << "\n"; // true
    std::cout << s.canReach(a2, 2) << "\n"; // false
    return 0;
}
