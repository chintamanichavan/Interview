#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int slidingPuzzle(std::vector<std::vector<int>>& board) {
        const std::vector<std::vector<int>> neighbors = {
            {1, 3}, {0, 2, 4}, {1, 5},
            {0, 4}, {1, 3, 5}, {2, 4}
        };
        std::string start(6, '0');
        int zero = 0;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                int idx = i * 3 + j;
                start[idx] = '0' + board[i][j];
                if (board[i][j] == 0) zero = idx;
            }
        }
        const std::string target = "123450";
        if (start == target) return 0;

        std::queue<std::tuple<std::string, int, int>> q;
        q.emplace(start, zero, 0);
        std::unordered_set<std::string> seen{start};
        while (!q.empty()) {
            auto [state, z, steps] = q.front(); q.pop();
            for (int nb : neighbors[z]) {
                std::string nxt = state;
                std::swap(nxt[z], nxt[nb]);
                if (nxt == target) return steps + 1;
                if (seen.insert(nxt).second) {
                    q.emplace(nxt, nb, steps + 1);
                }
            }
        }
        return -1;
    }
};

int main() {
    Solution s;
    std::vector<std::vector<int>> a = {{1, 2, 3}, {4, 0, 5}};
    std::vector<std::vector<int>> b = {{1, 2, 3}, {5, 4, 0}};
    std::vector<std::vector<int>> c = {{4, 1, 2}, {5, 0, 3}};
    std::vector<std::vector<int>> d = {{1, 2, 3}, {4, 5, 0}};
    std::cout << s.slidingPuzzle(a) << "\n"; // 1
    std::cout << s.slidingPuzzle(b) << "\n"; // -1
    std::cout << s.slidingPuzzle(c) << "\n"; // 5
    std::cout << s.slidingPuzzle(d) << "\n"; // 0
    return 0;
}
