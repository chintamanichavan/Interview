#include <iostream>
#include <numeric>
#include <vector>

class DSU {
public:
  DSU(int n) : parent(n), sz(n, 1) {
    std::iota(parent.begin(), parent.end(), 0);
  }
  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }
  void unite(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra != rb) {
      parent[ra] = rb;
      sz[rb] += sz[ra];
    }
  }
  int size(int x) { return sz[find(x)]; }

private:
  std::vector<int> parent, sz;
};

class Solution {
public:
  std::vector<int> hitBricks(std::vector<std::vector<int>> &grid,
                             std::vector<std::vector<int>> &hits) {
    int m = (int)grid.size(), n = (int)grid[0].size();
    int top = m * n;
    DSU d(m * n + 1);
    auto idx = [&](int r, int c) { return r * n + c; };

    auto g = grid;
    for (auto &h : hits)
      g[h[0]][h[1]] = 0;

    for (int r = 0; r < m; ++r)
      for (int c = 0; c < n; ++c)
        if (g[r][c] == 1) {
          if (r == 0)
            d.unite(idx(r, c), top);
          if (r > 0 && g[r - 1][c] == 1)
            d.unite(idx(r, c), idx(r - 1, c));
          if (c > 0 && g[r][c - 1] == 1)
            d.unite(idx(r, c), idx(r, c - 1));
        }

    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    std::vector<int> res(hits.size(), 0);
    for (int i = (int)hits.size() - 1; i >= 0; --i) {
      int r = hits[i][0], c = hits[i][1];
      if (grid[r][c] == 0)
        continue;
      int before = d.size(top);
      g[r][c] = 1;
      if (r == 0)
        d.unite(idx(r, c), top);
      for (auto &dd : dirs) {
        int nr = r + dd[0], nc = c + dd[1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && g[nr][nc] == 1)
          d.unite(idx(r, c), idx(nr, nc));
      }
      int after = d.size(top);
      res[i] = std::max(0, after - before - 1);
    }
    return res;
  }
};

void print(const std::vector<int> &v) {
  std::cout << "[";
  for (size_t i = 0; i < v.size(); ++i) {
    if (i)
      std::cout << ", ";
    std::cout << v[i];
  }
  std::cout << "]\n";
}

int main() {
  Solution s;
  std::vector<std::vector<int>> g1 = {{1, 0, 0, 0}, {1, 1, 1, 0}},
                                h1 = {{1, 0}};
  std::vector<std::vector<int>> g2 = {{1, 0, 0, 0}, {1, 1, 0, 0}},
                                h2 = {{1, 1}, {1, 0}};
  std::vector<std::vector<int>> g3 = {{1, 1, 1}, {0, 1, 0}, {0, 0, 0}},
                                h3 = {{0, 2}, {2, 0}, {0, 1}, {1, 2}};
  print(s.hitBricks(g1, h1)); // [2]
  print(s.hitBricks(g2, h2)); // [0, 0]
  print(s.hitBricks(g3, h3)); // [0, 0, 1, 0]
  return 0;
}
