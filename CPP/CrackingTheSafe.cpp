#include <iostream>
#include <string>
#include <unordered_set>

class Solution {
public:
  std::string crackSafe(int n, int k) {
    if (n == 1) {
      std::string s;
      for (int d = 0; d < k; ++d)
        s += char('0' + d);
      return s;
    }
    K = k;
    path.clear();
    seen.clear();
    std::string start(n - 1, '0');
    dfs(start);
    return path + start;
  }

private:
  int K;
  std::string path;
  std::unordered_set<std::string> seen;

  void dfs(const std::string &node) {
    for (int d = 0; d < K; ++d) {
      std::string edge = node + char('0' + d);
      if (!seen.count(edge)) {
        seen.insert(edge);
        dfs(edge.substr(1));
        path += char('0' + d);
      }
    }
  }
};

int main() {
  Solution s;
  std::cout << s.crackSafe(1, 2) << "\n"; // 01
  std::cout << s.crackSafe(2, 2) << "\n"; // 01100
  std::cout << s.crackSafe(3, 2) << "\n"; // 0011101000
  std::cout << s.crackSafe(2, 3) << "\n"; // 0221120100
  return 0;
}
