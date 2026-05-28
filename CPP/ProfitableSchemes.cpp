#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    int profitableSchemes(int n, int minProfit, std::vector<int>& group, std::vector<int>& profit) {
        constexpr int MOD = 1'000'000'007;
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(minProfit + 1, 0));
        dp[0][0] = 1;
        for (size_t i = 0; i < group.size(); ++i) {
            int g = group[i], p = profit[i];
            for (int j = n; j >= g; --j) {
                for (int k = minProfit; k >= 0; --k) {
                    if (!dp[j - g][k]) continue;
                    int nk = std::min(k + p, minProfit);
                    dp[j][nk] = (dp[j][nk] + dp[j - g][k]) % MOD;
                }
            }
        }
        long long total = 0;
        for (int j = 0; j <= n; ++j) total = (total + dp[j][minProfit]) % MOD;
        return (int)total;
    }
};

int main() {
    Solution s;
    std::vector<int> g1 = {2, 2}, p1 = {2, 3};
    std::vector<int> g2 = {2, 3, 5}, p2 = {6, 7, 8};
    std::vector<int> g3 = {1, 1}, p3 = {1, 1};
    std::cout << s.profitableSchemes(5, 3, g1, p1) << "\n";  // 2
    std::cout << s.profitableSchemes(10, 5, g2, p2) << "\n"; // 7
    std::cout << s.profitableSchemes(1, 1, g3, p3) << "\n";  // 2
    return 0;
}
