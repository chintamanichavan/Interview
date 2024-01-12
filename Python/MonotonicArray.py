def isMonotonic(nums):
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            decreasing = False
        if nums[i] < nums[i-1]:
            increasing = False
            
    return increasing or decreasing

# Test the function with the given examples
print(isMonotonic([1,2,2,3]))  # Expected output: true
print(isMonotonic([6,5,4,4]))  # Expected output: true
print(isMonotonic([1,3,2]))    # Expected output: false
