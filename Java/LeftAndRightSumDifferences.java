import java.util.Arrays;

public class LeftAndRightSumDifferences {
    public int[] leftRightDifference(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        int[] ans = new int[nums.length];
        int left = 0;
        for (int i = 0; i < nums.length; i++) {
            int right = total - left - nums[i];
            ans[i] = Math.abs(left - right);
            left += nums[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        LeftAndRightSumDifferences s = new LeftAndRightSumDifferences();
        System.out.println(Arrays.toString(s.leftRightDifference(new int[] { 10, 4, 8, 3 }))); // [15, 1, 11, 22]
        System.out.println(Arrays.toString(s.leftRightDifference(new int[] { 1 })));           // [0]
    }
}
