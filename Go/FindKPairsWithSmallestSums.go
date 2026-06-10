//go:build ignore

package main

import (
	"container/heap"
	"fmt"
)

type item struct {
	sum, i, j int
}

type MinHeap []item

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(a, b int) bool { return h[a].sum < h[b].sum }
func (h MinHeap) Swap(a, b int)      { h[a], h[b] = h[b], h[a] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(item)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kSmallestPairs(nums1, nums2 []int, k int) [][]int {
	res := [][]int{}
	if len(nums1) == 0 || len(nums2) == 0 {
		return res
	}
	h := &MinHeap{}
	for i := 0; i < len(nums1) && i < k; i++ {
		*h = append(*h, item{nums1[i] + nums2[0], i, 0})
	}
	heap.Init(h)
	for h.Len() > 0 && len(res) < k {
		it := heap.Pop(h).(item)
		res = append(res, []int{nums1[it.i], nums2[it.j]})
		if it.j+1 < len(nums2) {
			heap.Push(h, item{nums1[it.i] + nums2[it.j+1], it.i, it.j + 1})
		}
	}
	return res
}

func main() {
	fmt.Println(kSmallestPairs([]int{1, 7, 11}, []int{2, 4, 6}, 3)) // [[1 2] [1 4] [1 6]]
	fmt.Println(kSmallestPairs([]int{1, 1, 2}, []int{1, 2, 3}, 2))  // [[1 1] [1 1]]
	fmt.Println(kSmallestPairs([]int{1, 2}, []int{3}, 3))           // [[1 3] [2 3]]
}
