#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

class Solution {
public:
    int calculateMinimumHP(std::vector<std::vector<int>>& dungeon) {
        int m = dungeon.size(), n = dungeon[0].size();
        std::vector<int> dp(n + 1, INT_MAX);
        dp[n - 1] = 1;
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int need = std::min(dp[j], dp[j + 1]) - dungeon[i][j];
                dp[j] = std::max(need, 1);
            }
        }
        return dp[0];
    }
};

int main() {
    Solution s;
    std::vector<std::vector<int>> a = {{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}};
    std::vector<std::vector<int>> b = {{0}};
    std::vector<std::vector<int>> c = {{100}};
    std::vector<std::vector<int>> d = {{-3}};
    std::cout << s.calculateMinimumHP(a) << "\n"; // 7
    std::cout << s.calculateMinimumHP(b) << "\n"; // 1
    std::cout << s.calculateMinimumHP(c) << "\n"; // 1
    std::cout << s.calculateMinimumHP(d) << "\n"; // 4
    return 0;
}
