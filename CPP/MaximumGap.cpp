#include <algorithm>
#include <iostream>
#include <optional>
#include <vector>

class Solution {
public:
    int maximumGap(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        auto [mnIt, mxIt] = std::minmax_element(nums.begin(), nums.end());
        int mn = *mnIt, mx = *mxIt;
        if (mn == mx) return 0;

        // Pigeonhole: max gap >= ceil((mx-mn)/(n-1)), so it lies between buckets of that size.
        int bucketSize = std::max(1, (mx - mn) / (n - 1));
        int numBuckets = (mx - mn) / bucketSize + 1;
        std::vector<std::optional<std::pair<int, int>>> buckets(numBuckets);

        for (int x : nums) {
            int i = (x - mn) / bucketSize;
            if (!buckets[i]) buckets[i] = {x, x};
            else {
                buckets[i]->first = std::min(buckets[i]->first, x);
                buckets[i]->second = std::max(buckets[i]->second, x);
            }
        }

        int best = 0, prevMax = mn;
        for (auto& b : buckets) {
            if (!b) continue;
            best = std::max(best, b->first - prevMax);
            prevMax = b->second;
        }
        return best;
    }
};

int main() {
    Solution s;
    std::vector<int> a = {3, 6, 9, 1};
    std::vector<int> b = {10};
    std::vector<int> c = {1, 1, 1, 1};
    std::vector<int> d = {1, 10000000};
    std::cout << s.maximumGap(a) << "\n"; // 3
    std::cout << s.maximumGap(b) << "\n"; // 0
    std::cout << s.maximumGap(c) << "\n"; // 0
    std::cout << s.maximumGap(d) << "\n"; // 9999999
    return 0;
}
