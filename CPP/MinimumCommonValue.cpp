#include <iostream>
#include <vector>

class Solution {
public:
    int getCommon(std::vector<int>& nums1, std::vector<int>& nums2) {
        size_t i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) return nums1[i];
            if (nums1[i] < nums2[j]) ++i;
            else ++j;
        }
        return -1;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {1, 2, 3}, b = {2, 4};
    std::vector<int> c = {1, 2, 3, 6}, d = {2, 3, 4, 5};
    std::vector<int> e = {1, 2}, f = {3, 4};
    std::cout << s.getCommon(a, b) << "\n"; // 2
    std::cout << s.getCommon(c, d) << "\n"; // 2
    std::cout << s.getCommon(e, f) << "\n"; // -1
    return 0;
}
