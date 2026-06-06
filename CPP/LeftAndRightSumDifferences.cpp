#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> leftRightDifference(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        std::vector<int> ans(nums.size());
        int left = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            int right = total - left - nums[i];
            ans[i] = std::abs(left - right);
            left += nums[i];
        }
        return ans;
    }
};

void print(const std::vector<int>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << v[i];
    }
    std::cout << "]\n";
}

int main() {
    Solution s;
    std::vector<int> a = {10, 4, 8, 3};
    std::vector<int> b = {1};
    print(s.leftRightDifference(a));  // [15, 1, 11, 22]
    print(s.leftRightDifference(b));  // [0]
    return 0;
}
