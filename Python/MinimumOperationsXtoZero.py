def minOperations(nums, x):
    # Calculate the target sum which is the total sum minus x
    target = sum(nums) - x

    # If target is 0, that means the whole array needs to be removed
    if target == 0:
        return len(nums)

    # Initialize two pointers and the current sum
    left, right, curr_sum = 0, 0, 0
    max_length = -1  # To store the maximum length of subarray whose sum is target

    # Iterate through the array with the right pointer
    while right < len(nums):
        # Expand the right pointer
        curr_sum += nums[right]
        right += 1

        # Shrink the left pointer if needed
        while curr_sum > target and left < right:
            curr_sum -= nums[left]
            left += 1

        # Update the max_length if current subarray sum is equal to target
        if curr_sum == target:
            max_length = max(max_length, right - left)

    # If we didn't find any subarray with sum equal to target, return -1
    if max_length == -1:
        return -1

    # Return the minimum operations needed which is the total length minus max_length
    return len(nums) - max_length

# Test the function with the given examples
print(minOperations([1,1,4,2,3], 5))  # Expected output: 2
print(minOperations([5,6,7,8,9], 4))  # Expected output: -1
print(minOperations([3,2,20,1,1,3], 10))  # Expected output: 5
