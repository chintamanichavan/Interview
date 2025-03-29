
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0  # Initialize a counter for consecutive odd numbers

        for num in arr:
            if num % 2 == 1:  # Check if the number is odd
                count += 1
                if count == 3:  # If we find three consecutive odds, return true
                    return True
            else:
                count = 0  # Reset the counter if the number is even

        return False  # Return false if no three consecutive odds are found

# Example usage:
sol = Solution()
print(sol.threeConsecutiveOdds([2, 6, 4, 1]))  # Output: False
print(sol.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Output: True
