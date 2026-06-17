#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

class Solution {
public:
  int splitArray(std::vector<int> &nums, int k) {
    long long lo = *std::max_element(nums.begin(), nums.end());
    long long hi = std::accumulate(nums.begin(), nums.end(), 0LL);
    while (lo < hi) {
      long long mid = (lo + hi) / 2;
      if (needed(nums, mid) <= k)
        hi = mid;
      else
        lo = mid + 1;
    }
    return (int)lo;
  }

private:
  int needed(const std::vector<int> &nums, long long cap) {
    int count = 1;
    long long cur = 0;
    for (int x : nums) {
      if (cur + x > cap) {
        count++;
        cur = x;
      } else {
        cur += x;
      }
    }
    return count;
  }
};

int main() {
  Solution s;
  std::vector<int> a = {7, 2, 5, 10, 8}, b = {1, 2, 3, 4, 5}, c = {1, 4, 4};
  std::cout << s.splitArray(a, 2) << "\n"; // 18
  std::cout << s.splitArray(b, 2) << "\n"; // 9
  std::cout << s.splitArray(c, 3) << "\n"; // 4
  return 0;
}
