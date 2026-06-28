#include <algorithm>
#include <climits>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
  bool isRectangleCover(std::vector<std::vector<int>> &rectangles) {
    long long area = 0;
    int minx = INT_MAX, miny = INT_MAX, maxx = INT_MIN, maxy = INT_MIN;
    std::set<std::pair<int, int>> corners;

    for (auto &r : rectangles) {
      int x1 = r[0], y1 = r[1], x2 = r[2], y2 = r[3];
      area += (long long)(x2 - x1) * (y2 - y1);
      minx = std::min(minx, x1);
      miny = std::min(miny, y1);
      maxx = std::max(maxx, x2);
      maxy = std::max(maxy, y2);
      for (auto p : {std::make_pair(x1, y1), {x1, y2}, {x2, y1}, {x2, y2}}) {
        if (!corners.insert(p).second)
          corners.erase(p);
      }
    }

    std::set<std::pair<int, int>> expected = {
        {minx, miny}, {minx, maxy}, {maxx, miny}, {maxx, maxy}};
    if (corners != expected)
      return false;
    return area == (long long)(maxx - minx) * (maxy - miny);
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> a = {
      {1, 1, 3, 3}, {3, 1, 4, 2}, {3, 2, 4, 4}, {1, 3, 2, 4}, {2, 3, 3, 4}};
  std::vector<std::vector<int>> b = {
      {1, 1, 2, 3}, {1, 3, 2, 4}, {3, 1, 4, 2}, {3, 2, 4, 4}};
  std::vector<std::vector<int>> c = {
      {1, 1, 3, 3}, {3, 1, 4, 2}, {1, 3, 2, 4}, {2, 2, 4, 4}};
  std::vector<std::vector<int>> d = {{0, 0, 1, 1}};
  std::cout << std::boolalpha;
  std::cout << s.isRectangleCover(a) << "\n"; // true
  std::cout << s.isRectangleCover(b) << "\n"; // false
  std::cout << s.isRectangleCover(c) << "\n"; // false
  std::cout << s.isRectangleCover(d) << "\n"; // true
  return 0;
}
