//go:build ignore

package main

import "fmt"

type state struct{ pos, speed int }

func racecar(target int) int {
	bound := 2 * target
	seen := map[state]bool{{0, 1}: true}
	type item struct{ pos, speed, steps int }
	queue := []item{{0, 1, 0}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.pos == target {
			return cur.steps
		}
		// 'A'
		npos, nspeed := cur.pos+cur.speed, cur.speed*2
		if npos >= -bound && npos <= bound && !seen[state{npos, nspeed}] {
			seen[state{npos, nspeed}] = true
			queue = append(queue, item{npos, nspeed, cur.steps + 1})
		}
		// 'R'
		rspeed := 1
		if cur.speed > 0 {
			rspeed = -1
		}
		if !seen[state{cur.pos, rspeed}] {
			seen[state{cur.pos, rspeed}] = true
			queue = append(queue, item{cur.pos, rspeed, cur.steps + 1})
		}
	}
	return -1
}

func main() {
	fmt.Println(racecar(3)) // 2
	fmt.Println(racecar(6)) // 5
	fmt.Println(racecar(1)) // 1
	fmt.Println(racecar(4)) // 5
}
