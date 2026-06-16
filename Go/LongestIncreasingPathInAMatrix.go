//go:build ignore

package main

import "fmt"

func longestIncreasingPath(matrix [][]int) int {
	m, n := len(matrix), len(matrix[0])
	memo := make([][]int, m)
	for i := range memo {
		memo[i] = make([]int, n)
	}
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(r, c int) int
	dfs = func(r, c int) int {
		if memo[r][c] != 0 {
			return memo[r][c]
		}
		best := 1
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && matrix[nr][nc] > matrix[r][c] {
				best = max(best, 1+dfs(nr, nc))
			}
		}
		memo[r][c] = best
		return best
	}
	ans := 0
	for r := range m {
		for c := range n {
			ans = max(ans, dfs(r, c))
		}
	}
	return ans
}

func main() {
	fmt.Println(longestIncreasingPath([][]int{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}})) // 4
	fmt.Println(longestIncreasingPath([][]int{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}})) // 4
	fmt.Println(longestIncreasingPath([][]int{{1}}))                             // 1
}
