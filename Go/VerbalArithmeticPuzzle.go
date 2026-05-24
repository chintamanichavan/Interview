//go:build ignore

package main

import "fmt"

func isSolvable(words []string, result string) bool {
	maxLen := 0
	for _, w := range words {
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	if maxLen > len(result) {
		return false
	}

	revWords := make([]string, len(words))
	for i, w := range words {
		b := []byte(w)
		for l, r := 0, len(b)-1; l < r; l, r = l+1, r-1 {
			b[l], b[r] = b[r], b[l]
		}
		revWords[i] = string(b)
	}
	revResult := []byte(result)
	for l, r := 0, len(revResult)-1; l < r; l, r = l+1, r-1 {
		revResult[l], revResult[r] = revResult[r], revResult[l]
	}

	leading := [26]bool{}
	for _, w := range words {
		if len(w) > 1 {
			leading[w[0]-'A'] = true
		}
	}
	if len(result) > 1 {
		leading[result[0]-'A'] = true
	}

	const unset = -1
	var charDigit [26]int
	for i := range charDigit {
		charDigit[i] = unset
	}
	var used [10]bool

	var dfs func(col, idx, carry int) bool
	dfs = func(col, idx, carry int) bool {
		if col == len(revResult) {
			return carry == 0
		}
		if idx < len(revWords) {
			w := revWords[idx]
			if col >= len(w) || charDigit[w[col]-'A'] != unset {
				return dfs(col, idx+1, carry)
			}
			ch := w[col] - 'A'
			for d := range 10 {
				if used[d] || (d == 0 && leading[ch]) {
					continue
				}
				charDigit[ch] = d
				used[d] = true
				if dfs(col, idx+1, carry) {
					return true
				}
				charDigit[ch] = unset
				used[d] = false
			}
			return false
		}

		colSum := carry
		for _, w := range revWords {
			if col < len(w) {
				colSum += charDigit[w[col]-'A']
			}
		}
		digit := colSum % 10
		nextCarry := colSum / 10
		rCh := revResult[col] - 'A'
		if charDigit[rCh] != unset {
			if charDigit[rCh] != digit {
				return false
			}
			return dfs(col+1, 0, nextCarry)
		}
		if used[digit] || (digit == 0 && leading[rCh]) {
			return false
		}
		charDigit[rCh] = digit
		used[digit] = true
		if dfs(col+1, 0, nextCarry) {
			return true
		}
		charDigit[rCh] = unset
		used[digit] = false
		return false
	}

	return dfs(0, 0, 0)
}

func main() {
	fmt.Println(isSolvable([]string{"SEND", "MORE"}, "MONEY"))           // true
	fmt.Println(isSolvable([]string{"SIX", "SEVEN", "SEVEN"}, "TWENTY")) // true
	fmt.Println(isSolvable([]string{"LEET", "CODE"}, "POINT"))           // false
	fmt.Println(isSolvable([]string{"A", "B"}, "C"))                     // true
	fmt.Println(isSolvable([]string{"ACA"}, "JA"))                       // false
}
