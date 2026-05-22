//go:build ignore

package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	nxt := head.Next
	head.Next = swapPairs(nxt.Next)
	nxt.Next = head
	return nxt
}

func build(vals []int) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	for _, v := range vals {
		cur.Next = &ListNode{Val: v}
		cur = cur.Next
	}
	return dummy.Next
}

func toSlice(h *ListNode) []int {
	out := []int{}
	for h != nil {
		out = append(out, h.Val)
		h = h.Next
	}
	return out
}

func main() {
	fmt.Println(toSlice(swapPairs(build([]int{1, 2, 3, 4})))) // [2 1 4 3]
	fmt.Println(toSlice(swapPairs(build([]int{}))))           // []
	fmt.Println(toSlice(swapPairs(build([]int{1}))))          // [1]
	fmt.Println(toSlice(swapPairs(build([]int{1, 2, 3}))))    // [2 1 3]
}
