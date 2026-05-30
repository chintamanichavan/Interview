#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

class Solution {
public:
    bool asteroidsDestroyed(int mass, std::vector<int>& asteroids) {
        std::sort(asteroids.begin(), asteroids.end());
        // Sum may exceed int32 (~1e10); use int64.
        int64_t m = mass;
        for (int a : asteroids) {
            if (m < a) return false;
            m += a;
        }
        return true;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {3, 9, 19, 5, 21};
    std::vector<int> b = {4, 9, 23, 4};
    std::vector<int> c = {1};
    std::vector<int> d = {2};
    std::cout << std::boolalpha;
    std::cout << s.asteroidsDestroyed(10, a) << "\n"; // true
    std::cout << s.asteroidsDestroyed(5, b) << "\n";  // false
    std::cout << s.asteroidsDestroyed(1, c) << "\n";  // true
    std::cout << s.asteroidsDestroyed(1, d) << "\n";  // false
    return 0;
}
