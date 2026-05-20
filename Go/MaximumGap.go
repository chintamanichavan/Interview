//go:build ignore

package main

import "fmt"

func maximumGap(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}
	mn, mx := nums[0], nums[0]
	for _, x := range nums {
		if x < mn {
			mn = x
		}
		if x > mx {
			mx = x
		}
	}
	if mn == mx {
		return 0
	}

	// Pigeonhole: max gap >= ceil((mx-mn)/(n-1)), so it must occur between buckets of that size.
	bucketSize := max((mx-mn)/(n-1), 1)
	numBuckets := (mx-mn)/bucketSize + 1
	bMin := make([]int, numBuckets)
	bMax := make([]int, numBuckets)
	seen := make([]bool, numBuckets)

	for _, x := range nums {
		i := (x - mn) / bucketSize
		if !seen[i] {
			bMin[i], bMax[i] = x, x
			seen[i] = true
		} else {
			if x < bMin[i] {
				bMin[i] = x
			}
			if x > bMax[i] {
				bMax[i] = x
			}
		}
	}

	best := 0
	prevMax := mn
	for i := range numBuckets {
		if !seen[i] {
			continue
		}
		if gap := bMin[i] - prevMax; gap > best {
			best = gap
		}
		prevMax = bMax[i]
	}
	return best
}

func main() {
	fmt.Println(maximumGap([]int{3, 6, 9, 1}))  // 3
	fmt.Println(maximumGap([]int{10}))          // 0
	fmt.Println(maximumGap([]int{1, 1, 1, 1}))  // 0
	fmt.Println(maximumGap([]int{1, 10000000})) // 9999999
}
