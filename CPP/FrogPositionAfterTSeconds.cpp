#include <iostream>
#include <vector>

class Solution {
public:
    double frogPosition(int n, std::vector<std::vector<int>>& edges, int t, int target) {
        std::vector<std::vector<int>> adj(n + 1);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        std::vector<bool> visited(n + 1, false);
        visited[1] = true;
        return dfs(adj, visited, target, t, 1, 0, 1.0);
    }

private:
    double dfs(std::vector<std::vector<int>>& adj, std::vector<bool>& visited,
               int target, int t, int node, int time, double prob) {
        std::vector<int> children;
        for (int v : adj[node]) if (!visited[v]) children.push_back(v);
        if (node == target) {
            return (time == t || children.empty()) ? prob : 0.0;
        }
        if (time == t || children.empty()) return 0.0;
        double p = prob / (double)children.size();
        for (int c : children) {
            visited[c] = true;
            double res = dfs(adj, visited, target, t, c, time + 1, p);
            if (res > 0.0) return res;
        }
        return 0.0;
    }
};

int main() {
    Solution s;
    std::vector<std::vector<int>> edges = {{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5}};
    std::vector<std::vector<int>> empty;
    std::cout.precision(17);
    std::cout << s.frogPosition(7, edges, 2, 4) << "\n";   // 0.1666...
    std::cout << s.frogPosition(7, edges, 1, 7) << "\n";   // 0.3333...
    std::cout << s.frogPosition(7, edges, 20, 6) << "\n";  // 0.1666...
    std::cout << s.frogPosition(1, empty, 1, 1) << "\n";   // 1
    return 0;
}
