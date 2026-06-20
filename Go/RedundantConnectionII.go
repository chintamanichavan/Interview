//go:build ignore

package main

import "fmt"

func findRedundantDirectedConnection(edges [][]int) []int {
	n := len(edges)
	parent := make([]int, n+1)
	var cand1, cand2 []int
	for i := range edges {
		u, v := edges[i][0], edges[i][1]
		if parent[v] != 0 {
			cand1 = []int{parent[v], v}
			cand2 = []int{u, v}
			edges[i][1] = 0 // disable cand2 in the union pass
		} else {
			parent[v] = u
		}
	}

	uf := make([]int, n+1)
	for i := range uf {
		uf[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for uf[x] != x {
			uf[x] = uf[uf[x]]
			x = uf[x]
		}
		return x
	}

	for _, e := range edges {
		u, v := e[0], e[1]
		if v == 0 {
			continue
		}
		ru, rv := find(u), find(v)
		if ru == rv {
			if cand1 != nil {
				return cand1
			}
			return []int{u, v}
		}
		uf[rv] = ru
	}
	return cand2
}

func main() {
	fmt.Println(findRedundantDirectedConnection([][]int{{1, 2}, {1, 3}, {2, 3}}))                 // [2 3]
	fmt.Println(findRedundantDirectedConnection([][]int{{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5}})) // [4 1]
	fmt.Println(findRedundantDirectedConnection([][]int{{2, 1}, {3, 1}, {4, 2}, {1, 4}}))         // [2 1]
}
