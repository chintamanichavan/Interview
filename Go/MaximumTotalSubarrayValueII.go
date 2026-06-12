//go:build ignore

package main

import (
	"container/heap"
	"fmt"
)

type node struct {
	val  int
	l, r int
}

type MaxHeap []node

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].val > h[j].val }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any)        { *h = append(*h, x.(node)) }
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxTotalValue(nums []int, k int) int64 {
	n := len(nums)
	logt := make([]int, n+1)
	for i := 2; i <= n; i++ {
		logt[i] = logt[i/2] + 1
	}
	upMax := [][]int{append([]int(nil), nums...)}
	upMin := [][]int{append([]int(nil), nums...)}
	for j := 1; (1 << j) <= n; j++ {
		half := 1 << (j - 1)
		length := 1 << j
		pmx, pmn := upMax[j-1], upMin[j-1]
		cmx := make([]int, n-length+1)
		cmn := make([]int, n-length+1)
		for i := range n - length + 1 {
			cmx[i] = max(pmx[i], pmx[i+half])
			cmn[i] = min(pmn[i], pmn[i+half])
		}
		upMax = append(upMax, cmx)
		upMin = append(upMin, cmn)
	}
	value := func(l, r int) int {
		j := logt[r-l+1]
		shift := 1 << j
		mx := max(upMax[j][l], upMax[j][r-shift+1])
		mn := min(upMin[j][l], upMin[j][r-shift+1])
		return mx - mn
	}

	h := &MaxHeap{{value(0, n-1), 0, n - 1}}
	seen := map[int64]bool{int64(n - 1): true} // key = l*n + r, here l=0
	var total int64
	for i := 0; i < k; i++ {
		cur := heap.Pop(h).(node)
		total += int64(cur.val)
		l, r := cur.l, cur.r
		if l+1 <= r {
			key := int64(l+1)*int64(n) + int64(r)
			if !seen[key] {
				seen[key] = true
				heap.Push(h, node{value(l+1, r), l + 1, r})
			}
		}
		if l <= r-1 {
			key := int64(l)*int64(n) + int64(r-1)
			if !seen[key] {
				seen[key] = true
				heap.Push(h, node{value(l, r-1), l, r - 1})
			}
		}
	}
	return total
}

func main() {
	fmt.Println(maxTotalValue([]int{1, 3, 2}, 2))    // 4
	fmt.Println(maxTotalValue([]int{4, 2, 5, 1}, 3)) // 12
	fmt.Println(maxTotalValue([]int{1}, 1))          // 0
}
