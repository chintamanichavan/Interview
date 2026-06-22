//go:build ignore

package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Level-order encoding: node value, or '#' for a missing child.
func serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	out := []string{}
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node != nil {
			out = append(out, strconv.Itoa(node.Val))
			q = append(q, node.Left, node.Right)
		} else {
			out = append(out, "#")
		}
	}
	return strings.Join(out, ",")
}

func deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	tokens := strings.Split(data, ",")
	v, _ := strconv.Atoi(tokens[0])
	root := &TreeNode{Val: v}
	q := []*TreeNode{root}
	i := 1
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if tokens[i] != "#" {
			cv, _ := strconv.Atoi(tokens[i])
			node.Left = &TreeNode{Val: cv}
			q = append(q, node.Left)
		}
		i++
		if tokens[i] != "#" {
			cv, _ := strconv.Atoi(tokens[i])
			node.Right = &TreeNode{Val: cv}
			q = append(q, node.Right)
		}
		i++
	}
	return root
}

func toList(root *TreeNode) []any {
	out := []any{}
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node != nil {
			out = append(out, node.Val)
			q = append(q, node.Left, node.Right)
		} else {
			out = append(out, nil)
		}
	}
	for len(out) > 0 && out[len(out)-1] == nil {
		out = out[:len(out)-1]
	}
	return out
}

func main() {
	root := &TreeNode{1, &TreeNode{Val: 2}, &TreeNode{3, &TreeNode{Val: 4}, &TreeNode{Val: 5}}}
	data := serialize(root)
	fmt.Println(data)
	fmt.Println(toList(deserialize(data)))                         // [1 2 3 <nil> <nil> 4 5]
	fmt.Printf("%q\n", serialize(deserialize(serialize(nil))))     // ""
	fmt.Println(toList(deserialize(serialize(&TreeNode{Val: 7})))) // [7]
}
