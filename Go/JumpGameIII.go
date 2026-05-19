//go:build ignore

package main

import "fmt"

func canReach(arr []int, start int) bool {
	n := len(arr)
	seen := make([]bool, n)
	queue := []int{start}
	seen[start] = true
	for len(queue) > 0 {
		i := queue[0]
		queue = queue[1:]
		if arr[i] == 0 {
			return true
		}
		for _, j := range []int{i + arr[i], i - arr[i]} {
			if j >= 0 && j < n && !seen[j] {
				seen[j] = true
				queue = append(queue, j)
			}
		}
	}
	return false
}

func main() {
	fmt.Println(canReach([]int{4, 2, 3, 0, 3, 1, 2}, 5)) // true
	fmt.Println(canReach([]int{4, 2, 3, 0, 3, 1, 2}, 0)) // true
	fmt.Println(canReach([]int{3, 0, 2, 1, 2}, 2))       // false
}
