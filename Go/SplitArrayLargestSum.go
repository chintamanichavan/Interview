//go:build ignore

package main

import "fmt"

func splitArray(nums []int, k int) int {
	needed := func(cap int) int {
		count, cur := 1, 0
		for _, x := range nums {
			if cur+x > cap {
				count++
				cur = x
			} else {
				cur += x
			}
		}
		return count
	}

	lo, hi := 0, 0
	for _, x := range nums {
		lo = max(lo, x)
		hi += x
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if needed(mid) <= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func main() {
	fmt.Println(splitArray([]int{7, 2, 5, 10, 8}, 2)) // 18
	fmt.Println(splitArray([]int{1, 2, 3, 4, 5}, 2))  // 9
	fmt.Println(splitArray([]int{1, 4, 4}, 3))        // 4
}
