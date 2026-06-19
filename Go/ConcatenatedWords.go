//go:build ignore

package main

import "fmt"

func findAllConcatenatedWordsInADict(words []string) []string {
	set := make(map[string]struct{}, len(words))
	for _, w := range words {
		set[w] = struct{}{}
	}

	canForm := func(word string) bool {
		n := len(word)
		dp := make([]bool, n+1)
		dp[0] = true
		for i := 1; i <= n; i++ {
			for j := 0; j < i; j++ {
				if !dp[j] || (j == 0 && i == n) {
					continue
				}
				if _, ok := set[word[j:i]]; ok {
					dp[i] = true
					break
				}
			}
		}
		return dp[n]
	}

	res := []string{}
	for _, w := range words {
		if w != "" && canForm(w) {
			res = append(res, w)
		}
	}
	return res
}

func main() {
	fmt.Println(findAllConcatenatedWordsInADict([]string{"cat", "cats", "catsdogcats", "dog",
		"dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"}))
	// [catsdogcats dogcatsdog ratcatdogcat]
	fmt.Println(findAllConcatenatedWordsInADict([]string{"cat", "dog", "catdog"})) // [catdog]
	fmt.Println(findAllConcatenatedWordsInADict([]string{"a", "b", "ab", "abc"}))  // [ab]
}
