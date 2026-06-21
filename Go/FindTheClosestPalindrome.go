//go:build ignore

package main

import (
	"fmt"
	"strconv"
)

func reverse(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

func abs64(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func nearestPalindromic(n string) string {
	length := len(n)
	num, _ := strconv.ParseInt(n, 10, 64)
	cands := map[int64]bool{}
	cands[pow10(length-1)-1] = true
	cands[pow10(length)+1] = true

	prefix, _ := strconv.ParseInt(n[:(length+1)/2], 10, 64)
	for _, p := range []int64{prefix - 1, prefix, prefix + 1} {
		s := strconv.FormatInt(p, 10)
		var cand string
		if length%2 == 0 {
			cand = s + reverse(s)
		} else {
			cand = s + reverse(s[:len(s)-1])
		}
		v, _ := strconv.ParseInt(cand, 10, 64)
		cands[v] = true
	}
	delete(cands, num)

	var best int64 = -1
	for c := range cands {
		if c < 0 {
			continue
		}
		if best == -1 || abs64(c-num) < abs64(best-num) ||
			(abs64(c-num) == abs64(best-num) && c < best) {
			best = c
		}
	}
	return strconv.FormatInt(best, 10)
}

func pow10(e int) int64 {
	r := int64(1)
	for range e {
		r *= 10
	}
	return r
}

func main() {
	for _, t := range []string{"123", "1", "10", "1000", "999"} {
		fmt.Println(nearestPalindromic(t)) // 121, 0, 9, 999, 1001
	}
}
