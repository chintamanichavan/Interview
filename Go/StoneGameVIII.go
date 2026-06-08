//go:build ignore

package main

import "fmt"

func stoneGameVIII(stones []int) int {
	n := len(stones)
	prefix := make([]int64, n)
	var sum int64
	for i, v := range stones {
		sum += int64(v)
		prefix[i] = sum
	}
	dp := prefix[n-1]
	for i := n - 2; i >= 1; i-- {
		if prefix[i]-dp > dp {
			dp = prefix[i] - dp
		}
	}
	return int(dp)
}

func main() {
	fmt.Println(stoneGameVIII([]int{-1, 2, -3, 4, -5}))        // 5
	fmt.Println(stoneGameVIII([]int{7, -6, 5, 10, 5, -2, -6})) // 13
	fmt.Println(stoneGameVIII([]int{-10, -12}))                // -22
}
