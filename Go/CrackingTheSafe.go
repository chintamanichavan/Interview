//go:build ignore

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func crackSafe(n, k int) string {
	if n == 1 {
		var b strings.Builder
		for d := range k {
			b.WriteString(strconv.Itoa(d))
		}
		return b.String()
	}

	seen := map[string]bool{}
	var path []string

	var dfs func(node string)
	dfs = func(node string) {
		for d := range k {
			edge := node + strconv.Itoa(d)
			if !seen[edge] {
				seen[edge] = true
				dfs(edge[1:])
				path = append(path, strconv.Itoa(d))
			}
		}
	}

	start := strings.Repeat("0", n-1)
	dfs(start)
	return strings.Join(path, "") + start
}

func main() {
	fmt.Println(crackSafe(1, 2)) // 01
	fmt.Println(crackSafe(2, 2)) // 01100
	fmt.Println(crackSafe(3, 2)) // 0011101000
	fmt.Println(crackSafe(2, 3)) // 0221120100
}
