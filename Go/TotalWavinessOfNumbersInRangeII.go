//go:build ignore

package main

import (
	"fmt"
	"strconv"
)

type pair struct{ cnt, tot int64 }

func wavinessUpTo(n int64) int64 {
	if n < 0 {
		return 0
	}
	str := strconv.FormatInt(n, 10)
	L := len(str)
	s := make([]int, L)
	for i := range str {
		s[i] = int(str[i] - '0')
	}

	// Memo for non-tight states keyed by (pos, started, prev2+1, prev1+1).
	visited := make([][2][11][11]bool, L)
	memo := make([][2][11][11]pair, L)

	var dp func(pos int, started bool, prev2, prev1 int, tight bool) (int64, int64)
	dp = func(pos int, started bool, prev2, prev1 int, tight bool) (int64, int64) {
		if pos == L {
			return 1, 0
		}
		si := 0
		if started {
			si = 1
		}
		if !tight && visited[pos][si][prev2+1][prev1+1] {
			p := memo[pos][si][prev2+1][prev1+1]
			return p.cnt, p.tot
		}
		limit := 9
		if tight {
			limit = s[pos]
		}
		var cnt, tot int64
		for d := 0; d <= limit; d++ {
			ntight := tight && d == limit
			var nstarted bool
			var np2, np1, event int
			if !started && d == 0 {
				nstarted, np2, np1, event = false, -1, -1, 0
			} else {
				nstarted = true
				if prev1 != -1 && prev2 != -1 &&
					((prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d)) {
					event = 1
				}
				np2, np1 = prev1, d
			}
			sc, st := dp(pos+1, nstarted, np2, np1, ntight)
			cnt += sc
			tot += st + int64(event)*sc
		}
		if !tight {
			visited[pos][si][prev2+1][prev1+1] = true
			memo[pos][si][prev2+1][prev1+1] = pair{cnt, tot}
		}
		return cnt, tot
	}

	_, tot := dp(0, false, -1, -1, true)
	return tot
}

func totalWaviness(num1, num2 int64) int64 {
	return wavinessUpTo(num2) - wavinessUpTo(num1-1)
}

func main() {
	fmt.Println(totalWaviness(120, 130))             // 3
	fmt.Println(totalWaviness(198, 202))             // 3
	fmt.Println(totalWaviness(4848, 4848))           // 2
	fmt.Println(totalWaviness(1, 1000000))           // 2230005
	fmt.Println(totalWaviness(1, 1000000000000000))  // 7360000000000005
}
