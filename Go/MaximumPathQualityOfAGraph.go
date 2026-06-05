//go:build ignore

package main

import "fmt"

type edge struct{ to, cost int }

func maximalPathQuality(values []int, edges [][]int, maxTime int) int {
	n := len(values)
	adj := make([][]edge, n)
	for _, e := range edges {
		u, v, t := e[0], e[1], e[2]
		adj[u] = append(adj[u], edge{v, t})
		adj[v] = append(adj[v], edge{u, t})
	}

	visited := make([]int, n)
	best := 0

	var dfs func(node, timeLeft, quality int)
	dfs = func(node, timeLeft, quality int) {
		if node == 0 && quality > best {
			best = quality
		}
		for _, e := range adj[node] {
			if e.cost <= timeLeft {
				gain := 0
				if visited[e.to] == 0 {
					gain = values[e.to]
				}
				visited[e.to]++
				dfs(e.to, timeLeft-e.cost, quality+gain)
				visited[e.to]--
			}
		}
	}

	visited[0] = 1
	dfs(0, maxTime, values[0])
	return best
}

func main() {
	fmt.Println(maximalPathQuality([]int{0, 32, 10, 43}, [][]int{{0, 1, 10}, {1, 2, 15}, {0, 3, 10}}, 49)) // 75
	fmt.Println(maximalPathQuality([]int{5, 10, 15, 20}, [][]int{{0, 1, 10}, {1, 2, 10}, {0, 3, 10}}, 30)) // 25
	fmt.Println(maximalPathQuality([]int{1, 2, 3, 4}, [][]int{{0, 1, 10}, {1, 2, 11}, {2, 3, 12}, {1, 3, 13}}, 50)) // 7
	fmt.Println(maximalPathQuality([]int{5}, [][]int{}, 100)) // 5
}
