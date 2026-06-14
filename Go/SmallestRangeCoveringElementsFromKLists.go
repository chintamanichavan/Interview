//go:build ignore

package main

import (
	"container/heap"
	"fmt"
)

type ptr struct{ val, i, j int }

type MinHeap []ptr

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(a, b int) bool { return h[a].val < h[b].val }
func (h MinHeap) Swap(a, b int)      { h[a], h[b] = h[b], h[a] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(ptr)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func smallestRange(nums [][]int) []int {
	h := &MinHeap{}
	curMax := nums[0][0]
	for i, row := range nums {
		*h = append(*h, ptr{row[0], i, 0})
		curMax = max(curMax, row[0])
	}
	heap.Init(h)
	best := []int{(*h)[0].val, curMax}
	for {
		cur := heap.Pop(h).(ptr)
		if curMax-cur.val < best[1]-best[0] {
			best = []int{cur.val, curMax}
		}
		if cur.j+1 == len(nums[cur.i]) {
			break
		}
		nxt := nums[cur.i][cur.j+1]
		curMax = max(curMax, nxt)
		heap.Push(h, ptr{nxt, cur.i, cur.j + 1})
	}
	return best
}

func main() {
	fmt.Println(smallestRange([][]int{{4, 10, 15, 24, 26}, {0, 9, 12, 20}, {5, 18, 22, 30}})) // [20 24]
	fmt.Println(smallestRange([][]int{{1, 2, 3}, {1, 2, 3}, {1, 2, 3}}))                      // [1 1]
	fmt.Println(smallestRange([][]int{{1}, {2}, {3}}))                                        // [1 3]
}
