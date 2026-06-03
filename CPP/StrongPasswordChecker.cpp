#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>

class Solution {
public:
    int strongPasswordChecker(std::string password) {
        int n = (int)password.size();
        bool hasLower = false, hasUpper = false, hasDigit = false;
        for (char c : password) {
            if (islower((unsigned char)c)) hasLower = true;
            else if (isupper((unsigned char)c)) hasUpper = true;
            else if (isdigit((unsigned char)c)) hasDigit = true;
        }
        int missingType = 3 - hasLower - hasUpper - hasDigit;

        // Runs of >= 3 equal chars: L/3 replacements; bucket by L%3 for the >20 deletion case.
        int change = 0, one = 0, two = 0;
        int i = 2;
        while (i < n) {
            if (password[i] == password[i - 1] && password[i - 1] == password[i - 2]) {
                int length = 2;
                while (i < n && password[i] == password[i - 1]) { ++length; ++i; }
                change += length / 3;
                if (length % 3 == 0) ++one;
                else if (length % 3 == 1) ++two;
            } else {
                ++i;
            }
        }

        if (n < 6) return std::max(6 - n, missingType);
        if (n <= 20) return std::max(change, missingType);

        int del = n - 20;
        change -= std::min(del, one);
        change -= std::min(std::max(del - one, 0), two * 2) / 2;
        change -= std::max(del - one - two * 2, 0) / 3;
        return del + std::max(change, missingType);
    }
};

int main() {
    Solution s;
    std::cout << s.strongPasswordChecker("a") << "\n";                         // 5
    std::cout << s.strongPasswordChecker("aA1") << "\n";                       // 3
    std::cout << s.strongPasswordChecker("1337C0d3") << "\n";                  // 0
    std::cout << s.strongPasswordChecker("aaa123") << "\n";                    // 1
    std::cout << s.strongPasswordChecker("aaaaa") << "\n";                     // 2
    std::cout << s.strongPasswordChecker("1111111111") << "\n";                // 3
    std::cout << s.strongPasswordChecker("aaaabbaaabbaaabbaaabbaaaa") << "\n"; // 7
    return 0;
}
