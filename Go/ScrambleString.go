//go:build ignore

package main

import "fmt"

func isScramble(s1, s2 string) bool {
	memo := make(map[string]bool)

	var solve func(a, b string) bool
	solve = func(a, b string) bool {
		if a == b {
			return true
		}
		key := a + "|" + b
		if v, ok := memo[key]; ok {
			return v
		}
		// Anagram check via character counts.
		var cnt [26]int
		for i := 0; i < len(a); i++ {
			cnt[a[i]-'a']++
			cnt[b[i]-'a']--
		}
		for _, c := range cnt {
			if c != 0 {
				memo[key] = false
				return false
			}
		}
		n := len(a)
		for i := 1; i < n; i++ {
			if solve(a[:i], b[:i]) && solve(a[i:], b[i:]) {
				memo[key] = true
				return true
			}
			if solve(a[:i], b[n-i:]) && solve(a[i:], b[:n-i]) {
				memo[key] = true
				return true
			}
		}
		memo[key] = false
		return false
	}

	return solve(s1, s2)
}

func main() {
	fmt.Println(isScramble("great", "rgeat")) // true
	fmt.Println(isScramble("abcde", "caebd")) // false
	fmt.Println(isScramble("a", "a"))         // true
	fmt.Println(isScramble("abc", "bca"))     // true
}
