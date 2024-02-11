def find132pattern(nums):
    third = float('-inf')
    stack = []

    # Traverse the array from right to left
    for num in reversed(nums):
        # Check if current number is a potential nums[i] for 132 pattern
        if num < third:
            return True
        # Update third to the largest number which is smaller than nums[j]
        while stack and stack[-1] < num:
            third = stack.pop()
        stack.append(num)

    return False

# Test the function with the given examples
print(find132pattern([1,2,3,4]))       # Expected output: false
print(find132pattern([3,1,4,2]))       # Expected output: true
print(find132pattern([-1,3,2,0]))      # Expected output: true
