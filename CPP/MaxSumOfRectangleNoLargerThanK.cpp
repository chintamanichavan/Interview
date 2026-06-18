#include <climits>
#include <iostream>
#include <set>
#include <vector>

class Solution {
public:
  int maxSumSubmatrix(std::vector<std::vector<int>> &matrix, int k) {
    int m = (int)matrix.size(), n = (int)matrix[0].size();
    long long best = LLONG_MIN;
    for (int left = 0; left < n; ++left) {
      std::vector<long long> rowsum(m, 0);
      for (int right = left; right < n; ++right) {
        for (int i = 0; i < m; ++i)
          rowsum[i] += matrix[i][right];
        std::set<long long> prefixes{0};
        long long cur = 0;
        for (long long v : rowsum) {
          cur += v;
          auto it = prefixes.lower_bound(cur - k);
          if (it != prefixes.end())
            best = std::max(best, cur - *it);
          prefixes.insert(cur);
        }
      }
    }
    return (int)best;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {{1, 0, 1}, {0, -2, 3}};
  std::vector<std::vector<int>> b = {{2, 2, -1}};
  std::cout << s.maxSumSubmatrix(a, 2) << "\n"; // 2
  std::cout << s.maxSumSubmatrix(b, 3) << "\n"; // 3
  std::cout << s.maxSumSubmatrix(b, 0) << "\n"; // -1
  return 0;
}
