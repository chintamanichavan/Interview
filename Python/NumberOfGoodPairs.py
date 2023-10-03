def numIdenticalPairs(nums):
    # Create a frequency dictionary
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Count the good pairs
    count = 0
    for f in freq.values():
        count += (f * (f - 1)) // 2

    return count

# Test the function with the given examples
print(numIdenticalPairs([1,2,3,1,1,3]))  # Expected output: 4
print(numIdenticalPairs([1,1,1,1]))      # Expected output: 6
print(numIdenticalPairs([1,2,3]))        # Expected output: 0
