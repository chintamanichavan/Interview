class Solution:
    def MergeSortedArray(self, nums1, m, nums2, n):
    # nums1 and nums2 are two integer arrays and they are sorted in non-decreasing order
    # m and n represent the number of elements in the nums1 and nums2
        pointer1 = m - 1 # pointer1 and pointer2 are pointers for nums1 and nums2 respectively.
        pointer2 = n - 1
        pointer = m + n - 1 # Set pointer to last index of modification in nums1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[pointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1

            pointer -= 1

        # Fill the remaining with leftover elements
        nums1[:pointer2+1] = nums2[:pointer2+1]
        print("Sorted Array: " + str(nums1))

def main():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    s = Solution()
    s.MergeSortedArray(nums1, m, nums2, n)

if __name__ == '__main__':
    main()
