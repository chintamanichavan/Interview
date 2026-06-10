#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> kSmallestPairs(std::vector<int> &nums1,
                                               std::vector<int> &nums2, int k) {
    std::vector<std::vector<int>> res;
    if (nums1.empty() || nums2.empty())
      return res;
    // min-heap of (sum, i, j)
    using T = std::tuple<int, int, int>;
    std::priority_queue<T, std::vector<T>, std::greater<T>> heap;
    for (int i = 0; i < (int)nums1.size() && i < k; ++i) {
      heap.push({nums1[i] + nums2[0], i, 0});
    }
    while (!heap.empty() && (int)res.size() < k) {
      auto [sum, i, j] = heap.top();
      heap.pop();
      res.push_back({nums1[i], nums2[j]});
      if (j + 1 < (int)nums2.size()) {
        heap.push({nums1[i] + nums2[j + 1], i, j + 1});
      }
    }
    return res;
  }
};

void print(const std::vector<std::vector<int>> &v) {
  std::cout << "[";
  for (size_t i = 0; i < v.size(); ++i) {
    if (i)
      std::cout << ", ";
    std::cout << "[" << v[i][0] << ", " << v[i][1] << "]";
  }
  std::cout << "]\n";
}

int main() {
  Solution s;
  std::vector<int> a1 = {1, 7, 11}, b1 = {2, 4, 6};
  std::vector<int> a2 = {1, 1, 2}, b2 = {1, 2, 3};
  std::vector<int> a3 = {1, 2}, b3 = {3};
  print(s.kSmallestPairs(a1, b1, 3)); // [[1, 2], [1, 4], [1, 6]]
  print(s.kSmallestPairs(a2, b2, 2)); // [[1, 1], [1, 1]]
  print(s.kSmallestPairs(a3, b3, 3)); // [[1, 3], [2, 3]]
  return 0;
}
