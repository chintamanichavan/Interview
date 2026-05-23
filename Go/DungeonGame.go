//go:build ignore

package main

import (
	"fmt"
	"math"
)

func calculateMinimumHP(dungeon [][]int) int {
	m, n := len(dungeon), len(dungeon[0])
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = math.MaxInt32
	}
	dp[n-1] = 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			need := min(dp[j], dp[j+1]) - dungeon[i][j]
			dp[j] = max(need, 1)
		}
	}
	return dp[0]
}

func main() {
	fmt.Println(calculateMinimumHP([][]int{{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}})) // 7
	fmt.Println(calculateMinimumHP([][]int{{0}}))                                     // 1
	fmt.Println(calculateMinimumHP([][]int{{100}}))                                   // 1
	fmt.Println(calculateMinimumHP([][]int{{-3}}))                                    // 4
}
