#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
  std::vector<std::string>
  findAllConcatenatedWordsInADict(std::vector<std::string> &words) {
    std::unordered_set<std::string> set(words.begin(), words.end());
    std::vector<std::string> res;
    for (auto &w : words) {
      if (!w.empty() && canForm(w, set))
        res.push_back(w);
    }
    return res;
  }

private:
  bool canForm(const std::string &word,
               const std::unordered_set<std::string> &set) {
    int n = (int)word.size();
    std::vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (!dp[j] || (j == 0 && i == n))
          continue;
        if (set.count(word.substr(j, i - j))) {
          dp[i] = true;
          break;
        }
      }
    }
    return dp[n];
  }
};

void print(const std::vector<std::string> &v) {
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
  std::vector<std::string> a = {"cat", "cats",        "catsdogcats",
                                "dog", "dogcatsdog",  "hippopotamuses",
                                "rat", "ratcatdogcat"};
  std::vector<std::string> b = {"cat", "dog", "catdog"};
  std::vector<std::string> c = {"a", "b", "ab", "abc"};
  print(s.findAllConcatenatedWordsInADict(
      a)); // [catsdogcats, dogcatsdog, ratcatdogcat]
  print(s.findAllConcatenatedWordsInADict(b)); // [catdog]
  print(s.findAllConcatenatedWordsInADict(c)); // [ab]
  return 0;
}
