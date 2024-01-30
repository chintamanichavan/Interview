class Solution:
    def getPermutation(self, n: int, k: int) -> str:
    
        # Factorials
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)

        # Initialize list of numbers to get digits from
        numbers = [str(i) for i in range(1, n + 1)]

        # Adjust k to be zero-indexed
        k -= 1

        # Build the kth permutation
        kth_permutation = ""
        for i in range(n):
            index = k // factorials[n - i - 1]
            kth_permutation += numbers[index]
            numbers.pop(index)
            k %= factorials[n - i - 1]

        return kth_permutation
