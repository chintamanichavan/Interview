#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSwapsCouples(std::vector<int>& row) {
        std::unordered_map<int, int> pos;
        for (int i = 0; i < (int)row.size(); ++i) pos[row[i]] = i;
        int swaps = 0;
        for (int i = 0; i < (int)row.size(); i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) continue;
            int j = pos[partner];
            std::swap(row[i + 1], row[j]);
            pos[row[j]] = j;
            pos[row[i + 1]] = i + 1;
            swaps++;
        }
        return swaps;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {0, 2, 1, 3};
    std::vector<int> b = {3, 2, 0, 1};
    std::vector<int> c = {0, 2, 4, 1, 3, 5};
    std::vector<int> d = {5, 4, 2, 6, 3, 1, 0, 7};
    std::cout << s.minSwapsCouples(a) << "\n"; // 1
    std::cout << s.minSwapsCouples(b) << "\n"; // 0
    std::cout << s.minSwapsCouples(c) << "\n"; // 2
    std::cout << s.minSwapsCouples(d) << "\n"; // 2
    return 0;
}
