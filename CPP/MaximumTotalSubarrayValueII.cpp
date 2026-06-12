#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <vector>

class Solution {
public:
  long long maxTotalValue(std::vector<int> &nums, int k) {
    int n = (int)nums.size();
    std::vector<int> logt(n + 1, 0);
    for (int i = 2; i <= n; ++i)
      logt[i] = logt[i / 2] + 1;

    std::vector<std::vector<int>> upMax{nums}, upMin{nums};
    for (int j = 1; (1 << j) <= n; ++j) {
      int half = 1 << (j - 1), length = 1 << j;
      auto &pmx = upMax[j - 1];
      auto &pmn = upMin[j - 1];
      std::vector<int> cmx(n - length + 1), cmn(n - length + 1);
      for (int i = 0; i + length <= n; ++i) {
        cmx[i] = std::max(pmx[i], pmx[i + half]);
        cmn[i] = std::min(pmn[i], pmn[i + half]);
      }
      upMax.push_back(std::move(cmx));
      upMin.push_back(std::move(cmn));
    }
    auto value = [&](int l, int r) -> int {
      int j = logt[r - l + 1], shift = 1 << j;
      int mx = std::max(upMax[j][l], upMax[j][r - shift + 1]);
      int mn = std::min(upMin[j][l], upMin[j][r - shift + 1]);
      return mx - mn;
    };

    // max-heap of (value, l, r)
    std::priority_queue<std::tuple<int, int, int>> heap;
    std::unordered_set<long long> seen;
    auto key = [&](int l, int r) { return (long long)l * n + r; };
    heap.push({value(0, n - 1), 0, n - 1});
    seen.insert(key(0, n - 1));
    long long total = 0;
    for (int i = 0; i < k; ++i) {
      auto [v, l, r] = heap.top();
      heap.pop();
      total += v;
      if (l + 1 <= r && seen.insert(key(l + 1, r)).second) {
        heap.push({value(l + 1, r), l + 1, r});
      }
      if (l <= r - 1 && seen.insert(key(l, r - 1)).second) {
        heap.push({value(l, r - 1), l, r - 1});
      }
    }
    return total;
  }
};

int main() {
  Solution s;
  std::vector<int> a = {1, 3, 2}, b = {4, 2, 5, 1}, c = {1};
  std::cout << s.maxTotalValue(a, 2) << "\n"; // 4
  std::cout << s.maxTotalValue(b, 3) << "\n"; // 12
  std::cout << s.maxTotalValue(c, 1) << "\n"; // 0
  return 0;
}
