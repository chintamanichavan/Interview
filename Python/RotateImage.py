from typing import List

class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        l,r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                #save the topLeft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1

        return matrix


def main():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.rotate(matrix))

if __name__ == "__main__":
    main()
