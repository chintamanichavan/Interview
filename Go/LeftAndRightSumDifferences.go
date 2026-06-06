//go:build ignore

package main

import "fmt"

func leftRightDifference(nums []int) []int {
	total := 0
	for _, x := range nums {
		total += x
	}
	ans := make([]int, len(nums))
	left := 0
	for i, x := range nums {
		right := total - left - x
		ans[i] = abs(left - right)
		left += x
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	fmt.Println(leftRightDifference([]int{10, 4, 8, 3})) // [15 1 11 22]
	fmt.Println(leftRightDifference([]int{1}))           // [0]
}
