#include <array>
#include <iostream>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isScramble(std::string s1, std::string s2) {
        return solve(s1, s2);
    }

private:
    std::unordered_map<std::string, bool> memo;

    bool solve(const std::string& a, const std::string& b) {
        if (a == b) return true;
        std::string key = a + "|" + b;
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;

        std::array<int, 26> cnt{};
        for (size_t i = 0; i < a.size(); ++i) {
            cnt[a[i] - 'a']++;
            cnt[b[i] - 'a']--;
        }
        for (int c : cnt) {
            if (c != 0) return memo[key] = false;
        }
        int n = (int)a.size();
        for (int i = 1; i < n; ++i) {
            if (solve(a.substr(0, i), b.substr(0, i)) && solve(a.substr(i), b.substr(i))) {
                return memo[key] = true;
            }
            if (solve(a.substr(0, i), b.substr(n - i)) && solve(a.substr(i), b.substr(0, n - i))) {
                return memo[key] = true;
            }
        }
        return memo[key] = false;
    }
};

int main() {
    Solution s;
    std::cout << std::boolalpha;
    std::cout << s.isScramble("great", "rgeat") << "\n"; // true
    std::cout << s.isScramble("abcde", "caebd") << "\n"; // false
    std::cout << s.isScramble("a", "a") << "\n";         // true
    std::cout << s.isScramble("abc", "bca") << "\n";     // true
    return 0;
}
