#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    bool isSolvable(std::vector<std::string>& words, std::string result) {
        size_t maxLen = 0;
        for (auto& w : words) maxLen = std::max(maxLen, w.size());
        if (maxLen > result.size()) return false;

        revWords.clear();
        for (auto& w : words) {
            std::string r(w.rbegin(), w.rend());
            revWords.push_back(std::move(r));
        }
        revResult.assign(result.rbegin(), result.rend());

        leading.fill(false);
        for (auto& w : words) if (w.size() > 1) leading[w[0] - 'A'] = true;
        if (result.size() > 1) leading[result[0] - 'A'] = true;

        charDigit.fill(-1);
        used.fill(false);
        return dfs(0, 0, 0);
    }

private:
    std::vector<std::string> revWords;
    std::string revResult;
    std::array<bool, 26> leading{};
    std::array<int, 26> charDigit{};
    std::array<bool, 10> used{};

    bool dfs(int col, int idx, int carry) {
        if (col == (int)revResult.size()) return carry == 0;
        if (idx < (int)revWords.size()) {
            const std::string& w = revWords[idx];
            if (col >= (int)w.size() || charDigit[w[col] - 'A'] != -1) {
                return dfs(col, idx + 1, carry);
            }
            int ch = w[col] - 'A';
            for (int d = 0; d < 10; ++d) {
                if (used[d] || (d == 0 && leading[ch])) continue;
                charDigit[ch] = d;
                used[d] = true;
                if (dfs(col, idx + 1, carry)) return true;
                charDigit[ch] = -1;
                used[d] = false;
            }
            return false;
        }

        int colSum = carry;
        for (const auto& w : revWords) {
            if (col < (int)w.size()) colSum += charDigit[w[col] - 'A'];
        }
        int digit = colSum % 10, nextCarry = colSum / 10;
        int rCh = revResult[col] - 'A';
        if (charDigit[rCh] != -1) {
            if (charDigit[rCh] != digit) return false;
            return dfs(col + 1, 0, nextCarry);
        }
        if (used[digit] || (digit == 0 && leading[rCh])) return false;
        charDigit[rCh] = digit;
        used[digit] = true;
        if (dfs(col + 1, 0, nextCarry)) return true;
        charDigit[rCh] = -1;
        used[digit] = false;
        return false;
    }
};

int main() {
    Solution s;
    std::vector<std::string> a = {"SEND", "MORE"};
    std::vector<std::string> b = {"SIX", "SEVEN", "SEVEN"};
    std::vector<std::string> c = {"LEET", "CODE"};
    std::vector<std::string> d = {"A", "B"};
    std::vector<std::string> e = {"ACA"};
    std::cout << std::boolalpha;
    std::cout << s.isSolvable(a, "MONEY") << "\n";  // true
    std::cout << s.isSolvable(b, "TWENTY") << "\n"; // true
    std::cout << s.isSolvable(c, "POINT") << "\n";  // false
    std::cout << s.isSolvable(d, "C") << "\n";      // true
    std::cout << s.isSolvable(e, "JA") << "\n";     // false
    return 0;
}
