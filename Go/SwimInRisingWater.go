//go:build ignore

package main

import (
	"container/heap"
	"fmt"
)

type cell struct{ t, r, c int }

type MinHeap []cell

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(a, b int) bool { return h[a].t < h[b].t }
func (h MinHeap) Swap(a, b int)      { h[a], h[b] = h[b], h[a] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(cell)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func swimInWater(grid [][]int) int {
	n := len(grid)
	h := &MinHeap{{grid[0][0], 0, 0}}
	seen := make([][]bool, n)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(cell)
		if cur.r == n-1 && cur.c == n-1 {
			return cur.t
		}
		if seen[cur.r][cur.c] {
			continue
		}
		seen[cur.r][cur.c] = true
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc] {
				heap.Push(h, cell{max(cur.t, grid[nr][nc]), nr, nc})
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(swimInWater([][]int{{0, 2}, {1, 3}})) // 3
	fmt.Println(swimInWater([][]int{{0, 1, 2, 3, 4}, {24, 23, 22, 21, 5}, {12, 13, 14, 15, 16},
		{11, 17, 18, 19, 20}, {10, 9, 8, 7, 6}})) // 16
	fmt.Println(swimInWater([][]int{{0}})) // 0
}
