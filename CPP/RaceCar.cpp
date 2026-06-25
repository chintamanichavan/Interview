#include <iostream>
#include <queue>
#include <set>
#include <tuple>

class Solution {
public:
  int racecar(int target) {
    int bound = 2 * target;
    std::set<std::pair<int, int>> seen{{0, 1}};
    std::queue<std::tuple<int, int, int>> q; // pos, speed, steps
    q.push({0, 1, 0});
    while (!q.empty()) {
      auto [pos, speed, steps] = q.front();
      q.pop();
      if (pos == target)
        return steps;
      // 'A'
      int npos = pos + speed, nspeed = speed * 2;
      if (npos >= -bound && npos <= bound &&
          seen.insert({npos, nspeed}).second) {
        q.push({npos, nspeed, steps + 1});
      }
      // 'R'
      int rspeed = speed > 0 ? -1 : 1;
      if (seen.insert({pos, rspeed}).second) {
        q.push({pos, rspeed, steps + 1});
      }
    }
    return -1;
  }
};

int main() {
  Solution s;
  std::cout << s.racecar(3) << "\n"; // 2
  std::cout << s.racecar(6) << "\n"; // 5
  std::cout << s.racecar(1) << "\n"; // 1
  std::cout << s.racecar(4) << "\n"; // 5
  return 0;
}
