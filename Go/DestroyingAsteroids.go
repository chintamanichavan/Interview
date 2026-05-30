//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func asteroidsDestroyed(mass int, asteroids []int) bool {
	sort.Ints(asteroids)
	// mass + sum may exceed int32 (up to ~1e10), but int is 64-bit on linux/amd64.
	m := int64(mass)
	for _, a := range asteroids {
		if m < int64(a) {
			return false
		}
		m += int64(a)
	}
	return true
}

func main() {
	fmt.Println(asteroidsDestroyed(10, []int{3, 9, 19, 5, 21})) // true
	fmt.Println(asteroidsDestroyed(5, []int{4, 9, 23, 4}))      // false
	fmt.Println(asteroidsDestroyed(1, []int{1}))                // true
	fmt.Println(asteroidsDestroyed(1, []int{2}))                // false
}
