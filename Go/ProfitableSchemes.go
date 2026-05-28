//go:build ignore

package main

import "fmt"

const MOD = 1_000_000_007

func profitableSchemes(n, minProfit int, group, profit []int) int {
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, minProfit+1)
	}
	dp[0][0] = 1
	for idx := range group {
		g, p := group[idx], profit[idx]
		for j := n; j >= g; j-- {
			for k := minProfit; k >= 0; k-- {
				if dp[j-g][k] == 0 {
					continue
				}
				nk := min(k+p, minProfit)
				dp[j][nk] = (dp[j][nk] + dp[j-g][k]) % MOD
			}
		}
	}
	total := 0
	for j := 0; j <= n; j++ {
		total = (total + dp[j][minProfit]) % MOD
	}
	return total
}

func main() {
	fmt.Println(profitableSchemes(5, 3, []int{2, 2}, []int{2, 3}))         // 2
	fmt.Println(profitableSchemes(10, 5, []int{2, 3, 5}, []int{6, 7, 8})) // 7
	fmt.Println(profitableSchemes(1, 1, []int{1, 1}, []int{1, 1}))         // 2
}
