//go:build ignore

package main

import "fmt"

const MOD = 1_000_000_007

func one(c byte) int {
	if c == '*' {
		return 9
	}
	if c == '0' {
		return 0
	}
	return 1
}

func two(c1, c2 byte) int {
	switch c1 {
	case '1':
		if c2 == '*' {
			return 9
		}
		return 1
	case '2':
		if c2 == '*' {
			return 6
		}
		if c2 >= '0' && c2 <= '6' {
			return 1
		}
		return 0
	case '*':
		if c2 == '*' {
			return 15
		}
		if c2 >= '0' && c2 <= '6' {
			return 2
		}
		return 1
	}
	return 0
}

func numDecodings(s string) int {
	prev2, prev1 := 1, one(s[0])
	for i := 1; i < len(s); i++ {
		cur := (one(s[i])*prev1 + two(s[i-1], s[i])*prev2) % MOD
		prev2, prev1 = prev1, cur
	}
	return prev1 % MOD
}

func main() {
	fmt.Println(numDecodings("*"))  // 9
	fmt.Println(numDecodings("1*")) // 18
	fmt.Println(numDecodings("2*")) // 15
	fmt.Println(numDecodings("0"))  // 0
	fmt.Println(numDecodings("**")) // 96
	fmt.Println(numDecodings("*1")) // 11
}
