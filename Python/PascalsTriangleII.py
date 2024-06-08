class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex+1)
        if rowIndex == 0: return row
        prev_row = self.getRow(rowIndex-1)
        for i in range(1, len(row)-1):
            row[i] = prev_row[i-1] + prev_row[i]
        return row

# review 2024-01-14

# review 2024-03-16

# review 2024-06-07
