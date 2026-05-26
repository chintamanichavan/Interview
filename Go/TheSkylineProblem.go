//go:build ignore

package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
)

type Item struct {
	negH int
	endX int
}
type MaxHeap []Item

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i].negH < h[j].negH }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any)         { *h = append(*h, x.(Item)) }
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type Event struct{ x, negH, r int }

func getSkyline(buildings [][]int) [][]int {
	events := make([]Event, 0, 2*len(buildings))
	for _, b := range buildings {
		l, r, h := b[0], b[1], b[2]
		events = append(events, Event{l, -h, r})
		events = append(events, Event{r, 0, 0})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].x != events[j].x {
			return events[i].x < events[j].x
		}
		return events[i].negH < events[j].negH
	})

	h := &MaxHeap{{0, math.MaxInt32}}
	heap.Init(h)
	result := [][]int{}
	for _, e := range events {
		if e.negH != 0 {
			heap.Push(h, Item{e.negH, e.r})
		}
		for (*h)[0].endX <= e.x {
			heap.Pop(h)
		}
		curMax := -(*h)[0].negH
		if len(result) == 0 || result[len(result)-1][1] != curMax {
			result = append(result, []int{e.x, curMax})
		}
	}
	return result
}

func main() {
	fmt.Println(getSkyline([][]int{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}}))
	fmt.Println(getSkyline([][]int{{0, 2, 3}, {2, 5, 3}}))
	fmt.Println(getSkyline([][]int{{1, 2, 1}, {1, 2, 2}, {1, 2, 3}}))
	fmt.Println(getSkyline([][]int{{0, 3, 3}, {1, 5, 3}, {2, 4, 3}, {3, 7, 3}}))
}
