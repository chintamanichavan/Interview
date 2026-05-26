#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> getSkyline(std::vector<std::vector<int>>& buildings) {
        // Events: (x, negH, r). neg sort: starts (negative) before ends (0) at same x;
        // taller starts first.
        std::vector<std::tuple<int, int, int>> events;
        events.reserve(buildings.size() * 2);
        for (auto& b : buildings) {
            events.emplace_back(b[0], -b[2], b[1]);
            events.emplace_back(b[1], 0, 0);
        }
        std::sort(events.begin(), events.end());

        // Max-heap on (height, end_x). Sentinel ground keeps it non-empty.
        std::priority_queue<std::pair<int, int>> heap;
        heap.push({0, INT_MAX});

        std::vector<std::vector<int>> result;
        for (auto& [x, negH, r] : events) {
            if (negH != 0) heap.push({-negH, r});
            while (heap.top().second <= x) heap.pop();
            int curMax = heap.top().first;
            if (result.empty() || result.back()[1] != curMax) {
                result.push_back({x, curMax});
            }
        }
        return result;
    }
};

void print(const std::vector<std::vector<int>>& sk) {
    std::cout << "[";
    bool first = true;
    for (auto& p : sk) {
        if (!first) std::cout << ", ";
        std::cout << "[" << p[0] << "," << p[1] << "]";
        first = false;
    }
    std::cout << "]\n";
}

int main() {
    Solution s;
    std::vector<std::vector<int>> a = {{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}};
    std::vector<std::vector<int>> b = {{0, 2, 3}, {2, 5, 3}};
    std::vector<std::vector<int>> c = {{1, 2, 1}, {1, 2, 2}, {1, 2, 3}};
    std::vector<std::vector<int>> d = {{0, 3, 3}, {1, 5, 3}, {2, 4, 3}, {3, 7, 3}};
    print(s.getSkyline(a));
    print(s.getSkyline(b));
    print(s.getSkyline(c));
    print(s.getSkyline(d));
    return 0;
}
