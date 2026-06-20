#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int>
  findRedundantDirectedConnection(std::vector<std::vector<int>> &edges) {
    int n = (int)edges.size();
    std::vector<int> parent(n + 1, 0);
    std::vector<int> cand1, cand2;
    for (int i = 0; i < n; ++i) {
      int u = edges[i][0], v = edges[i][1];
      if (parent[v] != 0) {
        cand1 = {parent[v], v};
        cand2 = {u, v};
        edges[i][1] = 0; // disable cand2 in the union pass
      } else {
        parent[v] = u;
      }
    }

    uf.resize(n + 1);
    for (int i = 0; i <= n; ++i)
      uf[i] = i;
    for (auto &e : edges) {
      int u = e[0], v = e[1];
      if (v == 0)
        continue;
      int ru = find(u), rv = find(v);
      if (ru == rv)
        return cand1.empty() ? std::vector<int>{u, v} : cand1;
      uf[rv] = ru;
    }
    return cand2;
  }

private:
  std::vector<int> uf;
  int find(int x) {
    while (uf[x] != x) {
      uf[x] = uf[uf[x]];
      x = uf[x];
    }
    return x;
  }
};

void print(const std::vector<int> &v) {
  std::cout << "[" << v[0] << ", " << v[1] << "]\n";
}

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {{1, 2}, {1, 3}, {2, 3}};
  std::vector<std::vector<int>> b = {{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5}};
  std::vector<std::vector<int>> c = {{2, 1}, {3, 1}, {4, 2}, {1, 4}};
  print(s.findRedundantDirectedConnection(a)); // [2, 3]
  print(s.findRedundantDirectedConnection(b)); // [4, 1]
  print(s.findRedundantDirectedConnection(c)); // [2, 1]
  return 0;
}
