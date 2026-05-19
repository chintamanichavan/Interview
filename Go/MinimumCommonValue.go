//go:build ignore

package main

import "fmt"

func getCommon(nums1, nums2 []int) int {
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		switch {
		case nums1[i] == nums2[j]:
			return nums1[i]
		case nums1[i] < nums2[j]:
			i++
		default:
			j++
		}
	}
	return -1
}

func main() {
	fmt.Println(getCommon([]int{1, 2, 3}, []int{2, 4}))          // 2
	fmt.Println(getCommon([]int{1, 2, 3, 6}, []int{2, 3, 4, 5})) // 2
	fmt.Println(getCommon([]int{1, 2}, []int{3, 4}))             // -1
}
