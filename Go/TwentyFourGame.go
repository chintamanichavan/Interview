//go:build ignore

package main

import (
	"fmt"
	"math"
)

const eps = 1e-6

func judgePoint24(cards []int) bool {
	nums := make([]float64, len(cards))
	for i, c := range cards {
		nums[i] = float64(c)
	}
	return solve(nums)
}

func solve(nums []float64) bool {
	n := len(nums)
	if n == 1 {
		return math.Abs(nums[0]-24) < eps
	}
	for i := range n {
		for j := range n {
			if i == j {
				continue
			}
			rest := []float64{}
			for x := range n {
				if x != i && x != j {
					rest = append(rest, nums[x])
				}
			}
			a, b := nums[i], nums[j]
			cands := []float64{a + b, a - b, a * b}
			if math.Abs(b) > eps {
				cands = append(cands, a/b)
			}
			for _, val := range cands {
				next := make([]float64, len(rest), len(rest)+1)
				copy(next, rest)
				if solve(append(next, val)) {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println(judgePoint24([]int{4, 1, 8, 7})) // true
	fmt.Println(judgePoint24([]int{1, 2, 1, 2})) // false
	fmt.Println(judgePoint24([]int{3, 3, 8, 8})) // true
	fmt.Println(judgePoint24([]int{1, 1, 1, 1})) // false
}
