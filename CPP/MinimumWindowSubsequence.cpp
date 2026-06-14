#include <iostream>
#include <string>

class Solution {
public:
  std::string minWindow(std::string s1, std::string s2) {
    int m = (int)s1.size(), n = (int)s2.size();
    int i = 0, j = 0, start = -1, best = m + 1;
    while (i < m) {
      if (s1[i] == s2[j]) {
        if (++j == n) {
          int right = i;
          --j;
          while (j >= 0) {
            if (s1[i] == s2[j])
              --j;
            --i;
          }
          ++i; // left end
          if (right - i + 1 < best) {
            best = right - i + 1;
            start = i;
          }
          j = 0;
        }
      }
      ++i;
    }
    return start == -1 ? "" : s1.substr(start, best);
  }
};

int main() {
  Solution s;
  std::cout << s.minWindow("abcdebdde", "bde") << "\n"; // bcde
  std::cout << s.minWindow("abc", "ac") << "\n";        // abc
  std::cout << s.minWindow("abcde", "xyz") << "\n";     // (empty)
  return 0;
}
