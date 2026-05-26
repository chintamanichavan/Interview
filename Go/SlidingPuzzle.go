//go:build ignore

package main

import "fmt"

var neighbors = [][]int{
	{1, 3},
	{0, 2, 4},
	{1, 5},
	{0, 4},
	{1, 3, 5},
	{2, 4},
}

func slidingPuzzle(board [][]int) int {
	start := make([]byte, 6)
	zero := 0
	for i, row := range board {
		for j, v := range row {
			idx := i*3 + j
			start[idx] = byte('0' + v)
			if v == 0 {
				zero = idx
			}
		}
	}
	target := "123450"
	startStr := string(start)
	if startStr == target {
		return 0
	}

	type Item struct {
		state string
		zero  int
		steps int
	}
	queue := []Item{{startStr, zero, 0}}
	seen := map[string]bool{startStr: true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, nb := range neighbors[cur.zero] {
			b := []byte(cur.state)
			b[cur.zero], b[nb] = b[nb], b[cur.zero]
			nxt := string(b)
			if nxt == target {
				return cur.steps + 1
			}
			if !seen[nxt] {
				seen[nxt] = true
				queue = append(queue, Item{nxt, nb, cur.steps + 1})
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(slidingPuzzle([][]int{{1, 2, 3}, {4, 0, 5}})) // 1
	fmt.Println(slidingPuzzle([][]int{{1, 2, 3}, {5, 4, 0}})) // -1
	fmt.Println(slidingPuzzle([][]int{{4, 1, 2}, {5, 0, 3}})) // 5
	fmt.Println(slidingPuzzle([][]int{{1, 2, 3}, {4, 5, 0}})) // 0
}
