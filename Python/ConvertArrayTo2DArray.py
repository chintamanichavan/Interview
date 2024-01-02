class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        rows = []
        num_in_row = {}

        for num in nums:
            placed = False
            for i, row in enumerate(rows):
                if num not in num_in_row.get(i, set()):
                    row.append(num)
                    num_in_row.setdefault(i, set()).add(num)
                    placed = True
                    break

            if not placed:
                rows.append([num])
                num_in_row[len(rows) - 1] = {num}

        return rows
