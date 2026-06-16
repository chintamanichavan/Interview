#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  int longestIncreasingPath(std::vector<std::vector<int>> &matrix) {
    m = (int)matrix.size();
    n = (int)matrix[0].size();
    grid = &matrix;
    memo.assign(m, std::vector<int>(n, 0));
    int ans = 0;
    for (int r = 0; r < m; ++r)
      for (int c = 0; c < n; ++c)
        ans = std::max(ans, dfs(r, c));
    return ans;
  }

private:
  int m, n;
  std::vector<std::vector<int>> *grid = nullptr;
  std::vector<std::vector<int>> memo;
  static constexpr int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

  int dfs(int r, int c) {
    if (memo[r][c])
      return memo[r][c];
    auto &g = *grid;
    int best = 1;
    for (auto &d : dirs) {
      int nr = r + d[0], nc = c + d[1];
      if (nr >= 0 && nr < m && nc >= 0 && nc < n && g[nr][nc] > g[r][c]) {
        best = std::max(best, 1 + dfs(nr, nc));
      }
    }
    return memo[r][c] = best;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {{9, 9, 4}, {6, 6, 8}, {2, 1, 1}};
  std::vector<std::vector<int>> b = {{3, 4, 5}, {3, 2, 6}, {2, 2, 1}};
  std::vector<std::vector<int>> c = {{1}};
  std::cout << s.longestIncreasingPath(a) << "\n"; // 4
  std::cout << s.longestIncreasingPath(b) << "\n"; // 4
  std::cout << s.longestIncreasingPath(c) << "\n"; // 1
  return 0;
}
