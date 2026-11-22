package P0001_TwoSum;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] result1 = solution.twoSum(new int[]{2, 7, 11, 15},9);
        System.out.println(Arrays.toString(result1));

        int[] result2 = solution.twoSum(new int[]{-3, 4, 3, 90},0);
        System.out.println(Arrays.toString(result2));

        int[] result3 = solution.twoSum(new int[]{2, 7, 11, 15},18);
        System.out.println(Arrays.toString(result3));

        int[] result4 = solution.twoSum(new int[]{2, 7, 11, 15},26);
        System.out.println(Arrays.toString(result4));

        int[] result5 = solution.twoSum(new int[]{2, 7, 11, 15},22);
        System.out.println(Arrays.toString(result5));

    }
}
