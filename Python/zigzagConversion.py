class Solution():
    def Zigzag(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        row, step = 0, 1

        for char in s:
            result[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(result)


def main():
    s = "PAYPALISHIRING"
    numRows = 4
    sol = Solution()
    res = sol.Zigzag(s, numRows)
    print(res)

if __name__ == '__main__':
    main()
