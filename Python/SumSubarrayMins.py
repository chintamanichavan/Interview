class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        n = len(arr)
        # Initialize arrays to store the distance to the next and previous smaller elements
        left, right = [0] * n, [0] * n
        stack = []

        # Calculate distances to the previous smaller element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Clear the stack for the next calculation
        stack.clear()

        # Calculate distances to the next smaller element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Calculate the sum of minimums for all subarrays
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD
