class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # Dictionary to hold the diagonals
        diagonals = {}

        # Iterate through each element and add it to the corresponding diagonal
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(nums[i][j])

        # Traverse diagonals and reverse each diagonal's elements
        result = []
        for diagonal in diagonals.values():
            result.extend(diagonal[::-1])

        return result
