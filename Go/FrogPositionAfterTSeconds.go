//go:build ignore

package main

import "fmt"

func frogPosition(n int, edges [][]int, t int, target int) float64 {
	adj := make([][]int, n+1)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0])
	}
	visited := make([]bool, n+1)
	visited[1] = true

	var dfs func(node, time int, prob float64) float64
	dfs = func(node, time int, prob float64) float64 {
		children := make([]int, 0, len(adj[node]))
		for _, v := range adj[node] {
			if !visited[v] {
				children = append(children, v)
			}
		}
		if node == target {
			if time == t || len(children) == 0 {
				return prob
			}
			return 0
		}
		if time == t || len(children) == 0 {
			return 0
		}
		for _, c := range children {
			visited[c] = true
			res := dfs(c, time+1, prob/float64(len(children)))
			if res > 0 {
				return res
			}
		}
		return 0
	}

	return dfs(1, 0, 1.0)
}

func main() {
	edges := [][]int{{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5}}
	fmt.Println(frogPosition(7, edges, 2, 4))  // 0.1666...
	fmt.Println(frogPosition(7, edges, 1, 7))  // 0.3333...
	fmt.Println(frogPosition(7, edges, 20, 6)) // 0.1666...
	fmt.Println(frogPosition(1, [][]int{}, 1, 1)) // 1.0
}
