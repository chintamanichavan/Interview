#include <cstring>
#include <iostream>
#include <string>
#include <utility>

class Solution {
public:
    long long totalWaviness(long long num1, long long num2) {
        return wavinessUpTo(num2) - wavinessUpTo(num1 - 1);
    }

private:
    std::string s;
    int L;
    // memo[pos][started][prev2+1][prev1+1]
    bool visited[17][2][11][11];
    std::pair<long long, long long> memo[17][2][11][11];

    long long wavinessUpTo(long long n) {
        if (n < 0) return 0;
        s = std::to_string(n);
        L = (int)s.size();
        std::memset(visited, 0, sizeof(visited));
        return dp(0, false, -1, -1, true).second;
    }

    std::pair<long long, long long> dp(int pos, bool started, int prev2, int prev1, bool tight) {
        if (pos == L) return {1, 0};
        int si = started ? 1 : 0;
        if (!tight && visited[pos][si][prev2 + 1][prev1 + 1]) {
            return memo[pos][si][prev2 + 1][prev1 + 1];
        }
        int limit = tight ? (s[pos] - '0') : 9;
        long long cnt = 0, tot = 0;
        for (int d = 0; d <= limit; ++d) {
            bool ntight = tight && d == limit;
            bool nstarted;
            int np2, np1, event = 0;
            if (!started && d == 0) {
                nstarted = false; np2 = -1; np1 = -1;
            } else {
                nstarted = true;
                if (prev1 != -1 && prev2 != -1 &&
                    ((prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d))) {
                    event = 1;
                }
                np2 = prev1; np1 = d;
            }
            auto [sc, st] = dp(pos + 1, nstarted, np2, np1, ntight);
            cnt += sc;
            tot += st + (long long)event * sc;
        }
        if (!tight) {
            visited[pos][si][prev2 + 1][prev1 + 1] = true;
            memo[pos][si][prev2 + 1][prev1 + 1] = {cnt, tot};
        }
        return {cnt, tot};
    }
};

int main() {
    Solution s;
    std::cout << s.totalWaviness(120, 130) << "\n";                // 3
    std::cout << s.totalWaviness(198, 202) << "\n";                // 3
    std::cout << s.totalWaviness(4848, 4848) << "\n";              // 2
    std::cout << s.totalWaviness(1, 1000000LL) << "\n";            // 2230005
    std::cout << s.totalWaviness(1, 1000000000000000LL) << "\n";   // 7360000000000005
    return 0;
}
