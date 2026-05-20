public class MinimumCommonValue {
    public int getCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) return nums1[i];
            if (nums1[i] < nums2[j]) i++;
            else j++;
        }
        return -1;
    }

    public static void main(String[] args) {
        MinimumCommonValue s = new MinimumCommonValue();
        System.out.println(s.getCommon(new int[] { 1, 2, 3 }, new int[] { 2, 4 }));          // 2
        System.out.println(s.getCommon(new int[] { 1, 2, 3, 6 }, new int[] { 2, 3, 4, 5 })); // 2
        System.out.println(s.getCommon(new int[] { 1, 2 }, new int[] { 3, 4 }));             // -1
    }
}
