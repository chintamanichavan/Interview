#include <iostream>
#include <vector>

class Solution {
public:
    int maximalPathQuality(std::vector<int>& values, std::vector<std::vector<int>>& edges, int maxTime) {
        int n = (int)values.size();
        adj.assign(n, {});
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        vals = &values;
        visited.assign(n, 0);
        best = 0;
        visited[0] = 1;
        dfs(0, maxTime, values[0]);
        return (int)best;
    }

private:
    std::vector<std::vector<std::pair<int, int>>> adj;  // node -> (to, cost)
    std::vector<int>* vals = nullptr;
    std::vector<int> visited;
    long long best = 0;

    void dfs(int node, int timeLeft, long long quality) {
        if (node == 0 && quality > best) best = quality;
        for (auto& [to, cost] : adj[node]) {
            if (cost <= timeLeft) {
                long long gain = visited[to] == 0 ? (*vals)[to] : 0;
                visited[to]++;
                dfs(to, timeLeft - cost, quality + gain);
                visited[to]--;
            }
        }
    }
};

int main() {
    Solution s;
    std::vector<int> v1 = {0, 32, 10, 43};
    std::vector<std::vector<int>> e1 = {{0, 1, 10}, {1, 2, 15}, {0, 3, 10}};
    std::vector<int> v2 = {5, 10, 15, 20};
    std::vector<std::vector<int>> e2 = {{0, 1, 10}, {1, 2, 10}, {0, 3, 10}};
    std::vector<int> v3 = {1, 2, 3, 4};
    std::vector<std::vector<int>> e3 = {{0, 1, 10}, {1, 2, 11}, {2, 3, 12}, {1, 3, 13}};
    std::vector<int> v4 = {5};
    std::vector<std::vector<int>> e4 = {};
    std::cout << s.maximalPathQuality(v1, e1, 49) << "\n";  // 75
    std::cout << s.maximalPathQuality(v2, e2, 30) << "\n";  // 25
    std::cout << s.maximalPathQuality(v3, e3, 50) << "\n";  // 7
    std::cout << s.maximalPathQuality(v4, e4, 100) << "\n"; // 5
    return 0;
}
