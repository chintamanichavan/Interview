def majorityElement(nums):
    if not nums:
        return []

    # Boyer-Moore Voting Algorithm
    candidate1, candidate2, count1, count2 = nums[0], None, 1, 0

    for num in nums[1:]:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1, count2 = count1 - 1, count2 - 1

    # Check the two candidates' occurrences in the array
    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]

# Test the function with the given examples
print(majorityElement([3,2,3]))  # Expected output: [3]
print(majorityElement([1]))      # Expected output: [1]
print(majorityElement([1,2]))   # Expected output: [1,2]
