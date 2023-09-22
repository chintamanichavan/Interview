def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target < 0:  # if the combination exceeds the target, stop here
            return
        if target == 0:  # if the combination sums up to target, add it to the results
            res.append(path)
            return
        for i in range(start, len(candidates)):
            # To avoid duplicates, skip over duplicate numbers.
            # If the current number is the same as the previous one, skip it
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # Use the number at the current index and explore further
            backtrack(i+1, target-candidates[i], path + [candidates[i]])

    candidates.sort()  # Sort the array first
    res = []
    backtrack(0, target, [])
    return res

# Test the function with the given examples
print(combinationSum2([10,1,2,7,6,1,5], 8))
# Expected output: [[1,1,6], [1,2,5], [1,7], [2,6]]

print(combinationSum2([2,5,2,1,2], 5))
# Expected output: [[1,2,2], [5]]
