//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func maxSumSubmatrix(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	best := -1 << 62
	for left := range n {
		rowsum := make([]int, m)
		for right := left; right < n; right++ {
			for i := range m {
				rowsum[i] += matrix[i][right]
			}
			// ordered prefix sums (sorted slice); find smallest prefix >= cur-k
			prefixes := []int{0}
			cur := 0
			for _, v := range rowsum {
				cur += v
				idx := sort.SearchInts(prefixes, cur-k)
				if idx < len(prefixes) {
					if d := cur - prefixes[idx]; d > best {
						best = d
					}
				}
				pos := sort.SearchInts(prefixes, cur)
				prefixes = append(prefixes, 0)
				copy(prefixes[pos+1:], prefixes[pos:])
				prefixes[pos] = cur
			}
		}
	}
	return best
}

func main() {
	fmt.Println(maxSumSubmatrix([][]int{{1, 0, 1}, {0, -2, 3}}, 2)) // 2
	fmt.Println(maxSumSubmatrix([][]int{{2, 2, -1}}, 3))            // 3
	fmt.Println(maxSumSubmatrix([][]int{{2, 2, -1}}, 0))            // -1
}
