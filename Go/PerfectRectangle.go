//go:build ignore

package main

import "fmt"

type point struct{ x, y int }

func isRectangleCover(rectangles [][]int) bool {
	area := 0
	minx, miny := 1<<62, 1<<62
	maxx, maxy := -(1 << 62), -(1 << 62)
	corners := map[point]bool{}

	for _, r := range rectangles {
		x1, y1, x2, y2 := r[0], r[1], r[2], r[3]
		area += (x2 - x1) * (y2 - y1)
		minx, miny = min(minx, x1), min(miny, y1)
		maxx, maxy = max(maxx, x2), max(maxy, y2)
		for _, p := range []point{{x1, y1}, {x1, y2}, {x2, y1}, {x2, y2}} {
			if corners[p] {
				delete(corners, p)
			} else {
				corners[p] = true
			}
		}
	}

	expected := []point{{minx, miny}, {minx, maxy}, {maxx, miny}, {maxx, maxy}}
	if len(corners) != 4 {
		return false
	}
	for _, p := range expected {
		if !corners[p] {
			return false
		}
	}
	return area == (maxx-minx)*(maxy-miny)
}

func main() {
	fmt.Println(isRectangleCover([][]int{{1, 1, 3, 3}, {3, 1, 4, 2}, {3, 2, 4, 4}, {1, 3, 2, 4}, {2, 3, 3, 4}})) // true
	fmt.Println(isRectangleCover([][]int{{1, 1, 2, 3}, {1, 3, 2, 4}, {3, 1, 4, 2}, {3, 2, 4, 4}}))               // false
	fmt.Println(isRectangleCover([][]int{{1, 1, 3, 3}, {3, 1, 4, 2}, {1, 3, 2, 4}, {2, 2, 4, 4}}))               // false
	fmt.Println(isRectangleCover([][]int{{0, 0, 1, 1}}))                                                         // true
}
