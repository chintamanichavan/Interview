#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  int evaluate(std::string expression) { return ev(expression); }

private:
  std::unordered_map<std::string, std::vector<int>> scope;

  std::vector<std::string> topTokens(const std::string &s) {
    std::vector<std::string> res;
    int depth = 0;
    std::string cur;
    for (char ch : s) {
      if (ch == '(')
        ++depth;
      else if (ch == ')')
        --depth;
      if (ch == ' ' && depth == 0) {
        if (!cur.empty()) {
          res.push_back(cur);
          cur.clear();
        }
      } else {
        cur += ch;
      }
    }
    if (!cur.empty())
      res.push_back(cur);
    return res;
  }

  bool isIntLiteral(const std::string &s) {
    if (s.empty())
      return false;
    size_t i = (s[0] == '-') ? 1 : 0;
    if (i == s.size())
      return false;
    for (; i < s.size(); ++i)
      if (!isdigit((unsigned char)s[i]))
        return false;
    return true;
  }

  int ev(const std::string &expr) {
    if (expr[0] != '(') {
      if (isIntLiteral(expr))
        return std::stoi(expr);
      return scope[expr].back();
    }
    auto parts = topTokens(expr.substr(1, expr.size() - 2));
    if (parts[0] == "add")
      return ev(parts[1]) + ev(parts[2]);
    if (parts[0] == "mult")
      return ev(parts[1]) * ev(parts[2]);
    // let
    std::vector<std::string> assigned;
    size_t i = 1;
    while (i + 1 < parts.size()) {
      int val = ev(parts[i + 1]);
      scope[parts[i]].push_back(val);
      assigned.push_back(parts[i]);
      i += 2;
    }
    int result = ev(parts[i]);
    for (auto &v : assigned)
      scope[v].pop_back();
    return result;
  }
};

int main() {
  Solution s;
  std::cout << s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")
            << "\n";                                                      // 14
  std::cout << s.evaluate("(let x 3 x 2 x)") << "\n";                     // 2
  std::cout << s.evaluate("(let x 1 y 2 x (add x y) (add x y))") << "\n"; // 5
  std::cout << s.evaluate("(add 1 2)") << "\n";                           // 3
  std::cout << s.evaluate("(let x 7 -12)") << "\n";                       // -12
  return 0;
}
