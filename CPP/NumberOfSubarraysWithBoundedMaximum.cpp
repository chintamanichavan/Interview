#include <iostream>
#include <vector>

class Solution {
public:
  int numSubarrayBoundedMax(std::vector<int> &nums, int left, int right) {
    return count(nums, right) - count(nums, left - 1);
  }

private:
  int count(const std::vector<int> &nums, int bound) {
    int total = 0, length = 0;
    for (int x : nums) {
      length = (x <= bound) ? length + 1 : 0;
      total += length;
    }
    return total;
  }
};

int main() {
  Solution s;
  std::vector<int> a = {2, 1, 4, 3}, b = {2, 9, 2, 5, 6}, c = {1, 1, 1};
  std::cout << s.numSubarrayBoundedMax(a, 2, 3) << "\n"; // 3
  std::cout << s.numSubarrayBoundedMax(b, 2, 8) << "\n"; // 7
  std::cout << s.numSubarrayBoundedMax(c, 1, 1) << "\n"; // 6
  return 0;
}
