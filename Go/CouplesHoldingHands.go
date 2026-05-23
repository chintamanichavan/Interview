//go:build ignore

package main

import "fmt"

func minSwapsCouples(row []int) int {
	pos := make(map[int]int, len(row))
	for i, p := range row {
		pos[p] = i
	}
	swaps := 0
	for i := 0; i < len(row); i += 2 {
		partner := row[i] ^ 1
		if row[i+1] == partner {
			continue
		}
		j := pos[partner]
		row[i+1], row[j] = row[j], row[i+1]
		pos[row[j]] = j
		pos[row[i+1]] = i + 1
		swaps++
	}
	return swaps
}

func main() {
	fmt.Println(minSwapsCouples([]int{0, 2, 1, 3}))            // 1
	fmt.Println(minSwapsCouples([]int{3, 2, 0, 1}))            // 0
	fmt.Println(minSwapsCouples([]int{0, 2, 4, 1, 3, 5}))      // 2
	fmt.Println(minSwapsCouples([]int{5, 4, 2, 6, 3, 1, 0, 7})) // 2
}
