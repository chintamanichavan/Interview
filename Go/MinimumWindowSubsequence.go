//go:build ignore

package main

import "fmt"

func minWindow(s1, s2 string) string {
	m, n := len(s1), len(s2)
	i, j := 0, 0
	start, best := -1, m+1
	for i < m {
		if s1[i] == s2[j] {
			j++
			if j == n {
				right := i
				j--
				for j >= 0 {
					if s1[i] == s2[j] {
						j--
					}
					i--
				}
				i++ // left end of window
				if right-i+1 < best {
					best = right - i + 1
					start = i
				}
				j = 0
			}
		}
		i++
	}
	if start == -1 {
		return ""
	}
	return s1[start : start+best]
}

func main() {
	fmt.Println(minWindow("abcdebdde", "bde")) // bcde
	fmt.Println(minWindow("abc", "ac"))        // abc
	fmt.Println(minWindow("abcde", "xyz"))     // (empty)
}
