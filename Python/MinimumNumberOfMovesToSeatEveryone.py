
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)

        return total_moves

# Example usage:
# sol = Solution()
# print(sol.minMovesToSeat([3,1,5], [2,7,4]))  # Output: 4
# print(sol.minMovesToSeat([4,1,5,9], [1,3,2,6]))  # Output: 7
# print(sol.minMovesToSeat([2,2,6,6], [1,3,2,6]))  # Output: 4
