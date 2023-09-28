def sortArrayByParity(nums):
    i, j = 0, len(nums) - 1
    
    while i <= j:
        if nums[i] % 2 == 0:
            i += 1
        elif nums[j] % 2 == 1:
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    return nums

# Test the function with the given examples
print(sortArrayByParity([3,1,2,4]))  # Possible output: [4,2,3,1]
print(sortArrayByParity([0]))        # Expected output: [0]
