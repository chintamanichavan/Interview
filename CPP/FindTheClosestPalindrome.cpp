#include <cstdlib>
#include <iostream>
#include <set>
#include <string>

class Solution {
public:
  std::string nearestPalindromic(std::string n) {
    int length = (int)n.size();
    long long num = std::stoll(n);
    std::set<long long> cands;
    cands.insert(pow10(length - 1) - 1);
    cands.insert(pow10(length) + 1);

    long long prefix = std::stoll(n.substr(0, (length + 1) / 2));
    for (long long p : {prefix - 1, prefix, prefix + 1}) {
      std::string s = std::to_string(p);
      std::string rev(s.rbegin(), s.rend());
      std::string cand = (length % 2 == 0) ? s + rev : s + rev.substr(1);
      cands.insert(std::stoll(cand));
    }
    cands.erase(num);

    long long best = -1;
    for (long long c : cands) {
      if (c < 0)
        continue;
      if (best == -1 || llabs(c - num) < llabs(best - num) ||
          (llabs(c - num) == llabs(best - num) && c < best)) {
        best = c;
      }
    }
    return std::to_string(best);
  }

private:
  long long pow10(int e) {
    long long r = 1;
    for (int i = 0; i < e; ++i)
      r *= 10;
    return r;
  }
};

int main() {
  Solution s;
  for (std::string t : {"123", "1", "10", "1000", "999"}) {
    std::cout << s.nearestPalindromic(t) << "\n"; // 121, 0, 9, 999, 1001
  }
  return 0;
}
