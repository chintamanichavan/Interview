#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
  int swimInWater(std::vector<std::vector<int>> &grid) {
    int n = (int)grid.size();
    using T = std::tuple<int, int, int>; // (time, r, c)
    std::priority_queue<T, std::vector<T>, std::greater<T>> heap;
    std::vector<std::vector<bool>> seen(n, std::vector<bool>(n, false));
    heap.push({grid[0][0], 0, 0});
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (!heap.empty()) {
      auto [t, r, c] = heap.top();
      heap.pop();
      if (r == n - 1 && c == n - 1)
        return t;
      if (seen[r][c])
        continue;
      seen[r][c] = true;
      for (auto &d : dirs) {
        int nr = r + d[0], nc = c + d[1];
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc]) {
          heap.push({std::max(t, grid[nr][nc]), nr, nc});
        }
      }
    }
    return -1;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {{0, 2}, {1, 3}};
  std::vector<std::vector<int>> b = {{0, 1, 2, 3, 4},
                                     {24, 23, 22, 21, 5},
                                     {12, 13, 14, 15, 16},
                                     {11, 17, 18, 19, 20},
                                     {10, 9, 8, 7, 6}};
  std::vector<std::vector<int>> c = {{0}};
  std::cout << s.swimInWater(a) << "\n"; // 3
  std::cout << s.swimInWater(b) << "\n"; // 16
  std::cout << s.swimInWater(c) << "\n"; // 0
  return 0;
}
