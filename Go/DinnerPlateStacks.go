//go:build ignore

package main

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)         { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type DinnerPlates struct {
	cap    int
	stacks [][]int
	avail  *MinHeap
}

func Constructor(capacity int) DinnerPlates {
	h := &MinHeap{}
	heap.Init(h)
	return DinnerPlates{cap: capacity, avail: h}
}

func (d *DinnerPlates) Push(val int) {
	for d.avail.Len() > 0 && ((*d.avail)[0] >= len(d.stacks) || len(d.stacks[(*d.avail)[0]]) >= d.cap) {
		heap.Pop(d.avail)
	}
	if d.avail.Len() == 0 {
		heap.Push(d.avail, len(d.stacks))
		d.stacks = append(d.stacks, []int{})
	}
	i := (*d.avail)[0]
	d.stacks[i] = append(d.stacks[i], val)
	if len(d.stacks[i]) >= d.cap {
		heap.Pop(d.avail)
	}
}

func (d *DinnerPlates) Pop() int {
	for len(d.stacks) > 0 && len(d.stacks[len(d.stacks)-1]) == 0 {
		d.stacks = d.stacks[:len(d.stacks)-1]
	}
	if len(d.stacks) == 0 {
		return -1
	}
	return d.PopAtStack(len(d.stacks) - 1)
}

func (d *DinnerPlates) PopAtStack(index int) int {
	if index >= len(d.stacks) || len(d.stacks[index]) == 0 {
		return -1
	}
	heap.Push(d.avail, index)
	s := d.stacks[index]
	v := s[len(s)-1]
	d.stacks[index] = s[:len(s)-1]
	return v
}

func main() {
	ops := []string{"DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
		"push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"}
	args := [][]int{{2}, {1}, {2}, {3}, {4}, {5}, {0}, {20}, {21}, {0}, {2}, {}, {}, {}, {}, {}}
	var d DinnerPlates
	out := []string{}
	for i, op := range ops {
		switch op {
		case "DinnerPlates":
			d = Constructor(args[i][0])
			out = append(out, "null")
		case "push":
			d.Push(args[i][0])
			out = append(out, "null")
		case "pop":
			out = append(out, strconv.Itoa(d.Pop()))
		case "popAtStack":
			out = append(out, strconv.Itoa(d.PopAtStack(args[i][0])))
		}
	}
	fmt.Println("[" + strings.Join(out, ", ") + "]")
}
