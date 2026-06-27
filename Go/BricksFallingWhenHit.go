//go:build ignore

package main

import "fmt"

type DSU struct {
	parent, size []int
}

func newDSU(n int) *DSU {
	p := make([]int, n)
	s := make([]int, n)
	for i := range p {
		p[i] = i
		s[i] = 1
	}
	return &DSU{p, s}
}

func (d *DSU) find(x int) int {
	for d.parent[x] != x {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}

func (d *DSU) union(a, b int) {
	ra, rb := d.find(a), d.find(b)
	if ra != rb {
		d.parent[ra] = rb
		d.size[rb] += d.size[ra]
	}
}

func hitBricks(grid [][]int, hits [][]int) []int {
	m, n := len(grid), len(grid[0])
	top := m * n
	d := newDSU(m*n + 1)
	idx := func(r, c int) int { return r*n + c }

	g := make([][]int, m)
	for i := range grid {
		g[i] = append([]int(nil), grid[i]...)
	}
	for _, h := range hits {
		g[h[0]][h[1]] = 0
	}

	for r := range m {
		for c := range n {
			if g[r][c] == 1 {
				if r == 0 {
					d.union(idx(r, c), top)
				}
				if r > 0 && g[r-1][c] == 1 {
					d.union(idx(r, c), idx(r-1, c))
				}
				if c > 0 && g[r][c-1] == 1 {
					d.union(idx(r, c), idx(r, c-1))
				}
			}
		}
	}

	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	res := make([]int, len(hits))
	for i := len(hits) - 1; i >= 0; i-- {
		r, c := hits[i][0], hits[i][1]
		if grid[r][c] == 0 {
			continue
		}
		before := d.size[d.find(top)]
		g[r][c] = 1
		if r == 0 {
			d.union(idx(r, c), top)
		}
		for _, dd := range dirs {
			nr, nc := r+dd[0], c+dd[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && g[nr][nc] == 1 {
				d.union(idx(r, c), idx(nr, nc))
			}
		}
		after := d.size[d.find(top)]
		if after-before-1 > 0 {
			res[i] = after - before - 1
		}
	}
	return res
}

func main() {
	fmt.Println(hitBricks([][]int{{1, 0, 0, 0}, {1, 1, 1, 0}}, [][]int{{1, 0}}))                              // [2]
	fmt.Println(hitBricks([][]int{{1, 0, 0, 0}, {1, 1, 0, 0}}, [][]int{{1, 1}, {1, 0}}))                      // [0 0]
	fmt.Println(hitBricks([][]int{{1, 1, 1}, {0, 1, 0}, {0, 0, 0}}, [][]int{{0, 2}, {2, 0}, {0, 1}, {1, 2}})) // [0 0 1 0]
}
