#include <algorithm>
#include <array>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int catMouseGame(std::vector<std::vector<int>>& graph) {
        constexpr int DRAW = 0, MOUSE = 1, CAT = 2;
        int n = (int)graph.size();
        std::vector<std::vector<std::array<int, 3>>> color(
            n, std::vector<std::array<int, 3>>(n, {0, 0, 0}));
        std::vector<std::vector<std::array<int, 3>>> degree(
            n, std::vector<std::array<int, 3>>(n, {0, 0, 0}));
        std::vector<bool> hasZero(n, false);
        for (int i = 0; i < n; ++i) {
            hasZero[i] = std::find(graph[i].begin(), graph[i].end(), 0) != graph[i].end();
        }
        for (int m = 0; m < n; ++m) {
            for (int c = 0; c < n; ++c) {
                degree[m][c][MOUSE] = (int)graph[m].size();
                degree[m][c][CAT] = (int)graph[c].size() - (hasZero[c] ? 1 : 0);
            }
        }

        std::queue<std::tuple<int, int, int, int>> q;
        for (int i = 0; i < n; ++i) {
            for (int t : {MOUSE, CAT}) {
                color[0][i][t] = MOUSE;
                q.emplace(0, i, t, MOUSE);
                if (i > 0) {
                    color[i][i][t] = CAT;
                    q.emplace(i, i, t, CAT);
                }
            }
        }

        while (!q.empty()) {
            auto [m, c, turn, result] = q.front(); q.pop();
            if (turn == MOUSE) {
                for (int pc : graph[c]) {
                    if (pc == 0 || color[m][pc][CAT] != DRAW) continue;
                    if (result == CAT) {
                        color[m][pc][CAT] = CAT;
                        q.emplace(m, pc, CAT, CAT);
                    } else if (--degree[m][pc][CAT] == 0) {
                        color[m][pc][CAT] = result;
                        q.emplace(m, pc, CAT, result);
                    }
                }
            } else {
                for (int pm : graph[m]) {
                    if (color[pm][c][MOUSE] != DRAW) continue;
                    if (result == MOUSE) {
                        color[pm][c][MOUSE] = MOUSE;
                        q.emplace(pm, c, MOUSE, MOUSE);
                    } else if (--degree[pm][c][MOUSE] == 0) {
                        color[pm][c][MOUSE] = result;
                        q.emplace(pm, c, MOUSE, result);
                    }
                }
            }
        }

        return color[1][2][MOUSE];
    }
};

int main() {
    Solution s;
    std::vector<std::vector<int>> g1 = {{2, 5}, {3}, {0, 4, 5}, {1, 4, 5}, {2, 3}, {0, 2, 3}};
    std::vector<std::vector<int>> g2 = {{1, 3}, {0}, {3}, {0, 2}};
    std::cout << s.catMouseGame(g1) << "\n"; // 0
    std::cout << s.catMouseGame(g2) << "\n"; // 1
    return 0;
}
