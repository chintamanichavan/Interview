//go:build ignore

package main

import "fmt"

func strongPasswordChecker(password string) int {
	n := len(password)
	hasLower, hasUpper, hasDigit := false, false, false
	for i := range n {
		c := password[i]
		switch {
		case c >= 'a' && c <= 'z':
			hasLower = true
		case c >= 'A' && c <= 'Z':
			hasUpper = true
		case c >= '0' && c <= '9':
			hasDigit = true
		}
	}
	missingType := 3
	if hasLower {
		missingType--
	}
	if hasUpper {
		missingType--
	}
	if hasDigit {
		missingType--
	}

	// Runs of >= 3 equal chars: L//3 replacements each. Bucket by L%3 for the >20 deletion case.
	change, one, two := 0, 0, 0
	i := 2
	for i < n {
		if password[i] == password[i-1] && password[i-1] == password[i-2] {
			length := 2
			for i < n && password[i] == password[i-1] {
				length++
				i++
			}
			change += length / 3
			switch length % 3 {
			case 0:
				one++
			case 1:
				two++
			}
		} else {
			i++
		}
	}

	if n < 6 {
		return max(6-n, missingType)
	}
	if n <= 20 {
		return max(change, missingType)
	}

	del := n - 20
	change -= min(del, one)
	change -= min(max(del-one, 0), two*2) / 2
	change -= max(del-one-two*2, 0) / 3
	return del + max(change, missingType)
}

func main() {
	fmt.Println(strongPasswordChecker("a"))                          // 5
	fmt.Println(strongPasswordChecker("aA1"))                        // 3
	fmt.Println(strongPasswordChecker("1337C0d3"))                   // 0
	fmt.Println(strongPasswordChecker("aaa123"))                     // 1
	fmt.Println(strongPasswordChecker("aaaaa"))                      // 2
	fmt.Println(strongPasswordChecker("1111111111"))                 // 3
	fmt.Println(strongPasswordChecker("aaaabbaaabbaaabbaaabbaaaa"))  // 7
}
