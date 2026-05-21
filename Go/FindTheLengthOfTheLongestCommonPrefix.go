//go:build ignore

package main

import "fmt"

func longestCommonPrefix(arr1, arr2 []int) int {
	prefixes := make(map[int]struct{})
	for _, x := range arr1 {
		for x > 0 {
			prefixes[x] = struct{}{}
			x /= 10
		}
	}

	best := 0
	for _, y := range arr2 {
		for y > 0 {
			if _, ok := prefixes[y]; ok {
				if d := digits(y); d > best {
					best = d
				}
				break
			}
			y /= 10
		}
	}
	return best
}

func digits(n int) int {
	d := 0
	for n > 0 {
		d++
		n /= 10
	}
	return d
}

func main() {
	fmt.Println(longestCommonPrefix([]int{1, 10, 100}, []int{1000})) // 3
	fmt.Println(longestCommonPrefix([]int{1, 2, 3}, []int{4, 4, 4})) // 0
	fmt.Println(longestCommonPrefix([]int{1}, []int{1}))             // 1
}
