#include <iostream>
#include <string>

class Solution {
public:
    int numDecodings(std::string s) {
        constexpr long long MOD = 1'000'000'007LL;
        long long prev2 = 1, prev1 = one(s[0]);
        for (size_t i = 1; i < s.size(); ++i) {
            long long cur = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % MOD;
            prev2 = prev1;
            prev1 = cur;
        }
        return (int)(prev1 % MOD);
    }

private:
    static int one(char c) {
        if (c == '*') return 9;
        if (c == '0') return 0;
        return 1;
    }

    static int two(char c1, char c2) {
        if (c1 == '1') return (c2 == '*') ? 9 : 1;
        if (c1 == '2') {
            if (c2 == '*') return 6;
            return (c2 >= '0' && c2 <= '6') ? 1 : 0;
        }
        if (c1 == '*') {
            if (c2 == '*') return 15;
            if (c2 >= '0' && c2 <= '6') return 2;
            return 1;
        }
        return 0;
    }
};

int main() {
    Solution s;
    std::cout << s.numDecodings("*") << "\n";  // 9
    std::cout << s.numDecodings("1*") << "\n"; // 18
    std::cout << s.numDecodings("2*") << "\n"; // 15
    std::cout << s.numDecodings("0") << "\n";  // 0
    std::cout << s.numDecodings("**") << "\n"; // 96
    std::cout << s.numDecodings("*1") << "\n"; // 11
    return 0;
}
