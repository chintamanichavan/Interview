class Solution():
    def summaryRanges(self, nums):
        if not nums:
            return []

        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([n])
            else:
                ranges[-1].append(n)
        return ['->'.join(map(str, r)) if len(r) > 1 else str(r[0]) for r in ranges]


def main():
    nums = [0,2,3,4,6,8,9]
    s = Solution()
    res = s.summaryRanges(nums)
    print(res)

if __name__ == '__main__':
    main()
