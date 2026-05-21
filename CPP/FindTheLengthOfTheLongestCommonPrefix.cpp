#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestCommonPrefix(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_set<int> prefixes;
        for (int x : arr1) {
            while (x > 0) {
                prefixes.insert(x);
                x /= 10;
            }
        }

        int best = 0;
        for (int y : arr2) {
            while (y > 0) {
                if (prefixes.count(y)) {
                    best = std::max(best, digits(y));
                    break;
                }
                y /= 10;
            }
        }
        return best;
    }

private:
    static int digits(int n) {
        int d = 0;
        while (n > 0) { d++; n /= 10; }
        return d;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {1, 10, 100}, b = {1000};
    std::vector<int> c = {1, 2, 3}, d = {4, 4, 4};
    std::vector<int> e = {1}, f = {1};
    std::cout << s.longestCommonPrefix(a, b) << "\n"; // 3
    std::cout << s.longestCommonPrefix(c, d) << "\n"; // 0
    std::cout << s.longestCommonPrefix(e, f) << "\n"; // 1
    return 0;
}
