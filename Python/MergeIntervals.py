class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

def main():
    # Instantiate the Solution class
    solution = Solution()

    # Provide intervals as input
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    # Call the merge method of the Solution class
    result = solution.merge(intervals)

    # Print the result
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
