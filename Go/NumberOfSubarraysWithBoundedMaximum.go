//go:build ignore

package main

import "fmt"

func numSubarrayBoundedMax(nums []int, left, right int) int {
	count := func(bound int) int {
		total, length := 0, 0
		for _, x := range nums {
			if x <= bound {
				length++
			} else {
				length = 0
			}
			total += length
		}
		return total
	}
	return count(right) - count(left-1)
}

func main() {
	fmt.Println(numSubarrayBoundedMax([]int{2, 1, 4, 3}, 2, 3))    // 3
	fmt.Println(numSubarrayBoundedMax([]int{2, 9, 2, 5, 6}, 2, 8)) // 7
	fmt.Println(numSubarrayBoundedMax([]int{1, 1, 1}, 1, 1))       // 6
}
