//go:build ignore

package main

import (
	"fmt"
	"slices"
)

const (
	DRAW  = 0
	MOUSE = 1
	CAT   = 2
)

func catMouseGame(graph [][]int) int {
	n := len(graph)
	color := make([][][3]int, n)
	degree := make([][][3]int, n)
	for i := range color {
		color[i] = make([][3]int, n)
		degree[i] = make([][3]int, n)
	}
	hasZero := make([]bool, n)
	for i, adj := range graph {
		hasZero[i] = slices.Contains(adj, 0)
	}
	for m := range n {
		for c := range n {
			degree[m][c][MOUSE] = len(graph[m])
			degree[m][c][CAT] = len(graph[c])
			if hasZero[c] {
				degree[m][c][CAT]--
			}
		}
	}

	type State struct{ m, c, turn, result int }
	queue := []State{}
	for i := range n {
		for _, t := range []int{MOUSE, CAT} {
			color[0][i][t] = MOUSE
			queue = append(queue, State{0, i, t, MOUSE})
			if i > 0 {
				color[i][i][t] = CAT
				queue = append(queue, State{i, i, t, CAT})
			}
		}
	}

	for len(queue) > 0 {
		s := queue[0]
		queue = queue[1:]
		if s.turn == MOUSE {
			for _, pc := range graph[s.c] {
				if pc == 0 || color[s.m][pc][CAT] != DRAW {
					continue
				}
				if s.result == CAT {
					color[s.m][pc][CAT] = CAT
					queue = append(queue, State{s.m, pc, CAT, CAT})
				} else {
					degree[s.m][pc][CAT]--
					if degree[s.m][pc][CAT] == 0 {
						color[s.m][pc][CAT] = s.result
						queue = append(queue, State{s.m, pc, CAT, s.result})
					}
				}
			}
		} else {
			for _, pm := range graph[s.m] {
				if color[pm][s.c][MOUSE] != DRAW {
					continue
				}
				if s.result == MOUSE {
					color[pm][s.c][MOUSE] = MOUSE
					queue = append(queue, State{pm, s.c, MOUSE, MOUSE})
				} else {
					degree[pm][s.c][MOUSE]--
					if degree[pm][s.c][MOUSE] == 0 {
						color[pm][s.c][MOUSE] = s.result
						queue = append(queue, State{pm, s.c, MOUSE, s.result})
					}
				}
			}
		}
	}

	return color[1][2][MOUSE]
}

func main() {
	fmt.Println(catMouseGame([][]int{{2, 5}, {3}, {0, 4, 5}, {1, 4, 5}, {2, 3}, {0, 2, 3}})) // 0
	fmt.Println(catMouseGame([][]int{{1, 3}, {0}, {3}, {0, 2}}))                              // 1
}
