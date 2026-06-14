#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
  std::vector<int> smallestRange(std::vector<std::vector<int>> &nums) {
    using T = std::tuple<int, int, int>; // (val, list, idx)
    std::priority_queue<T, std::vector<T>, std::greater<T>> heap;
    int curMax = INT_MIN;
    for (int i = 0; i < (int)nums.size(); ++i) {
      heap.push({nums[i][0], i, 0});
      curMax = std::max(curMax, nums[i][0]);
    }
    std::vector<int> best = {std::get<0>(heap.top()), curMax};
    while (true) {
      auto [val, i, j] = heap.top();
      heap.pop();
      if (curMax - val < best[1] - best[0])
        best = {val, curMax};
      if (j + 1 == (int)nums[i].size())
        break;
      int nxt = nums[i][j + 1];
      curMax = std::max(curMax, nxt);
      heap.push({nxt, i, j + 1});
    }
    return best;
  }
};

void print(const std::vector<int> &v) {
  std::cout << "[" << v[0] << ", " << v[1] << "]\n";
}

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {
      {4, 10, 15, 24, 26}, {0, 9, 12, 20}, {5, 18, 22, 30}};
  std::vector<std::vector<int>> b = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};
  std::vector<std::vector<int>> c = {{1}, {2}, {3}};
  print(s.smallestRange(a)); // [20, 24]
  print(s.smallestRange(b)); // [1, 1]
  print(s.smallestRange(c)); // [1, 3]
  return 0;
}
