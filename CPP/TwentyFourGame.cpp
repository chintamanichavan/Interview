#include <cmath>
#include <iostream>
#include <vector>

class Solution {
public:
  bool judgePoint24(std::vector<int> &cards) {
    std::vector<double> nums(cards.begin(), cards.end());
    return solve(nums);
  }

private:
  static constexpr double EPS = 1e-6;

  bool solve(std::vector<double> &nums) {
    int n = (int)nums.size();
    if (n == 1)
      return std::fabs(nums[0] - 24.0) < EPS;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j)
          continue;
        std::vector<double> rest;
        for (int x = 0; x < n; ++x)
          if (x != i && x != j)
            rest.push_back(nums[x]);
        double a = nums[i], b = nums[j];
        std::vector<double> cands = {a + b, a - b, a * b};
        if (std::fabs(b) > EPS)
          cands.push_back(a / b);
        for (double val : cands) {
          rest.push_back(val);
          if (solve(rest))
            return true;
          rest.pop_back();
        }
      }
    }
    return false;
  }
};

int main() {
  Solution s;
  std::vector<int> a = {4, 1, 8, 7}, b = {1, 2, 1, 2}, c = {3, 3, 8, 8},
                   d = {1, 1, 1, 1};
  std::cout << std::boolalpha;
  std::cout << s.judgePoint24(a) << "\n"; // true
  std::cout << s.judgePoint24(b) << "\n"; // false
  std::cout << s.judgePoint24(c) << "\n"; // true
  std::cout << s.judgePoint24(d) << "\n"; // false
  return 0;
}
