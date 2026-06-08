#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    int stoneGameVIII(std::vector<int>& stones) {
        int n = (int)stones.size();
        std::vector<long long> prefix(n);
        long long sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += stones[i];
            prefix[i] = sum;
        }
        long long dp = prefix[n - 1];
        for (int i = n - 2; i >= 1; --i) {
            dp = std::max(dp, prefix[i] - dp);
        }
        return (int)dp;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {-1, 2, -3, 4, -5};
    std::vector<int> b = {7, -6, 5, 10, 5, -2, -6};
    std::vector<int> c = {-10, -12};
    std::cout << s.stoneGameVIII(a) << "\n";  // 5
    std::cout << s.stoneGameVIII(b) << "\n";  // 13
    std::cout << s.stoneGameVIII(c) << "\n";  // -22
    return 0;
}
