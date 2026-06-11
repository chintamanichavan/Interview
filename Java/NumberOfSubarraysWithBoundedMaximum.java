public class NumberOfSubarraysWithBoundedMaximum {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        return count(nums, right) - count(nums, left - 1);
    }

    private int count(int[] nums, int bound) {
        int total = 0, length = 0;
        for (int x : nums) {
            length = (x <= bound) ? length + 1 : 0;
            total += length;
        }
        return total;
    }

    public static void main(String[] args) {
        NumberOfSubarraysWithBoundedMaximum s = new NumberOfSubarraysWithBoundedMaximum();
        System.out.println(s.numSubarrayBoundedMax(new int[] { 2, 1, 4, 3 }, 2, 3));    // 3
        System.out.println(s.numSubarrayBoundedMax(new int[] { 2, 9, 2, 5, 6 }, 2, 8)); // 7
        System.out.println(s.numSubarrayBoundedMax(new int[] { 1, 1, 1 }, 1, 1));       // 6
    }
}
